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

public interface DynamicDataProcessor {
    public List<DataRow> loadData() throws GoglotekException;

    public List<DataRow> updateServerData(int index) throws GoglotekException;

    default List<DataRow> processServerToggleData(String data) throws GoglotekException {
        List<DataRow> rows = new ArrayList<>();
        if (data != null) {
            try {
                Response rsp = new ObjectMapper().readValue(data, Response.class);
                DataRow row = new MenuRow();
                row.setType(RowDataType.TOGGLE);
                row.setSelected(Boolean.parseBoolean(rsp.getValue()));
                rows.add(row);

            } catch (JsonProcessingException e) {
                throw new GoglotekException(e.getMessage(), e);
            }
        }
        return rows;
    }

    default List<DataRow> processServerData(String data) throws GoglotekException {
        List<DataRow> rows = new ArrayList<>();
        if (data != null) {
            try {
                Response[] rspList = new ObjectMapper().readValue(data, Response[].class);
                for (Response r : rspList) {
                    DataRow row = new MenuRow();
                    row.setIndex(Integer.parseInt(r.getKey()));
                    row.setText(MenuUtil.textFromName(r.getDisplayName()));
                    row.setName(r.getDisplayName());
                    row.setSelected(r.getValue().equals("1"));
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
}

