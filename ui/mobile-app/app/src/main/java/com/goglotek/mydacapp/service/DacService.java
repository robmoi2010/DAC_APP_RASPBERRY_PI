package com.goglotek.mydacapp.service;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.util.Config;
import com.goglotek.mydacapp.util.RestClient;

import okhttp3.OkHttpClient;

public class DacService {
    static String BASE_URL = Config.getConfig("BASE_URL");

    public static String getFilters() throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).get(BASE_URL + "dac/filters");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String getVolumeDisableStatus() throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).get(BASE_URL + "dac/volume/status");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String updateFilter(String data) throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).post(BASE_URL + "dac/filters", data);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String updateVolumeStatus(String data) throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).post(BASE_URL + "dac/volume/status", data);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String getDacModes() throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).get(BASE_URL + "dac/dac_modes");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String updateDacMode(String data) throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).post(BASE_URL + "dac/dac_modes", data);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String getVolumeModes() throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).get(BASE_URL + "dac/volume_modes");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String updateVolumeModes(String data) throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).post(BASE_URL + "dac/volume_modes", data);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String getSecondOrderStatus() throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).get(BASE_URL + "dac/thd_compensation/second_order/status");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String updateSecondOrderStatus(String data) throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).post(BASE_URL + "dac/thd_compensation/second_order/status", data);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String getThirdOrderStatus() throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).get(BASE_URL + "dac/thd_compensation/third_order/status");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String updateThirdOrderStatus(String data) throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).post(BASE_URL + "dac/thd_compensation/third_order/status", data);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String getOversamplingStatus() throws GoglotekException {
        try {
            RestClient.getInstance(new OkHttpClient()).get(BASE_URL + "dac/oversampling/status");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String updateOversamplingStatus(String data) throws GoglotekException {
        try {
            return RestClient.getInstance(new OkHttpClient()).post(BASE_URL + "dac/oversampling/status", data);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }
}
