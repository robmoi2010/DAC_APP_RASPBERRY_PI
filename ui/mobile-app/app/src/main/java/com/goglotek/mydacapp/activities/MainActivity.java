package com.goglotek.mydacapp.activities;

import android.os.Bundle;

import androidx.fragment.app.Fragment;

import com.goglotek.mydacapp.fragments.AppFragment;
import com.goglotek.mydacapp.fragments.HomeFragment;

public class MainActivity extends DacAppActivity {
    @Override
    public void onSaveInstanceState(Bundle saveInstanceStateBundle) {
        super.onSaveInstanceState(saveInstanceStateBundle);
    }

    @Override
    public void onStart() {
        super.onStart();
        System.out.println("starting...");
    }

    @Override
    public void onPause() {
        super.onPause();
        System.out.println("paused..");
    }

    @Override
    public void onStop() {
        super.onStop();
        System.out.println("stopped...");
    }

    @Override
    public void onResume() {
        super.onResume();
        System.out.println("Resumed...");
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        System.out.println("destroyed...");
    }

    @Override
    protected Fragment getFragment() {
        return new HomeFragment();
    }
}
