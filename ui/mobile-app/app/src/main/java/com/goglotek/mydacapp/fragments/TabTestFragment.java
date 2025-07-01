package com.goglotek.mydacapp.fragments;

import static android.view.ViewGroup.LayoutParams.MATCH_PARENT;
import static android.view.ViewGroup.LayoutParams.WRAP_CONTENT;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.LinearLayout;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.viewpager2.widget.ViewPager2;

import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.fragments.util.PagerAdapter;
import com.goglotek.mydacapp.menu.Menu;
import com.goglotek.mydacapp.menu.MenuUtil;
import com.google.android.material.tabs.TabLayout;
import com.google.android.material.tabs.TabLayoutMediator;

public class TabTestFragment extends Fragment {
    PagerAdapter pagerAdapter;
    ViewPager2 viewPager;
    TabLayout tabLayout;

    @Nullable
    @Override
    public View onCreateView(
            @NonNull LayoutInflater inflater,
            @Nullable ViewGroup container,
            @Nullable Bundle savedInstanceState
    ) {
        View view = inflater.inflate(R.layout.fragment_tabs, container, false);
        tabLayout = new TabLayout(requireContext());
        tabLayout.setTabMode(TabLayout.MODE_SCROLLABLE);
        viewPager = new ViewPager2(requireContext());

        ((ViewGroup) view).addView(tabLayout, new LinearLayout.LayoutParams(MATCH_PARENT, WRAP_CONTENT));
        ((ViewGroup) view).addView(viewPager, new LinearLayout.LayoutParams(MATCH_PARENT, 0, 1f));
        return view;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        Menu menu = MenuUtil.createAppMenus();
        pagerAdapter = new PagerAdapter(this, menu);
        viewPager.setAdapter(pagerAdapter);

        new TabLayoutMediator(tabLayout, viewPager, (tab, pos) -> {
            tab.setText(menu.getRows().get(pos).getText());
        }).attach();
    }
}
