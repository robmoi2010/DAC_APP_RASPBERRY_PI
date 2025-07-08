package com.goglotek.mydacapp.menu;

import android.os.Parcelable;

import java.io.Serializable;
import java.util.List;

public interface Menu extends Serializable {
    public List<DataRow> getRows();

    public void setRows(List<DataRow> rows);

    public void addRow(DataRow row);

    public MenuDataType getDataType();

    public void setDataType(MenuDataType dataType);

    public DataRow getRoot();

    public void setRoot(DataRow root);

}
