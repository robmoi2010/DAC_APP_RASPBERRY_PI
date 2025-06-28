package com.goglotek.mydacapp.service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.exceptions.NullDataException;
import com.goglotek.mydacapp.models.Home;
import com.goglotek.mydacapp.models.Response;
import com.goglotek.mydacapp.util.Config;
import com.goglotek.mydacapp.util.RestClient;
import com.goglotek.mydacapp.util.VolumeDirection;

import okhttp3.OkHttpClient;

public class SystemService {
    static String BASE_URL = Config.getConfig("BASE_URL");

    public static Home getHomeData() throws GoglotekException {
        try {
            String data = RestClient.getInstance().get(BASE_URL + "system/home");
            if (data != null) {
                Response[] dt = new ObjectMapper().readValue(data, Response[].class);
                Home home = Home.getInstance(dt);
                return home;
            } else {
                throw new NullDataException("Null data from server");
            }
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static int updateVolume(VolumeDirection direction) throws GoglotekException {
        try {
            String url = BASE_URL + ((direction == VolumeDirection.UP) ? "system/volume/up" : "system/volume/down");
            String data = RestClient.getInstance().get(url);
            Response r = new ObjectMapper().readValue(data, Response.class);
            return Integer.parseInt(r.getValue());
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String getVolumeDevice() throws GoglotekException {
        try {
            return RestClient.getInstance().get(BASE_URL + "system/volume_device");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String updateVolumeDevice(String data) throws GoglotekException {
        try {
            return RestClient.getInstance().put(BASE_URL + "system/volume_device", data);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String getVolumeAlgorithm() throws GoglotekException {
        try {
            return RestClient.getInstance().get(BASE_URL + "system/volume_algorithm");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String updateVolumeAlgorithm(String data) throws GoglotekException {
        try {
            return RestClient.getInstance().put(BASE_URL + "system/volume_algorithm", data);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String getSoundModes() throws GoglotekException {
        try {
            return RestClient.getInstance().get(BASE_URL + "system/sound_mode");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String updateSoundMode(String data) throws GoglotekException {
        try {
            return RestClient.getInstance().put(BASE_URL + "system/sound_mode", data);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String increaseVolume() throws GoglotekException {
        try {
            return RestClient.getInstance().get(BASE_URL + "system/volume/up");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public static String decreaseVolume() throws GoglotekException {
        try {
            return RestClient.getInstance().get(BASE_URL + "system/volume/down");
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }


}
