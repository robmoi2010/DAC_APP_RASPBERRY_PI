package com.goglotek.mydacapp.fragments.util;

import androidx.recyclerview.widget.DiffUtil;

import com.goglotek.mydacapp.menu.DataRow;

import java.util.List;

public class DiffCallBack extends DiffUtil.Callback {
    private List<DataRow> oldList;
    private List<DataRow> newList;

    public DiffCallBack(List<DataRow> oldList, List<DataRow> newList) {
        this.oldList = oldList;
        this.newList = newList;
    }

    @Override
    public int getOldListSize() {
        return oldList.size();
    }

    @Override
    public int getNewListSize() {
        return newList.size();
    }

    @Override
    public boolean areItemsTheSame(int oldItemPosition, int newItemPosition) {
        DataRow oldItem = this.oldList.get(oldItemPosition);
        DataRow newItem = this.newList.get(newItemPosition);
        return sameItem(oldItem, newItem);
    }

    @Override
    public boolean areContentsTheSame(int oldItemPosition, int newItemPosition) {
        DataRow oldItem = this.oldList.get(oldItemPosition);
        DataRow newItem = this.newList.get(newItemPosition);
        return sameItem(oldItem, newItem);
    }

    private boolean sameItem(DataRow oldItem, DataRow newItem) {
        return oldItem.getText() == newItem.getText() && oldItem.getName() == newItem.getName() && oldItem.isSelected() == newItem.isSelected();
    }
}
