package com.goglotek.mydacapp.models;

public class Home {
    private static Home sHome;
    private Response[] mData;

    private Home(Response[] data) {
        this.mData = data;
    }

    public static Home getInstance(Response[] data) {
        if (sHome == null) {
            sHome = new Home(data);
        } else {
            sHome.setData(data);
        }
        return sHome;
    }

    public Response[] getData() {
        return mData;
    }

    public void setData(Response[] data) {
        this.mData = data;
    }
}
