/*
 * Copyright (C) 2025 Robert Moi, Goglotek LTD
 *
 *  This file is part of the DAC_APPLICATION System.
 *
 *  The DAC_APPLICATION System is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  The DAC_APPLICATION is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with the Fraud Detector System. If not, see <https://www.gnu.org/licenses/>
 */

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
