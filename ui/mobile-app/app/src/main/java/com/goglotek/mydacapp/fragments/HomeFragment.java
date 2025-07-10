package com.goglotek.mydacapp.fragments;


import android.app.Activity;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.SeekBar;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.github.anastr.speedviewlib.SpeedView;
import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.Menu;
import com.goglotek.mydacapp.menu.MenuUtil;
import com.goglotek.mydacapp.models.Home;
import com.goglotek.mydacapp.models.Response;
import com.goglotek.mydacapp.service.SystemService;
import com.goglotek.mydacapp.util.Config;
import com.goglotek.mydacapp.util.VolumeDirection;
import com.goglotek.mydacapp.util.WebSocketClient;
import com.goglotek.mydacapp.util.WebsocketHandler;
import com.google.android.material.slider.Slider;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import timber.log.Timber;

public class HomeFragment extends Fragment {
    SpeedView volumeView;
    Slider volumeSlider;
    Button settings;
    TextView homeData;
    int previousSliderVolume;
    boolean updatingSliderVolume = false;
    Handler handler = new Handler(Looper.getMainLooper());
    Runnable debouncedRunnable = null;
    int debounceDelayMs = 300;
    boolean isVolumeSliderWsUpdate = false;

    @Override
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle bundle) {
        View view = inflater.inflate(R.layout.home, container, false);
        settings = view.findViewById(R.id.settingsBtn);
        settings.setOnClickListener((View) -> handleSettingsOnclick());
        volumeSlider = view.findViewById(R.id.slider);
        previousSliderVolume = (int) volumeSlider.getValue();
        volumeSlider.addOnChangeListener((slider, newVal, b) -> {
            if (debouncedRunnable != null) {
                handler.removeCallbacks(debouncedRunnable);
            }
            debouncedRunnable = () -> {
                handleVolumeSliderOnchange((int) newVal);
            };
            handler.postDelayed(debouncedRunnable, debounceDelayMs);
        });
        //get current volume and other home data from server
        populateHomeData(null, false);
        //creates a web socket to listen for server changes in volume and update the ui.
        createHomeDataWebSocketListener();
        return view;
    }

    private void handleSettingsOnclick() {
        try {
            requireActivity().getSupportFragmentManager()
                    .beginTransaction()
                    .replace(R.id.fragment_container, new MainTabFragment())
                    .addToBackStack(null)
                    .commit();
        } catch (Exception e) {
            Timber.e(e, e.getMessage());
        }
    }

    private void populateHomeData(Home home, boolean isWsData) {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        executor.execute(() -> {
            try {
                Home homeLocal = null;
                if (home == null) {
                    homeLocal = SystemService.getHomeData();
                } else {
                    homeLocal = home;
                }
                Home finalHomeLocal = homeLocal;
                requireActivity().runOnUiThread(() -> {
                    Integer volume = null;
                    StringBuilder sb = new StringBuilder();
                    Response[] data = finalHomeLocal != null ? finalHomeLocal.getData() : null;
                    if (data != null) {
                        for (Response rsp : finalHomeLocal.getData()) {
                            if (rsp.getKey().equals(Config.getConfig("CURRENT_VOLUME_ID"))) {
                                volume = Integer.parseInt(rsp.getValue());
                            } else {
                                sb.append(" " + rsp.getDisplayName().trim()).append(":").append(rsp.getValue().trim()).append("\n");
                            }
                        }
                    }
                    volumeView = volumeView == null ? ((Activity) getContext()).findViewById(R.id.speedView) : volumeView;
                    volumeView.setTrembleData(0, 0);
                    if (volume != null) {
                        volumeView.speedTo(volume, 200);
                    }
                    if (!updatingSliderVolume) {
                        if (volume != null) {
                            isVolumeSliderWsUpdate = true;
                            volumeSlider.setValue(volume);
                        }
                    }
                    homeData = homeData == null ? ((Activity) getContext()).findViewById((R.id.home_data)) : homeData;
                    homeData.setText(processHomeText(homeData.getText().toString(), sb.toString()));
                });
            } catch (GoglotekException e) {
                Timber.e(e, e.getMessage());
            }
        });
    }

    private String processHomeText(String currentText, String serverText) {//updates only fields received from server and keeps current fields not in server payload
        if (serverText.trim().isEmpty()) {
            return currentText;
        }
        String[] txt = serverText.trim().split("\n");
        String buffer = "";
        String processedText = "";
        while (currentText.length() > 0) {
            if (!currentText.contains(":")) {
                break;
            }
            buffer = currentText.substring(0, currentText.indexOf(":")).trim();
            boolean found = false;
            for (int i = 0; i < txt.length; i++) {
                if (txt[i] != null) {
                    if (txt[i].contains(buffer.trim())) {
                        processedText += txt[i].trim() + " ";
                        found = true;
                        txt[i] = null;
                    }
                }
            }
            currentText = currentText.substring(buffer.length() + 1).trim();
            String text = "";
            if (currentText.contains(" ")) {
                text = currentText.substring(0, currentText.indexOf(" "));
            } else {
                text = currentText.substring(0);
            }
            if (!found) {
                processedText += buffer.trim() + ":" + text.trim() + " ";
            }
            if (currentText.length() > text.length()) {
                currentText = currentText.substring(text.length() + 1);
            } else {
                currentText = "";
            }
        }
        for (int i = 0; i < txt.length; i++) {
            if (txt[i] != null) {
                processedText += txt[i];
            }
        }
        return processedText.trim();
    }

    private void handleVolumeSliderOnchange(int newVal) {
        //if slider change was as a result of websocket update, don't process the event and reset the flag
        if (isVolumeSliderWsUpdate) {
            isVolumeSliderWsUpdate = false;
            return;
        }
        if (newVal != previousSliderVolume) {
            VolumeDirection direction = null;
            if (newVal > previousSliderVolume) {
                direction = VolumeDirection.UP;
            } else {
                direction = VolumeDirection.DOWN;
            }
            VolumeDirection finalDirection = direction;
            updatingSliderVolume = true;
            ExecutorService executor = Executors.newSingleThreadExecutor();
            executor.execute(() -> {
                try {
                    int count = 0;
                    int volume;
                    while (true) {
                        volume = SystemService.updateVolume(finalDirection);
                        if (finalDirection == VolumeDirection.UP) {
                            if (volume >= newVal) {
                                break;
                            }
                        } else {
                            if (volume <= newVal) {
                                break;
                            }
                        }
                        //just in case there is an issue, the loop wont run forever
                        count++;
                        if (count > 2000) {
                            break;
                        }
                    }
                    requireActivity().runOnUiThread(() -> {
                        updatingSliderVolume = false;
                    });
                } catch (GoglotekException e) {
                    Timber.e(e, e.getMessage());
                }
            });
        }
        previousSliderVolume = newVal;

    }

    private void createHomeDataWebSocketListener() {
        WebSocketClient client = new WebSocketClient(Config.getConfig("BASE_URL") + "system/ws", new WebsocketHandler() {
            @Override
            public void handleIncomingMessage(String message) {
                try {
                    Response[] rsp = new ObjectMapper().readValue(message, Response[].class);
                    Home home = Home.getInstance(rsp);
                    populateHomeData(home, true);
                } catch (Exception e) {
                    Timber.e(e, e.getMessage());
                }
            }

            @Override
            public void postDelayed(WebSocketClient client, long delay) {
                try {
                    Thread.sleep(delay);
                    client.connect();
                } catch (InterruptedException e) {
                    Timber.e(e, e.getMessage());
                }
            }
        });
        client.connect();
    }
}
