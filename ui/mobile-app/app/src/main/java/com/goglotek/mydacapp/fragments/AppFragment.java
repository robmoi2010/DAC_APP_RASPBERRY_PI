package com.goglotek.mydacapp.fragments;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.fragments.util.DataAdapter;
import com.goglotek.mydacapp.models.Response;

import java.util.ArrayList;
import java.util.List;

public class AppFragment extends Fragment {
    private RecyclerView recyclerView;
    private DataAdapter adapter;

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

    private void updateUI() {

        adapter = new DataAdapter(getList());
        recyclerView.setAdapter(adapter);
    }

    private List<Response> getList() {
        List<Response> l = new ArrayList<>();
        for (int i = 0; i < 50; i++) {
            Response r = new Response("" + i, "" + i, "item " + i);
            l.add(r);
        }
        return l;
    }
}
