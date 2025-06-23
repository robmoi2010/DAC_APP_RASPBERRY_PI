package com.goglotek.mydacapp.fragments;


import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.SeekBar;

import androidx.fragment.app.Fragment;

import com.github.anastr.speedviewlib.SpeedView;
import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.models.Home;

public class HomeFragment extends Fragment {
    private Home home;
    SpeedView volumeView;
    SeekBar volumeSlider;
    Button settings;

    @Override
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle bundle) {
        View view = inflater.inflate(R.layout.home, container, false);
        return view;
    }
}
