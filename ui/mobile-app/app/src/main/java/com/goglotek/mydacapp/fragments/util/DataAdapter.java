/*
 * Copyright (C) 2025 Robert Moi, Goglotek LTD
 *
 *  This file is part of the DAC_APPLICATION System.
 *
 *  The DAC_APPLICATION System is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  The DAC_APPLICATION is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with the Fraud Detector System. If not, see <https://www.gnu.org/licenses/>
 */

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

  public DataAdapter(List<DataRow> rows, OnItemClickListener listener,
      onSwitchChangeListener switchListener, onSliderChangeListener sliderChangeListener) {
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
