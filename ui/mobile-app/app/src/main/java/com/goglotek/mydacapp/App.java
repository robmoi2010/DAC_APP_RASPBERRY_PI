package com.goglotek.mydacapp;

import android.app.Application;
import android.util.Log;

import com.goglotek.mydacapp.models.WebClient;
import com.goglotek.mydacapp.models.WebClientType;

import java.util.HashMap;
import java.util.Map;

import timber.log.Timber;


public class App extends Application {
    public class MyDebugTree extends Timber.Tree {
        @Override
        protected void log(int priority, String tag, String message, Throwable t) {
            String level;
            switch (priority) {
                case Log.VERBOSE:
                    level = "VERBOSE";
                    break;
                case Log.DEBUG:
                    level = "DEBUG";
                    break;
                case Log.INFO:
                    level = "INFO";
                    break;
                case Log.WARN:
                    level = "WARN";
                    break;
                case Log.ERROR:
                    level = "ERROR";
                    break;
                case Log.ASSERT:
                    level = "ASSERT";
                    break;
                default:
                    level = "UNKNOWN";
                    break;
            }

            String formatted = String.format("[%s] %s: %s", level, tag, message);

            // Print to Logcat
            Log.println(priority, "MyCustomTree", formatted);

            // If throwable exists, log it too
            if (t != null) {
                Log.println(priority, "MyCustomTree", Log.getStackTraceString(t));
            }
        }

    }


    public static Map<WebClientType, WebClient> webClientMap = new HashMap<>();

    @Override
    public void onCreate() {
        super.onCreate();
        Timber.plant(new MyDebugTree());
        createWebClientsMap();
    }

    public void createWebClientsMap() {
        WebClient client = WebClient.getInstance("system/home", "", "system/home", WebClientType.HOME_DATA);
        webClientMap.put(WebClientType.HOME_DATA, client);

        WebClient client1 = WebClient.getInstance("dac/dpll_bandwidth", "", "dac/dpll_bandwidth", WebClientType.DPLL_BANDWIDTH);
        webClientMap.put(WebClientType.DPLL_BANDWIDTH, client1);

        WebClient client2 = WebClient.getInstance("dac/filters", "", "dac/filters", WebClientType.FILTERS);
        webClientMap.put(WebClientType.FILTERS, client2);

        WebClient client3 = WebClient.getInstance("dsp/input", "", "dsp/input", WebClientType.DSP_INPUT);
        webClientMap.put(WebClientType.DSP_INPUT, client3);

        WebClient client4 = WebClient.getInstance("dsp/input", "", "dsp/input", WebClientType.MAINS_OUTPUT);
        webClientMap.put(WebClientType.MAINS_OUTPUT, client4);

        WebClient client5 = WebClient.getInstance("dac/oversampling/status", "", "dac/oversampling/status", WebClientType.OVERSAMPLING);
        webClientMap.put(WebClientType.OVERSAMPLING, client5);

        WebClient client6 = WebClient.getInstance("dac/thd_compensation/second_order/status", "", "dac/thd_compensation/second_order/status", WebClientType.SECOND_ORDER);
        webClientMap.put(WebClientType.SECOND_ORDER, client6);

        WebClient client7 = WebClient.getInstance("dac/thd_compensation/third_order/status", "", "dac/thd_compensation/third_order/status", WebClientType.THIRD_ORDER);
        webClientMap.put(WebClientType.THIRD_ORDER, client7);

        WebClient client8 = WebClient.getInstance("system/sound_mode", "", "system/sound_mode", WebClientType.SOUND_MODES);
        webClientMap.put(WebClientType.SOUND_MODES, client8);

        WebClient client9 = WebClient.getInstance("", "", "", WebClientType.VOLUME);
        webClientMap.put(WebClientType.VOLUME, client9);

        WebClient client10 = WebClient.getInstance("system/volume_algorithm", "", "system/volume_algorithm", WebClientType.VOLUME_ALGORITHM);
        webClientMap.put(WebClientType.VOLUME_ALGORITHM, client10);

        WebClient client11 = WebClient.getInstance("system/volume/up", "", "", WebClientType.VOLUME_UP);
        webClientMap.put(WebClientType.VOLUME_UP, client11);

        WebClient client12 = WebClient.getInstance("system/volume/down", "", "", WebClientType.VOLUME_DOWN);
        webClientMap.put(WebClientType.VOLUME_DOWN, client12);

        WebClient client13 = WebClient.getInstance("dac/volume/status", "", "dac/volume/status", WebClientType.VOLUME_STATUS);
        webClientMap.put(WebClientType.VOLUME_STATUS, client13);

        WebClient client14 = WebClient.getInstance("dsp/output/subwoofer", "", "dsp/output/subwoofer", WebClientType.SUBWOOFER_OUTPUT);
        webClientMap.put(WebClientType.SUBWOOFER_OUTPUT, client14);

        WebClient client15 = WebClient.getInstance("system/volume_device", "", "system/volume_device", WebClientType.VOLUME_DEVICE);
        webClientMap.put(WebClientType.VOLUME_DEVICE, client15);

        WebClient client16 = WebClient.getInstance("dac/dac_modes", "", "dac/dac_modes", WebClientType.DAC_MODES);
        webClientMap.put(WebClientType.DAC_MODES, client16);

        WebClient client17 = WebClient.getInstance("dac/volume_modes", "", "dac/volume_modes", WebClientType.VOLUME_MODES);
        webClientMap.put(WebClientType.VOLUME_MODES, client17);
    }
}
