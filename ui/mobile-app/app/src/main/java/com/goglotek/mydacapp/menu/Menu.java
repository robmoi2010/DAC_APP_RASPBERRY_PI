package com.goglotek.mydacapp.menu;

import java.util.List;

public interface Menu {
    public List<DataRow> getRows();

    public void setRows(List<DataRow> rows);

    public void addRow(DataRow row);

    public MenuDataType getDataType();

    public void setDataType(MenuDataType dataType);
    public DataRow getRoot();

    public void setRoot(DataRow root);

}
