package com.goglotek.mydacapp.service;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.util.Config;
import com.goglotek.mydacapp.util.RestClient;

import okhttp3.OkHttpClient;

public class DspService {
    static String BASE_URL = Config.getConfig("BASE_URL");

    public static String getInputOptions() throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).get(BASE_URL + "dsp/input");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String updateInput(String data) throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).put(BASE_URL + "dsp/input", data);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String getMainsOutputOptions() throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).get(BASE_URL + "dsp/output/mains");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String updateMainsOutput(String data) throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).put(BASE_URL + "dsp/output/mains", data);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String getSubwooferOutputOptions() throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).get(BASE_URL + "dsp/output/subwoofer");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String updateSubwooferOutput(String data) throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).put(BASE_URL + "dsp/output/subwoofer", data);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }
}
