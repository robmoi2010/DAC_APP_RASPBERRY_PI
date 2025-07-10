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
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import androidx.viewpager2.widget.ViewPager2;

import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.fragments.util.DataAdapter;
import com.goglotek.mydacapp.fragments.util.ViewPagerAdapter;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.menu.Menu;
import com.goglotek.mydacapp.menu.MenuDataType;
import com.goglotek.mydacapp.menu.MenuUtil;
import com.google.android.material.tabs.TabLayout;
import com.google.android.material.tabs.TabLayoutMediator;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import timber.log.Timber;

public class MenuFragment extends Fragment {
    private RecyclerView recyclerView;
    private DataAdapter adapter;
    private TextView header;
    private Menu menu;
    private ViewPagerAdapter pagerAdapter;
    private ViewPager2 viewPager;
    private TabLayout tabLayout;
    private boolean initDataLoaded = false;
    private ProgressBar progressBar;
    private FrameLayout overlay;

    public MenuFragment() {

    }

    private MenuFragment(Menu menu) {
        this.menu = menu;
    }

    public static MenuFragment newInstance(Menu menu) {
        MenuFragment frag = new MenuFragment(menu);
        Bundle bundle = new Bundle();
        bundle.putSerializable("menu", menu);
        frag.setArguments(bundle);
        return frag;
    }

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        super.onCreateView(inflater, container, savedInstanceState);
        menu = (Menu) getArguments().getSerializable("menu");
        LinearLayout layout = new LinearLayout(requireContext());
        layout.setOrientation(LinearLayout.VERTICAL);

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
        overlay.setClickable(true);
        overlay.addView(progressBar);
        overlay.setVisibility(View.GONE);

        layout.addView(tabLayout, new LinearLayout.LayoutParams(MATCH_PARENT, WRAP_CONTENT));
        layout.addView(viewPager, new LinearLayout.LayoutParams(MATCH_PARENT, 0, 1f));
        layout.addView(overlay);

        if (menu.getDataType() == MenuDataType.DYNAMIC) {
            View view = inflater.inflate(R.layout.app, container, false);
            recyclerView = new RecyclerView(requireContext());
            recyclerView.setLayoutManager(new LinearLayoutManager(requireContext()));
            header = view.findViewById(R.id.header_title);
            return recyclerView;
        }
        return layout;
    }

    @Override
    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        menu = (Menu) getArguments().getSerializable("menu");
        if (menu.getDataType() == MenuDataType.DYNAMIC) {
            adapter = new DataAdapter(new ArrayList<>(), (row) ->
                    handleRowOnclick(row)
                    , (isChecked, row) -> handleSwitchChange(isChecked, row), (current, row) -> handleSliderChange(current, row));
            recyclerView.setAdapter(adapter);
            overlay.setVisibility(View.VISIBLE);
            loadData();
            overlay.setVisibility(View.GONE);
            initDataLoaded = true;
        } else {
            pagerAdapter = new ViewPagerAdapter(this, menu);
            viewPager.registerOnPageChangeCallback(
                    new ViewPager2.OnPageChangeCallback() {
                        @Override
                        public void onPageSelected(int position) {
                            MenuFragment frag = pagerAdapter.getFragment(position);
                            if (frag != null) {
                                if (frag.menu.getDataType() == MenuDataType.DYNAMIC) {
                                    if (!initDataLoaded) {
                                        overlay.setVisibility(View.VISIBLE);
                                        frag.loadData();
                                        overlay.setVisibility(View.GONE);
                                    }
                                }
                            }
                        }
                    }
            );
            viewPager.setAdapter(pagerAdapter);
            new TabLayoutMediator(tabLayout, viewPager, (tab, position) -> {
                tab.setText(menu.getRows().get(position).getText());
            }).attach();
        }
    }

    private void loadData() {

        ExecutorService service = Executors.newSingleThreadExecutor();
        service.execute(() -> {
            try {
                final List<DataRow> rows = MenuUtil.getDataProcessor(menu.getRoot()).loadData();
                try {
                    requireActivity().runOnUiThread(() -> {
                        menu.setRows(rows);
                        updateAdapter();
                    });
                } catch (Exception e) {
                    Timber.e(e, e.getMessage());
                }
            } catch (GoglotekException e) {
                Timber.e(e, e.getMessage());
            }
        });
    }

    private void updateAdapter() {

        adapter.updateItems(menu.getRows());
        header.setText(menu.getRoot() != null ? menu.getRoot().getText() : "Settings");
    }

    private void handleRowOnclick(DataRow row) {
        updateServerData(row);
    }

    private void handleSliderChange(int current, DataRow row) {
        updateServerData(current, false, false);
    }

    private void handleSwitchChange(boolean isChecked, DataRow row) {
        updateServerData(row.getIndex(), true, isChecked);
    }

    private void updateServerData(DataRow row) {
        updateServerData(row.getIndex(), false, false);
    }

    private void updateServerData(int index, boolean isSwitch, boolean checked) {
        ExecutorService executorService = Executors.newSingleThreadExecutor();
        executorService.execute(() -> {
            int localIndex = index;
            List<DataRow> dt = new ArrayList<>();
            try {
                if (isSwitch) {
                    if (checked) {
                        localIndex = 1;
                    } else {
                        localIndex = 0;
                    }
                }
                dt = MenuUtil.getDataProcessor(menu.getRoot()).updateServerData(localIndex);
            } catch (GoglotekException e) {
                Timber.e(e, e.getMessage());
            }
            final List<DataRow> finalList = dt;
            requireActivity().runOnUiThread(() -> {
                menu.setRows(finalList);
                updateAdapter();
            });
        });
    }
}
