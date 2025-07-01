package com.goglotek.mydacapp.fragments;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.text.Layout;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.LinearLayout;
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
import com.goglotek.mydacapp.fragments.util.PagerAdapter;
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


public class DisplayFragment extends Fragment {
    private Menu menu;
    private boolean dataPopulated = false;
    private RecyclerView recyclerView;
    private DataAdapter adapter;
    private TextView header;
    private PagerAdapter pagerAdapter;


    private DisplayFragment() {
    }

    public static DisplayFragment newInstance(Menu menu) {
        DisplayFragment fragment = new DisplayFragment();
        Bundle bundle = new Bundle();
        bundle.putSerializable("menu", menu);
        fragment.setArguments(bundle);
        return fragment;
    }

    @Nullable
    @Override
    public View onCreateView(
            @NonNull LayoutInflater inflater,
            @Nullable ViewGroup container,
            @Nullable Bundle savedInstanceState
    ) {
        super.onCreateView(inflater, container, savedInstanceState);
        this.menu = (Menu) getArguments().getSerializable("menu");
        if (menu.getDataType() == MenuDataType.DYNAMIC) {
            View view = inflater.inflate(R.layout.app, container, false);
            recyclerView = view.findViewById(R.id.data_view_recycler);
            recyclerView.setLayoutManager(new LinearLayoutManager(requireContext()));
            adapter = new DataAdapter(new ArrayList<>(), (row) ->
                    handleRowOnclick(row)
                    , (isChecked, row) -> handleSwitchChange(isChecked, row));
            recyclerView.setAdapter(adapter);
            header = view.findViewById(R.id.header_title);
            //loadData();
            return recyclerView;
        } else {
            LinearLayout layout = new LinearLayout(getContext());
            layout.setLayoutParams(new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.MATCH_PARENT
            ));
            layout.setOrientation(LinearLayout.VERTICAL);
            pagerAdapter = new PagerAdapter(this, menu);
            ViewPager2 viewPager = new ViewPager2(getContext());
            viewPager.setLayoutParams(new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    0,
                    1f // Fills remaining space
            ));
            viewPager.registerOnPageChangeCallback(
                    new ViewPager2.OnPageChangeCallback() {
                        @Override
                        public void onPageSelected(int position) {
//                            DisplayFragment frag = pagerAdapter.getFragment(position);
//                            if (frag != null) {
//                                if (frag.menu.getDataType() == MenuDataType.DYNAMIC) {
//                                    frag.loadData();
//                                }
//                            }
                        }
                    }
            );
            viewPager.setAdapter(pagerAdapter);
            TabLayout tabLayout = new TabLayout(getContext());
            tabLayout.setLayoutParams(new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT
            ));

            new TabLayoutMediator(tabLayout, viewPager, (tab, position) -> {
                tab.setText(menu.getRows().get(position).getText());
            }).attach();
            layout.addView(tabLayout);
            layout.addView(viewPager);
            return layout;
        }
    }

    private void loadData() {
        System.out.println("loading data for " + menu.getRoot().getName());
        ExecutorService service = Executors.newSingleThreadExecutor();
        service.execute(() -> {
            try {
                final List<DataRow> rows = MenuUtil.getDataProcessor(menu.getRoot()).loadData();
                ((Activity) getContext()).runOnUiThread(() -> {
                    menu.setRows(rows);
                    updateAdapter();
                });
            } catch (GoglotekException e) {
                e.printStackTrace();
            }
        });
    }

    private void updateAdapter() {
        adapter.updateItems(menu.getRows());
        header.setText(menu.getRoot() != null ? menu.getRoot().getText() : "Settings");
    }

    private void handleRowOnclick(DataRow row) {

    }

    private void handleSwitchChange(boolean isChecked, DataRow row) {
        System.out.println("Switched.." + isChecked);
        //updateServerData(row.getIndex(), true, isChecked);
    }

}
