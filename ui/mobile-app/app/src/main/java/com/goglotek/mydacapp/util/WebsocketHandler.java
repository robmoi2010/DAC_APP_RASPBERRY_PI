package com.goglotek.mydacapp.util;

public interface WebsocketHandler {
    public void handleIncomingMessage(String message);

    void postDelayed(WebSocketClient client, long delay);
}
