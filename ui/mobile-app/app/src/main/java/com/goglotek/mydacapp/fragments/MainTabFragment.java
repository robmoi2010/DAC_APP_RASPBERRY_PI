package com.goglotek.mydacapp.fragments;

import static android.view.ViewGroup.LayoutParams.MATCH_PARENT;
import static android.view.ViewGroup.LayoutParams.WRAP_CONTENT;

import android.graphics.Color;
import android.os.Bundle;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.ProgressBar;

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

import java.io.Serializable;
import java.util.EmptyStackException;

public class MainTabFragment extends Fragment {
    public interface OverlayController extends Serializable {
        void showOverlay();

        void hideOverlay();
    }

    ViewPagerAdapter pagerAdapter;
    ViewPager2 viewPager;
    TabLayout tabLayout;
    ProgressBar progressBar;
    private FrameLayout overlay;

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
        progressBar = new ProgressBar(requireContext());
        FrameLayout.LayoutParams progressParams = new FrameLayout.LayoutParams(
                ViewGroup.LayoutParams.WRAP_CONTENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        );
        progressParams.gravity = Gravity.CENTER;
        progressBar.setLayoutParams(progressParams);
        progressBar.setVisibility(View.VISIBLE);


        // Overlay with ProgressBar (spinner)
        overlay = new FrameLayout(requireContext());
        overlay.setLayoutParams(new FrameLayout.LayoutParams(
                FrameLayout.LayoutParams.MATCH_PARENT,
                FrameLayout.LayoutParams.MATCH_PARENT
        ));
        overlay.setBackgroundColor(Color.parseColor("#88FFFFFF"));
        overlay.setClickable(true); // block touches below
        overlay.addView(progressBar);
        ((ViewGroup) view).addView(tabLayout, new LinearLayout.LayoutParams(MATCH_PARENT, WRAP_CONTENT));
        ((ViewGroup) view).addView(viewPager, new LinearLayout.LayoutParams(MATCH_PARENT, 0, 1f));
        ((ViewGroup) view).addView(overlay);
        return view;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        Menu menu = MenuUtil.createAppMenus();
        pagerAdapter = new ViewPagerAdapter(this, menu, new OverlayController() {

            @Override
            public void showOverlay() {
                overlay.setVisibility(View.VISIBLE);
                System.out.println("visible");
            }

            @Override
            public void hideOverlay() {
                overlay.setVisibility(View.GONE);
                System.out.println("invisible");
            }
        });
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
            e.printStackTrace();
        }
    }
}
