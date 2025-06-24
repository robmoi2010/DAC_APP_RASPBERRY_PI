package com.goglotek.mydacapp.service;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.util.Config;
import com.goglotek.mydacapp.util.RestClient;

import okhttp3.OkHttpClient;

public class DspService {
    static String BASE_URL = Config.getConfig("BASE_URL");
}
