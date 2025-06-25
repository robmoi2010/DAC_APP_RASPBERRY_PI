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
    private Menu systemMenu;
    private TextView header;


    @Override
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle bundle) {
        View view = inflater.inflate(R.layout.app, container, false);
        recyclerView = view.findViewById(R.id.data_view_recycler);
        recyclerView.setLayoutManager(new LinearLayoutManager(requireContext()));
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
            requireActivity().getSupportFragmentManager().popBackStack();
        }
    }

    private void updateUI() {
        if (systemMenu == null) {
            systemMenu = MenuUtil.createAppMenus();
            currentMenu = systemMenu;
        }
        if (currentMenu.getDataType() == MenuDataType.DYNAMIC) {
            ExecutorService service = Executors.newSingleThreadExecutor();
            service.execute(() -> {
                try {
                    final List<DataRow> rows = MenuUtil.getDataProcessor(currentMenu.getRoot()).loadData();
                    ((Activity) getContext()).runOnUiThread(() -> {
                        currentMenu.setRows(rows);
                        adapter = new DataAdapter(getContext(), currentMenu.getRows(), (row) -> {
                            handleRowOnclick(row);
                        });
                        recyclerView.setAdapter(adapter);
                        header.setText(currentMenu.getRoot() != null ? currentMenu.getRoot().getText() : "Settings");
                    });
                } catch (GoglotekException e) {
                    e.printStackTrace();
                }
            });
        } else {
            adapter = new DataAdapter(getContext(), currentMenu.getRows(), (row) -> {
                handleRowOnclick(row);
            });
            recyclerView.setAdapter(adapter);
            header.setText(currentMenu.getRoot() != null ? currentMenu.getRoot().getText() : "Settings");
        }

    }

    private void handleRowOnclick(DataRow row) {
        if (currentMenu.getDataType() == MenuDataType.STATIC) {
            MenuUtil.menuStack.push(currentMenu);
            currentMenu = row.getNext();
        } else {
            ExecutorService executorService = Executors.newSingleThreadExecutor();
            executorService.execute(() -> {
                try {
                    Menu m = currentMenu;
                    m.setRows(MenuUtil.getDataProcessor(currentMenu.getRoot()).updateServerData(row.getIndex()));
                    currentMenu = m;
                } catch (GoglotekException e) {
                    e.printStackTrace();
                }
            });
        }

        updateUI();
    }
}
