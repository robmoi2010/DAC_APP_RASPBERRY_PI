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

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.WebSocket;
import okhttp3.WebSocketListener;

public class WebSocketClient {

  String URL;
  private WebSocket webSocket;
  private WebsocketHandler handler;
  private int MAX_RETRIES = 100;
  private int retryCount = 0;
  private boolean connectionSuccessful = false;

  public WebSocketClient(String url, WebsocketHandler handler) {
    this.handler = handler;
    this.URL = url;
  }

  public void connect() {
    OkHttpClient client = new OkHttpClient();
    Request request = new Request.Builder()
        .url(URL)
        .build();

    WebSocketListener listener = WebsocketListener.getInstance(this, handler);
    webSocket = client.newWebSocket(request, listener);
  }

  public void tryReconnect() {
    if (retryCount < MAX_RETRIES) {
      retryCount++;
      long delay = retryCount * 2000L;
      handler.postDelayed(this, delay);
      System.out.println("Reconnecting in " + delay + " ms... (attempt " + retryCount + ")");
    } else {
      System.out.println("Max retries reached. Not reconnecting.");
    }
  }

  public int getMAX_RETRIES() {
    return MAX_RETRIES;
  }

  public void setMAX_RETRIES(int MAX_RETRIES) {
    this.MAX_RETRIES = MAX_RETRIES;
  }

  public int getRetryCount() {
    return retryCount;
  }

  public void setRetryCount(int retryCount) {
    this.retryCount = retryCount;
  }

  public boolean isConnectionSuccessful() {
    return connectionSuccessful;
  }

  public void setConnectionSuccessful(boolean connectionSuccessful) {
    this.connectionSuccessful = connectionSuccessful;
  }
}

class WebsocketListener extends WebSocketListener {

  private WebsocketHandler handler;
  private WebSocketClient client;


  private WebsocketListener(WebSocketClient client, WebsocketHandler handler) {
    this.handler = handler;
    this.client = client;
  }

  public static WebsocketListener getInstance(WebSocketClient client, WebsocketHandler handler) {
    return new WebsocketListener(client, handler);
  }

  @Override
  public void onOpen(WebSocket webSocket, Response response) {
    client.setConnectionSuccessful(true); // Reset retries
    System.out.println("WebSocket Connected");
    client.setRetryCount(0);
  }

  @Override
  public void onMessage(WebSocket webSocket, String text) {
    handler.handleIncomingMessage(text);
  }


  @Override
  public void onClosing(WebSocket webSocket, int code, String reason) {
    System.out.println("Closing : " + code + " / " + reason);
    webSocket.close(code, reason);
    client.tryReconnect();
  }

  @Override
  public void onFailure(WebSocket webSocket, Throwable t, Response response) {
    t.printStackTrace();
    webSocket.close(1001, "Server failure");
    client.tryReconnect();
  }


}

