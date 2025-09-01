/*
 * Copyright (C) 2025 Robert Moi, Goglotek LTD
 *
 *  This file is part of the DAC_APPLICATION System.
 *
 *  The DAC_APPLICATION System is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  The DAC_APPLICATION is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with the Fraud Detector System. If not, see <https://www.gnu.org/licenses/>
 */

package com.goglotek.mydacapp.util;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class RestClient {

  private static OkHttpClient client = null;
  private static RestClient restClient = null;
  public static final MediaType JSON = MediaType.get("application/json");

  private RestClient() {

  }

  public static RestClient getInstance() {
    if (client == null) {
      client = new OkHttpClient();
    }
    if (restClient == null) {
      restClient = new RestClient();
    }
    return restClient;
  }

  public String get(String url) throws Exception {
    if (client == null) {
      client = new OkHttpClient();
    }
    Request request = new Request.Builder().url(url).get()
        .addHeader("Content-type", "application/json").build();
    try (Response response = client.newCall(request).execute()) {
      return response.body().string();
    }
  }

  public String put(String url, String data) throws Exception {
    if (client == null) {
      client = new OkHttpClient();
    }
    RequestBody body = RequestBody.create(data, JSON);
    Request request = new Request.Builder().url(url).addHeader("Content-type", "application/json")
        .put(body).build();
    try (Response response = client.newCall(request).execute()) {
      return response.body().string();
    }
  }
}