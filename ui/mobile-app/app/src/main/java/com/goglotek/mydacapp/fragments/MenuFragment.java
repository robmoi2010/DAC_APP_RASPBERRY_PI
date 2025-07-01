package com.goglotek.mydacapp.fragments;

import static android.view.ViewGroup.LayoutParams.MATCH_PARENT;
import static android.view.ViewGroup.LayoutParams.WRAP_CONTENT;

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

public class MenuFragment extends Fragment {
    private RecyclerView recyclerView;
    private DataAdapter adapter;
    private TextView header;
    private Menu menu;
    PagerAdapter pagerAdapter;
    ViewPager2 viewPager;
    private TabLayout tabLayout;
    
    public static MenuFragment newInstance(Menu menu) {
        MenuFragment frag = new MenuFragment();
        Bundle bundle = new Bundle();
        bundle.putSerializable("menu", menu);
        frag.setArguments(bundle);
        return frag;
    }

    @Override
    public View onCreateView(
            @NonNull LayoutInflater inflater,
            @Nullable ViewGroup container,
            @Nullable Bundle savedInstanceState
    ) {
        super.onCreateView(inflater, container, savedInstanceState);
        menu = (Menu) getArguments().getSerializable("menu");
        LinearLayout layout = new LinearLayout(requireContext());
        layout.setOrientation(LinearLayout.VERTICAL);

        tabLayout = new TabLayout(requireContext());
        tabLayout.setTabMode(TabLayout.MODE_SCROLLABLE);
        viewPager = new ViewPager2(requireContext());

        layout.addView(tabLayout, new LinearLayout.LayoutParams(MATCH_PARENT, WRAP_CONTENT));
        layout.addView(viewPager, new LinearLayout.LayoutParams(MATCH_PARENT, 0, 1f));
        if (menu.getDataType() == MenuDataType.DYNAMIC) {
            View view = inflater.inflate(R.layout.app, container, false);
            recyclerView = view.findViewById(R.id.data_view_recycler);
            recyclerView.setLayoutManager(new LinearLayoutManager(requireContext()));
            header = view.findViewById(R.id.header_title);
            return recyclerView;
        }

        return layout;
    }

    @Override
    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        if (menu.getDataType() == MenuDataType.DYNAMIC) {
            adapter = new DataAdapter(new ArrayList<>(), (row) ->
                    handleRowOnclick(row)
                    , (isChecked, row) -> handleSwitchChange(isChecked, row));
            recyclerView.setAdapter(adapter);
        } else {
            pagerAdapter = new PagerAdapter(this, menu);
            viewPager.registerOnPageChangeCallback(
                    new ViewPager2.OnPageChangeCallback() {
                        @Override
                        public void onPageSelected(int position) {
                            MenuFragment frag = pagerAdapter.getFragment(position);
                            if (frag != null) {
                                if (frag.menu.getDataType() == MenuDataType.DYNAMIC) {
                                    frag.loadData();
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
        System.out.println("loading data for " + menu.getRoot().getName());
        ExecutorService service = Executors.newSingleThreadExecutor();
        service.execute(() -> {
            try {
                final List<DataRow> rows = MenuUtil.getDataProcessor(menu.getRoot()).loadData();
                requireActivity().runOnUiThread(() -> {
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
