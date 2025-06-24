package com.goglotek.mydacapp.fragments.util;

import android.view.View;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.menu.DataRow;

public class DataHolder extends RecyclerView.ViewHolder {
    public TextView row;

    public DataHolder(View view) {
        super(view);
        row = view.findViewById(R.id.list_item);
    }

    public void bind(final DataRow dataRow, final DataAdapter.OnItemClickListener listener) {
        row.setText(dataRow.getName());
        itemView.setOnClickListener(v -> listener.onItemClick(dataRow));
    }
}
