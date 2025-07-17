package com.goglotek.mydacapp.fragments;


import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.fragment.app.Fragment;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.github.anastr.speedviewlib.SpeedView;
import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.App;
import com.goglotek.mydacapp.dataprocessors.GenericDataProcessor;
import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.exceptions.NullDataException;
import com.goglotek.mydacapp.models.Response;
import com.goglotek.mydacapp.models.WebClientType;
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
    boolean isManualSliderChange = false;
    Handler handler = new Handler(Looper.getMainLooper());
    Runnable debouncedRunnable = null;
    int debounceDelayMs = 300;
    boolean isVolumeSliderWsUpdate = false;
    private AlertDialog dialog;
    private GenericDataProcessor homeDataProcessor;
    private GenericDataProcessor volumeUpProcessor;
    private GenericDataProcessor volumeDownProcessor;
    private ImageView volumePlus;
    private ImageView volumeMinus;
    private final int VOLUME_BTN_STEPS = 1;

    @Override
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle bundle) {
        View view = inflater.inflate(R.layout.home, container, false);
        dialog = new AlertDialog.Builder(container.getContext()).create();
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

        volumePlus = view.findViewById(R.id.volumePlus);
        volumeMinus = view.findViewById(R.id.volumeMinus);


        //initialize data processors
        homeDataProcessor = GenericDataProcessor.getInstance(App.webClientMap.get(WebClientType.HOME_DATA));
        volumeUpProcessor = GenericDataProcessor.getInstance(App.webClientMap.get(WebClientType.VOLUME_UP));
        volumeDownProcessor = GenericDataProcessor.getInstance(App.webClientMap.get(WebClientType.VOLUME_DOWN));

        //set volume buttons event listeners
        volumePlus.setOnClickListener((v) -> {
            Executors.newSingleThreadExecutor().execute(() -> {
                try {
                    int current = (int) volumeSlider.getValue();
                    int ret = Integer.parseInt(volumeUpProcessor.sendGet().getValue());
                    while (ret < current + VOLUME_BTN_STEPS) {
                        ret = Integer.parseInt(volumeUpProcessor.sendGet().getValue());
                    }
                } catch (GoglotekException e) {
                    requireActivity().runOnUiThread(() -> {
                        dialog.setMessage(e.getMessage());
                        dialog.show();
                        Timber.e(e, e.getMessage());
                    });
                }
            });
        });
        volumeMinus.setOnClickListener((v) -> {
            Executors.newSingleThreadExecutor().execute(() -> {
                try {
                    int current = (int) volumeSlider.getValue();
                    int ret = Integer.parseInt(volumeDownProcessor.sendGet().getValue());
                    while (ret > current - VOLUME_BTN_STEPS) {
                        ret = Integer.parseInt(volumeDownProcessor.sendGet().getValue());
                    }
                } catch (GoglotekException e) {
                    requireActivity().runOnUiThread(() -> {
                        dialog.setMessage(e.getMessage());
                        dialog.show();
                        Timber.e(e, e.getMessage());
                    });
                }
            });
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
            dialog.setMessage(e.getMessage());
            dialog.show();
            Timber.e(e, e.getMessage());
        }
    }


    private void populateHomeData(Response[] resp, boolean isWsData) {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        executor.execute(() -> {
            try {
                Response[] respLocal = null;
                if (respLocal == null) {
                    respLocal = homeDataProcessor.sendGetArrayResponse();
                } else {
                    respLocal = resp;
                }
                Response[] finalRespLocal = respLocal;
                requireActivity().runOnUiThread(() -> {
                    Integer volume = null;
                    StringBuilder sb = new StringBuilder();
                    if (finalRespLocal == null) {
                        return;
                    }
                    for (Response rsp : finalRespLocal) {
                        if (rsp.getKey().equals(Config.getConfig("CURRENT_VOLUME_ID"))) {
                            volume = Integer.parseInt(rsp.getValue());
                        } else {
                            sb.append(" " + rsp.getDisplayName().trim()).append(":").append(rsp.getValue().trim()).append("\n");
                        }
                    }
                    volumeView = volumeView == null ? requireActivity().findViewById(R.id.speedView) : volumeView;
                    volumeView.setTrembleData(0, 0);
                    if (volume != null) {
                        volumeView.speedTo(volume, 200);
                    }
                    if (!isManualSliderChange) {
                        if (volume != null) {
                            isVolumeSliderWsUpdate = true;
                            volumeSlider.setValue(volume);
                        }
                    }
                    homeData = homeData == null ? requireActivity().findViewById((R.id.home_data)) : homeData;
                    homeData.setText(processHomeText(homeData.getText().toString(), sb.toString()));
                    isVolumeSliderWsUpdate = false;
                });
            } catch (GoglotekException e) {
                requireActivity().runOnUiThread(() -> {
                    dialog.setMessage(e.getMessage());
                    dialog.show();
                });
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
            isManualSliderChange = true;
            ExecutorService executor = Executors.newSingleThreadExecutor();
            executor.execute(() -> {
                try {
                    int count = 0;
                    int volume;
                    while (true) {
                        String data = (finalDirection == VolumeDirection.UP) ? volumeUpProcessor.sendGet().getValue() : volumeDownProcessor.sendGet().getValue();
                        volume = Integer.parseInt(data);
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
                        isManualSliderChange = false;
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
                    populateHomeData(rsp, true);
                } catch (Exception e) {
                    dialog.setMessage(e.getMessage());
                    dialog.show();
                    Timber.e(e, e.getMessage());
                }
            }

            @Override
            public void postDelayed(WebSocketClient client, long delay) {
                try {
                    Thread.sleep(delay);
                    client.connect();
                } catch (InterruptedException e) {
                    dialog.setMessage(e.getMessage());
                    dialog.show();
                    Timber.e(e, e.getMessage());
                }
            }
        });
        client.connect();
    }
}
