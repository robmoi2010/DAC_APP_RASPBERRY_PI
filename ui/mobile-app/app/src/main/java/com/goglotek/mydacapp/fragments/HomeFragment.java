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

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.github.anastr.speedviewlib.SpeedView;
import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.App;
import com.goglotek.mydacapp.dataprocessors.GenericDataProcessor;
import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.exceptions.NullDataException;
import com.goglotek.mydacapp.menu.Menu;
import com.goglotek.mydacapp.menu.MenuUtil;
import com.goglotek.mydacapp.models.Request;
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
        volumeSlider.addOnSliderTouchListener(new Slider.OnSliderTouchListener() {
                                                  @Override
                                                  public void onStartTrackingTouch(@NonNull Slider slider) {
                                                  }

                                                  @Override
                                                  public void onStopTrackingTouch(@NonNull Slider slider) {
                                                      handleVolumeSliderOnchange((int) slider.getValue());
                                                  }
                                              }
        );
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
                    float current = volumeSlider.getValue();
                    if (current >= 100) {
                        return;
                    }
                    float ret = Float.parseFloat(volumeUpProcessor.sendGet().getValue());
                    while (ret < current + VOLUME_BTN_STEPS) {
                        ret = Float.parseFloat(volumeUpProcessor.sendGet().getValue());
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
                    float current = volumeSlider.getValue();
                    if (current <= 0) {
                        return;
                    }
                    float ret = Float.parseFloat(volumeDownProcessor.sendGet().getValue());
                    while (ret > current - VOLUME_BTN_STEPS) {
                        ret = Float.parseFloat(volumeDownProcessor.sendGet().getValue());
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
                if (resp == null) {
                    respLocal = homeDataProcessor.sendGetArrayResponse();
                } else {
                    respLocal = resp;
                }
                Response[] finalRespLocal = respLocal;
                requireActivity().runOnUiThread(() -> {
                    Float volume = null;
                    StringBuilder sb = new StringBuilder();
                    if (finalRespLocal == null) {
                        return;
                    }
                    for (Response rsp : finalRespLocal) {
                        if (rsp.getKey().equals(Config.getConfig("CURRENT_VOLUME_ID"))) {
                            volume = Float.parseFloat(rsp.getValue());
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
            isManualSliderChange = true;
            ExecutorService executor = Executors.newSingleThreadExecutor();
            executor.execute(() -> {
                try {
                    GenericDataProcessor processor = GenericDataProcessor.getInstance(App.webClientMap.get(WebClientType.VOLUME_UPDATE));
                    Request r = new Request("0", "" + newVal);
                    processor.sendPut(new ObjectMapper().writeValueAsString(r));
                    requireActivity().runOnUiThread(() -> {
                        isManualSliderChange = false;
                    });
                } catch (GoglotekException e) {
                    Timber.e(e, e.getMessage());
                } catch (JsonProcessingException e) {
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
