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

package com.goglotek.mydacapp.fragments.util;

import android.util.SparseArray;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.viewpager2.adapter.FragmentStateAdapter;
import com.goglotek.mydacapp.fragments.MenuFragment;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.menu.Menu;
import timber.log.Timber;

public class ViewPagerAdapter extends FragmentStateAdapter {

  private Menu menu;
  private SparseArray<MenuFragment> fragments = new SparseArray<>();

  public ViewPagerAdapter(@NonNull Fragment fragment, Menu menu) {
    super(fragment);
    this.menu = menu;
  }

  @NonNull
  @Override
  public Fragment createFragment(int position) {
    try {
      DataRow row = menu.getRows().get(position);
      MenuFragment fragment = MenuFragment.newInstance(row.getNext());
      fragments.put(position, fragment);
      return fragment;
      //} else {
      // MenuFragment fragment = MenuFragment.newInstance(menu);
      //  fragments.put(position, fragment);
      // return fragment;
      // }

//        if (menu.getDataType() == MenuDataType.STATIC) {
//            DisplayFragment fragment = DisplayFragment.newInstance(row.getNext());
//            fragments.put(position, fragment);
//            return fragment;
//        } else {
//            DisplayFragment fragment = DisplayFragment.newInstance(menu);
//            fragments.put(position, fragment);
//            return fragment;
//        }
    } catch (Exception e) {
      Timber.e(e, e.getMessage());
    }
    return null;
  }

  public MenuFragment getFragment(int pos) {
    return fragments.get(pos);
  }

  @Override
  public int getItemCount() {
    return this.menu.getRows().size();
  }
}
