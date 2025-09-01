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

package com.goglotek.mydacapp.fragments;

import static android.view.ViewGroup.LayoutParams.MATCH_PARENT;
import static android.view.ViewGroup.LayoutParams.WRAP_CONTENT;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.LinearLayout;
import androidx.activity.OnBackPressedCallback;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.viewpager2.widget.ViewPager2;
import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.fragments.util.ViewPagerAdapter;
import com.goglotek.mydacapp.menu.Menu;
import com.goglotek.mydacapp.menu.MenuUtil;
import com.google.android.material.tabs.TabLayout;
import com.google.android.material.tabs.TabLayoutMediator;
import java.util.EmptyStackException;
import timber.log.Timber;

public class MainTabFragment extends Fragment {

  ViewPagerAdapter pagerAdapter;
  ViewPager2 viewPager;
  TabLayout tabLayout;
  AlertDialog dialog;

  @Nullable
  @Override
  public View onCreateView(
      @NonNull LayoutInflater inflater,
      @Nullable ViewGroup container,
      @Nullable Bundle savedInstanceState
  ) {
    View view = inflater.inflate(R.layout.fragment_tabs, container, false);
    dialog = new AlertDialog.Builder(container.getContext()).create();
    tabLayout = new TabLayout(requireContext());
    tabLayout.setTabMode(TabLayout.MODE_SCROLLABLE);
    viewPager = new ViewPager2(requireContext());

    ((ViewGroup) view).addView(tabLayout,
        new LinearLayout.LayoutParams(MATCH_PARENT, WRAP_CONTENT));
    ((ViewGroup) view).addView(viewPager, new LinearLayout.LayoutParams(MATCH_PARENT, 0, 1f));
    return view;
  }

  @Override
  public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
    Menu menu = MenuUtil.createAppMenus();
    pagerAdapter = new ViewPagerAdapter(this, menu);
    viewPager.setAdapter(pagerAdapter);

    new TabLayoutMediator(tabLayout, viewPager, (tab, pos) -> {
      tab.setText(menu.getRows().get(pos).getText());
    }).attach();

    requireActivity().getOnBackPressedDispatcher().addCallback(getViewLifecycleOwner(),
        new OnBackPressedCallback(true) {
          @Override
          public void handleOnBackPressed() {
            handleBackButtonPress();
          }
        }
    );
  }

  private void handleBackButtonPress() {
    try {
      requireActivity().getSupportFragmentManager()
          .beginTransaction()
          .replace(R.id.fragment_container, new HomeFragment())
          .addToBackStack(null)
          .commit();

    } catch (EmptyStackException e) {
      dialog.setMessage(e.getMessage());
      dialog.show();
      Timber.e(e, e.getMessage());
    }
  }
}
