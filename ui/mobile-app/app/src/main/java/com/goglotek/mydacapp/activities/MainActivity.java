package com.goglotek.mydacapp.activities;

import android.os.Bundle;
import android.view.MenuItem;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.goglotek.mydacapp.fragments.AppFragment;
import com.goglotek.mydacapp.fragments.HomeFragment;

public class MainActivity extends DacAppActivity {
    @Override
    public void onSaveInstanceState(Bundle saveInstanceStateBundle) {
        super.onSaveInstanceState(saveInstanceStateBundle);
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        if (item.getItemId() == android.R.id.home) {
            onBackPressed();
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
    @Override
    protected Fragment getFragment() {
        return new HomeFragment();
    }
}
