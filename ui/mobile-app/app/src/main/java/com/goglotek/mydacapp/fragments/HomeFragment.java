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
        createHomeDataWebSocketListener(view);
        return view;
    }

    private void handleSettingsOnclick() {
        requireActivity().getSupportFragmentManager()
                .beginTransaction()
                .replace(R.id.fragment_container, new AppFragment())
                .addToBackStack(null)
                .commit();
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
                ((Activity) getContext()).runOnUiThread(() -> {
                    int volume = 0;
                    StringBuilder sb = new StringBuilder();
                    Response[] data = finalHomeLocal != null ? finalHomeLocal.getData() : null;
                    if (data != null) {
                        for (Response rsp : finalHomeLocal.getData()) {
                            if (rsp.getKey().equals(Config.getConfig("CURRENT_VOLUME_ID"))) {
                                volume = Integer.parseInt(rsp.getValue());
                            } else {
                                sb.append(" " + rsp.getDisplayName()).append(": ").append(rsp.getValue());
                            }
                        }
                    }
                    volumeView = volumeView == null ? ((Activity) getContext()).findViewById(R.id.speedView) : volumeView;
                    volumeView.setTrembleData(0, 0);
                    volumeView.speedTo(volume, 200);
                    if (!updatingSliderVolume) {
                        volumeSlider.setValue(volume);
                    }
                    if (!isWsData) {
                        homeData = homeData == null ? ((Activity) getContext()).findViewById((R.id.home_data)) : homeData;
                        homeData.setText(sb.toString());
                    }
                });
            } catch (GoglotekException e) {
                e.printStackTrace();
            }
        });
    }

    private void handleVolumeSliderOnchange(int newVal) {

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
                    ((Activity) getContext()).runOnUiThread(() -> {
                        updatingSliderVolume = false;
                    });
                } catch (GoglotekException e) {
                    e.printStackTrace();
                }
            });
        }
        previousSliderVolume = newVal;

    }

    private void createHomeDataWebSocketListener(View view) {
        WebSocketClient client = new WebSocketClient(Config.getConfig("BASE_URL") + "system/ws", new WebsocketHandler() {
            @Override
            public void handleIncomingMessage(String message) {
                try {
                    Response[] rsp = new ObjectMapper().readValue(message, Response[].class);
                    Home home = Home.getInstance(rsp);
                    populateHomeData(home, true);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        client.connect();
    }
}
