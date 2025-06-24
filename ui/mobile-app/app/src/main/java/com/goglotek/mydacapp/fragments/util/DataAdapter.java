package com.goglotek.mydacapp.fragments.util;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.recyclerview.widget.RecyclerView;

import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.menu.DataRow;

import java.util.List;

public class DataAdapter extends RecyclerView.Adapter<DataHolder> {
    private List<DataRow> rowList;
    private OnItemClickListener listener;

    public interface OnItemClickListener {
        void onItemClick(DataRow row);
    }

    public DataAdapter(List<DataRow> rowList, OnItemClickListener listener) {
        this.rowList = rowList;
        this.listener = listener;
    }

    @Override
    public DataHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View view = inflater.inflate(R.layout.list_item_data, parent, false);
        return new DataHolder(view);
    }

    @Override
    public void onBindViewHolder(DataHolder holder, int position) {
        DataRow r = rowList.get(position);
        r.setIndex(position);
        holder.bind(r, listener);
    }


    @Override
    public int getItemCount() {
        return rowList.size();
    }

    public void setResponseDataList(List<DataRow> responseDataList) {
        this.rowList = responseDataList;
    }
}
