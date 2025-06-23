package com.goglotek.mydacapp.models;

public class Home {
    private static Home sHome;
    private int mCurrentVolume;
    private String[] mData;

    private Home(int currentVolume, String[] data) {
        this.mCurrentVolume = currentVolume;
        this.mData = data;

    }

    public static Home getInstance(int currentVolume, String[] data) {
        if (sHome == null) {
            sHome = new Home(currentVolume, data);
        }
        return sHome;
    }

    public int getCurrentVolume() {
        return mCurrentVolume;
    }

    public void setCurrentVolume(int currentVolume) {
        this.mCurrentVolume = currentVolume;
    }

    public String[] getData() {
        return mData;
    }

    public void setData(String[] data) {
        this.mData = data;
    }
}
