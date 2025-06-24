package com.goglotek.mydacapp.menu;

import com.goglotek.mydacapp.models.Response;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class AppMenu implements Menu {
    private List<DataRow> rows = new ArrayList<>();

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

}
