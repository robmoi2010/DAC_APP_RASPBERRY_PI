package com.goglotek.mydacapp.activities;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

import com.goglotek.mydacapp.R;

public abstract class DacAppActivity extends AppCompatActivity {
    protected abstract Fragment getFragment();

    Toolbar toolbar;

    @Override
    protected void onCreate(Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_main);
        toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        if (getSupportActionBar() != null) {
            getSupportActionBar().setDisplayHomeAsUpEnabled(true); // Show back arrow
            getSupportActionBar().setDisplayShowHomeEnabled(true);
        }
        toolbar.setNavigationOnClickListener(v -> onBackPressed());
        FragmentManager fManager = getSupportFragmentManager();
        Fragment fragment = getFragment();
        fManager.beginTransaction().replace(R.id.fragment_container, fragment).commit();
    }

}
