package com.goglotek.mydacapp.util;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class RestClient {
    private OkHttpClient client = null;
    private static RestClient restClient = null;
    public static final MediaType JSON = MediaType.get("application/json");

    private RestClient(OkHttpClient client) {
        this.client = client;
    }

    public static RestClient getInstance(OkHttpClient client) {
        if (restClient == null) {
            restClient = new RestClient(client);
        }
        return restClient;
    }

    public String get(String url) {
        if (client == null) {
            client = new OkHttpClient();
        }
        try {

            Request request = new Request.Builder().url(url).get().addHeader("Content-type", "application/json").build();
            try (Response response = client.newCall(request).execute()) {
                return response.body().string();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public String post(String url, String data) {
        if (client == null) {
            client = new OkHttpClient();
        }
        try {
            RequestBody body = RequestBody.create(data, JSON);
            Request request = new Request.Builder().url(url).addHeader("Content-type", "application/json").post(body).build();
            try (Response response = client.newCall(request).execute()) {
                return response.body().string();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

//    public static final MediaType JSON = MediaType.get("application/json");
//
//    OkHttpClient client = new OkHttpClient();
//
//    String post(String url, String json) throws IOException {
//        RequestBody body = RequestBody.create(json, JSON);
//        Request request = new Request.Builder()
//                .url(url)
//                .post(body)
//                .build();
//        try (Response response = client.newCall(request).execute()) {
//            return response.body().string();
//        }
//    }
}
