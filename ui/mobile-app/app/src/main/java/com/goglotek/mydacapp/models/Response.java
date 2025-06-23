package com.goglotek.mydacapp.models;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Response {
    private String key;
    private String value;
    @JsonProperty("display_name")
    private String displayName;

    public Response() {

    }

    public Response(String key, String value, String displayName) {
        this.key = key;
        this.value = value;
        this.displayName = displayName;
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public String getDisplayName() {
        return displayName;
    }

    public void setDisplayName(String displayName) {
        this.displayName = displayName;
    }
}
