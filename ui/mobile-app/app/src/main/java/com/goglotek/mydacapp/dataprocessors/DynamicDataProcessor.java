package com.goglotek.mydacapp.dataprocessors;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.menu.MenuRow;
import com.goglotek.mydacapp.menu.MenuUtil;
import com.goglotek.mydacapp.menu.RowDataType;
import com.goglotek.mydacapp.models.Response;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public interface DynamicDataProcessor {
    public List<DataRow> loadData() throws GoglotekException;

    public List<DataRow> updateServerData(int index) throws GoglotekException;

    default List<DataRow> processServerData(String data) throws GoglotekException {
        return processServerData(data, RowDataType.TEXT, null);
    }

    default List<DataRow> processServerData(String data, RowDataType type) throws GoglotekException {
        return processServerData(data, type, null);
    }

    default List<DataRow> processServerData(String data, RowDataType type, List<Map<String, String>> rowOptions) throws GoglotekException {
        List<DataRow> rows = new ArrayList<>();
        if (data != null) {
            try {
                Response[] rspList;
                if (type == RowDataType.TEXT) {
                    rspList = new ObjectMapper().readValue(data, Response[].class);
                } else {
                    rspList = new Response[1];
                    Response r = new ObjectMapper().readValue(data, Response.class);
                    rspList[0] = (r);
                }
                for (Response r : rspList) {
                    DataRow row = new MenuRow();
                    row.setType(type);
                    row.setIndex(Integer.parseInt(r.getKey()));
                    row.setName(r.getDisplayName());
                    if (type == RowDataType.NUMBER) {
                        row.setText(r.getValue());
                    } else {
                        row.setSelected(r.getValue().equals("1"));
                        row.setText(MenuUtil.textFromName(r.getDisplayName()));
                    }

                    if (rowOptions != null) {
                        row.setRowOptions(rowOptions);
                    }
                    rows.add(row);
                }
            } catch (JsonProcessingException e) {
                throw new GoglotekException(e.getMessage(), e);
            }
        }
        return rows;
    }

    default String generateResponseData(int index) throws GoglotekException {
        Response r = new Response("" + index, "" + index, "");
        try {
            return new ObjectMapper().writeValueAsString(r);
        } catch (JsonProcessingException e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    default List<DataRow> dummyData() {
        List<DataRow> rows = new ArrayList<>();
        for (int i = 0; i < 100; i++) {
            DataRow row = new MenuRow();
            row.setIndex(i);
            row.setText("Data " + i);
            row.setName("Data " + i);
            row.setSelected(false);
            rows.add(row);
        }
        DataRow row = new MenuRow();
        row.setIndex(100);
        row.setText("Data " + 100);
        row.setName("Data " + 100);
        row.setSelected(true);
        rows.add(row);
        return rows;
    }
}

