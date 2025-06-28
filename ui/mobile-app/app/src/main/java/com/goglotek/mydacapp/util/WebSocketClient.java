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

    public WebSocketClient(String url, WebsocketHandler handler) {
        this.handler = handler;
        this.URL = url;
    }

    public void connect() {
        OkHttpClient client = new OkHttpClient();

        Request request = new Request.Builder()
                .url(URL)
                .build();

        WebSocketListener listener = WebsocketListener.getInstance(handler);
        webSocket = client.newWebSocket(request, listener);
    }
}

class WebsocketListener extends WebSocketListener {
    private WebsocketHandler handler;

    private WebsocketListener(WebsocketHandler handler) {
        this.handler = handler;
    }

    public static WebsocketListener getInstance(WebsocketHandler handler) {
        return new WebsocketListener(handler);
    }

    @Override
    public void onMessage(WebSocket webSocket, String text) {
        handler.handleIncomingMessage(text);
    }


    @Override
    public void onClosing(WebSocket webSocket, int code, String reason) {
        webSocket.close(1000, null);
        System.out.println("Closing : " + code + " / " + reason);
    }

    @Override
    public void onFailure(WebSocket webSocket, Throwable t, Response response) {
        t.printStackTrace();
    }

}

