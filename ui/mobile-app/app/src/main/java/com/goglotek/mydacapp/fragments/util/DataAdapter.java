package com.goglotek.mydacapp.fragments.util;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.recyclerview.widget.DiffUtil;
import androidx.recyclerview.widget.RecyclerView;

import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.menu.DataRow;

import java.util.List;

public class DataAdapter extends RecyclerView.Adapter<DataHolder> {
    private OnItemClickListener listener;
    private onSwitchChangeListener switchChangeListener;
    private onSliderChangeListener sliderChangeListener;
    private List<DataRow> rows;

    public interface OnItemClickListener {
        void onItemClick(DataRow row);
    }

    public interface onSwitchChangeListener {
        public void handleSwitchChange(boolean isChecked, DataRow row);
    }

    public interface onSliderChangeListener {
        public void handleSliderChange(int current, DataRow row);
    }

    public DataAdapter(List<DataRow> rows, OnItemClickListener listener, onSwitchChangeListener switchListener, onSliderChangeListener sliderChangeListener) {
        super();
        this.listener = listener;
        this.rows = rows;
        this.switchChangeListener = switchListener;
        this.sliderChangeListener = sliderChangeListener;
    }

    @Override
    public DataHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View view = inflater.inflate(R.layout.list_item_data, parent, false);
        return new DataHolder(view, this.switchChangeListener, this.sliderChangeListener);
    }

    @Override
    public int getItemCount() {
        return rows.size();
    }

    @Override
    public void onBindViewHolder(DataHolder holder, int position) {
        DataRow r = rows.get(position);
        holder.itemView.setVisibility(View.VISIBLE);
        holder.bind(r, listener);
    }

    public void updateItems(List<DataRow> data) {
        DiffCallBack callBack = new DiffCallBack(this.rows, data);
        DiffUtil.DiffResult results = DiffUtil.calculateDiff(callBack);
        this.rows.clear();
        this.rows.addAll(data);
        results.dispatchUpdatesTo(this);
    }
}
