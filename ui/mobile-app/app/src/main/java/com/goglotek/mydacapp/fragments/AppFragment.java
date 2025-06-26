package com.goglotek.mydacapp.fragments;

import android.app.Activity;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.ToggleButton;

import androidx.activity.OnBackPressedCallback;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.fragments.util.DataAdapter;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.menu.Menu;
import com.goglotek.mydacapp.menu.MenuDataType;
import com.goglotek.mydacapp.menu.MenuUtil;
import com.goglotek.mydacapp.models.Response;

import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class AppFragment extends Fragment {
    private RecyclerView recyclerView;
    private DataAdapter adapter;
    private Menu currentMenu;
    private TextView header;



    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle bundle) {
        View view = inflater.inflate(R.layout.app, container, false);
        recyclerView = view.findViewById(R.id.data_view_recycler);
        recyclerView.setLayoutManager(new LinearLayoutManager(requireContext()));
        adapter = new DataAdapter(new ArrayList<>(), (row) ->
                handleRowOnclick(row)
                , (isChecked, row) -> handleSwitchChange(isChecked, row));
        recyclerView.setAdapter(adapter);
        header = view.findViewById(R.id.header_title);
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
            if (MenuUtil.menuStack.empty()) {
                requireActivity().getSupportFragmentManager()
                        .beginTransaction()
                        .replace(R.id.fragment_container, new HomeFragment())
                        .addToBackStack(null)
                        .commit();
            } else {
                currentMenu = MenuUtil.menuStack.pop();
                updateUI();
            }
        } catch (EmptyStackException e) {
            e.printStackTrace();
        }
    }

    private void updateUI() {
        if (currentMenu == null) {
            currentMenu = MenuUtil.createAppMenus();
        }
        if (currentMenu.getDataType() == MenuDataType.DYNAMIC) {
            ExecutorService service = Executors.newSingleThreadExecutor();
            service.execute(() -> {
                try {
                    final List<DataRow> rows = MenuUtil.getDataProcessor(currentMenu.getRoot()).loadData();
                    ((Activity) getContext()).runOnUiThread(() -> {
                        currentMenu.setRows(rows);
                        updateAdapter();
                    });
                } catch (GoglotekException e) {
                    e.printStackTrace();
                }
            });
        } else {
            updateAdapter();
        }
    }

    private void updateAdapter() {
        adapter.updateItems(currentMenu.getRows());
        header.setText(currentMenu.getRoot() != null ? currentMenu.getRoot().getText() : "Settings");
    }

    private void handleRowOnclick(DataRow row) {
        if (currentMenu.getDataType() == MenuDataType.STATIC) {
            MenuUtil.menuStack.push(currentMenu);
            currentMenu = row.getNext();
            updateUI();
        } else {
            updateServerData(row);
        }
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
                dt = MenuUtil.getDataProcessor(currentMenu.getRoot()).updateServerData(localIndex);
            } catch (GoglotekException e) {
                e.printStackTrace();
            }
            final List<DataRow> finalList = dt;
            ((Activity) getContext()).runOnUiThread(() -> {
                currentMenu.setRows(finalList);
                updateUI();
            });
        });
    }

    private void handleSwitchChange(boolean isChecked, DataRow row) {
        System.out.println("Switched.." + isChecked);
        updateServerData(row.getIndex(), true, isChecked);
    }
}
