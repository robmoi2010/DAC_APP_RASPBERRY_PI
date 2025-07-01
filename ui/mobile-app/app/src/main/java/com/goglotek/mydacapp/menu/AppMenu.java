package com.goglotek.mydacapp.menu;

import android.os.Parcel;
import android.os.Parcelable;

import androidx.annotation.NonNull;

import java.util.ArrayList;
import java.util.List;

public class AppMenu implements Menu {
    private List<DataRow> rows ;
    private MenuDataType dataType;
    private DataRow root;

    @Override
    public List<DataRow> getRows() {
        return this.rows;
    }

    @Override
    public void setRows(List<DataRow> rows) {
        this.rows = rows;
    }

    @Override
    public void addRow(DataRow row) {
        rows.add(row);
    }

    @Override
    public MenuDataType getDataType() {
        return this.dataType;
    }

    @Override
    public void setDataType(MenuDataType dataType) {
        this.dataType = dataType;
    }

    @Override
    public DataRow getRoot() {
        return this.root;
    }

    @Override
    public void setRoot(DataRow root) {
        this.root = root;
    }


}
