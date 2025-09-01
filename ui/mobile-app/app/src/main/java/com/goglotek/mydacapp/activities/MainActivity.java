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
import android.view.MenuItem;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
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
