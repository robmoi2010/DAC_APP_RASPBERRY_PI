package com.goglotek.mydacapp.fragments.util;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.recyclerview.widget.RecyclerView;

import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.models.Response;

import java.util.List;

public class DataAdapter extends RecyclerView.Adapter<DataHolder> {
    private List<Response> responseDataList;

    public DataAdapter(List<Response> responseDataList) {
        this.responseDataList = responseDataList;
    }

    @Override
    public DataHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View view = inflater.inflate(R.layout.list_item_data, parent, false);
        return new DataHolder(view);
    }

    @Override
    public void onBindViewHolder(DataHolder holder, int position) {
        Response r = responseDataList.get(position);
        holder.row.setText(r.getDisplayName());
    }

    @Override
    public int getItemCount() {
        return responseDataList.size();
    }

    public void setResponseDataList(List<Response> responseDataList) {
        this.responseDataList = responseDataList;
    }
}
