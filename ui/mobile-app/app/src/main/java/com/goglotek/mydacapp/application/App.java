package com.goglotek.mydacapp.application;

import android.app.Application;
import static timber.log.Timber.DebugTree;

import timber.log.Timber;


public class App extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        //if (BuildConfig.DEBUG) {
        Timber.plant(new DebugTree());

    }
}
