package com.goglotek.mydacapp.models;

public class WebClient {
    private String getURL;
    private String postURL;
    private String putURL;
    private WebClientType clientType;

    private WebClient(String getURL, String postURL, String putURL, WebClientType clientType) {
        this.getURL = getURL;
        this.postURL = postURL;
        this.putURL = putURL;
        this.clientType = clientType;
    }

    private WebClient() {

    }

    public static WebClient getInstance() {
        return new WebClient();
    }

    public static WebClient getInstance(String getURL, String postURL, String putURL, WebClientType clientType) {
        return new WebClient(getURL, postURL, putURL, clientType);
    }

    public String getGetURL() {
        return getURL;
    }

    public void setGetURL(String getURL) {
        this.getURL = getURL;
    }

    public String getPostURL() {
        return postURL;
    }

    public void setPostURL(String postURL) {
        this.postURL = postURL;
    }

    public String getPutURL() {
        return putURL;
    }

    public void setPutURL(String putURL) {
        this.putURL = putURL;
    }

    public WebClientType getClientType() {
        return clientType;
    }

    public void setClientType(WebClientType clientType) {
        this.clientType = clientType;
    }
}
