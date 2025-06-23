package com.goglotek.mydacapp.fragments.util;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import com.goglotek.mydacapp.R;

public class DataHolder extends RecyclerView.ViewHolder {
    public TextView row;

    public DataHolder(View view) {
        super(view);
        row = view.findViewById(R.id.list_item);
    }
}
