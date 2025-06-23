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
        recyclerView.setLayoutManager(new LinearLayoutManager(getActivity()));
        updateUI();
        return view;
    }

    private void updateUI() {
        List<Response> rsp = new ArrayList<>();
        Response r = new Response();
        r.setKey("0");
        r.setValue("0");
        r.setDisplayName("DacSettings");
        rsp.add(r);
        adapter = new DataAdapter(rsp);
        recyclerView.setAdapter(adapter);
    }
}
