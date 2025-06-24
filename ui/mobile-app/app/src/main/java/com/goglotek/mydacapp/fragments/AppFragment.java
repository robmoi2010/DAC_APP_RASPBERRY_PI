package com.goglotek.mydacapp.fragments;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import androidx.activity.OnBackPressedCallback;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.fragments.util.DataAdapter;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.menu.Menu;
import com.goglotek.mydacapp.menu.MenuUtil;
import com.goglotek.mydacapp.models.Response;

import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.List;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class AppFragment extends Fragment {
    private RecyclerView recyclerView;
    private DataAdapter adapter;
    private Menu currentMenu;
    private Menu systemMenu;

    @Override
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle bundle) {
        View view = inflater.inflate(R.layout.app, container, false);
        recyclerView = view.findViewById(R.id.data_view_recycler);
        recyclerView.setLayoutManager(new LinearLayoutManager(requireContext()));
        updateUI();

        return view;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
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
            currentMenu = MenuUtil.menuStack.pop();
            updateUI();
        } catch (EmptyStackException e) {

        }
    }

    private void updateUI() {
        if (systemMenu == null) {
            systemMenu = MenuUtil.createSettingsMenu();
            currentMenu = systemMenu;
        }
        if (currentMenu.getRows().isEmpty()) {
            currentMenu.setRows(MenuUtil.loadDynamicData(currentMenu));
        }
        adapter = new DataAdapter(currentMenu.getRows(), (row) -> {
            handleRowOnclick(row);
        });
        recyclerView.setAdapter(adapter);
    }

    private void handleRowOnclick(DataRow row) {
        MenuUtil.menuStack.push(currentMenu);
        currentMenu = row.getNext();
        updateUI();
    }
}
