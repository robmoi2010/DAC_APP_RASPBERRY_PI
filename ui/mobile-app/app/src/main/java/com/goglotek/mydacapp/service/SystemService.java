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
            String data = RestClient.getInstance(new OkHttpClient()).get(BASE_URL + "system/home");
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

    public static void updateVolume(VolumeDirection direction) throws GoglotekException {
        try {
            String url = BASE_URL + ((direction == VolumeDirection.UP) ? "system/volume/up" : "system/volume/down");
            RestClient.getInstance(new OkHttpClient()).get(url);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }
}
