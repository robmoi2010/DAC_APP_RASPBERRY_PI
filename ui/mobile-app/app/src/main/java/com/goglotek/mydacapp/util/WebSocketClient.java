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

