package com.goglotek.mydacapp.activities;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

import com.goglotek.mydacapp.R;

public abstract class DacAppActivity extends AppCompatActivity {
    protected abstract Fragment getFragment();

    @Override
    protected void onCreate(Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_main);
        FragmentManager fManager = getSupportFragmentManager();
        Fragment fragment = fManager.findFragmentById(R.id.fragment_container);
        if (fragment == null) {
            fragment = getFragment();
            fManager.beginTransaction().add(R.id.fragment_container, fragment).commit();
        }
    }
}
