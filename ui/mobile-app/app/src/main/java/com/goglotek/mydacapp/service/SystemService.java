package com.goglotek.mydacapp.service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.goglotek.mydacapp.models.Home;
import com.goglotek.mydacapp.models.Response;
import com.goglotek.mydacapp.util.Config;
import com.goglotek.mydacapp.util.RestClient;
import com.goglotek.mydacapp.util.VolumeDirection;

import okhttp3.OkHttpClient;

public class SystemService {

    static String BASE_URL = Config.getConfig("BASE_URL");

    public static Home getHomeData() {
        String data = RestClient.getInstance(new OkHttpClient()).get(BASE_URL + "system/home");
        try {
            Response[] dt = new ObjectMapper().readValue(data, Response[].class);
            Home home = Home.getInstance(dt);
            return home;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public static void updateVolume(VolumeDirection direction) {
        String url = BASE_URL + ((direction == VolumeDirection.UP) ? "system/volume/up" : "system/volume/down");
        RestClient.getInstance(new OkHttpClient()).get(url);
    }
}
