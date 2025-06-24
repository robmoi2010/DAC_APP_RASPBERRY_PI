package com.goglotek.mydacapp.menu;

import com.goglotek.mydacapp.models.Response;

import java.util.List;

public interface Menu {
    public List<DataRow> getRows();

    public void setRows(List<DataRow> rows);

    public void addRow(DataRow row);

}
