package com.goglotek.mydacapp.dataprocessors;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.menu.MenuRow;
import com.goglotek.mydacapp.menu.MenuUtil;
import com.goglotek.mydacapp.menu.RowDataType;
import com.goglotek.mydacapp.models.Response;
import com.goglotek.mydacapp.models.WebClient;
import com.goglotek.mydacapp.util.Config;
import com.goglotek.mydacapp.util.RestClient;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class GenericDataProcessor {
    static String BASE_URL = Config.getConfig("BASE_URL");
    private WebClient webClient;
    private List<Map<String, String>> options;

    private GenericDataProcessor(WebClient webClient) {
        this.webClient = webClient;
    }

    private GenericDataProcessor(WebClient webClient, List<Map<String, String>> options) {
        this.webClient = webClient;
        this.options = options;
    }

    private GenericDataProcessor() {

    }

    public static GenericDataProcessor getInstance() {
        return new GenericDataProcessor();
    }

    public static GenericDataProcessor getInstance(WebClient webClient) {
        return new GenericDataProcessor(webClient);
    }

    public static GenericDataProcessor getInstance(WebClient webClient, List<Map<String, String>> options) {
        return new GenericDataProcessor(webClient, options);
    }

    public Response sendGet() throws GoglotekException {
        try {
            String data = get();
            return new ObjectMapper().readValue(data, Response.class);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public Response[] sendGetArrayResponse() throws GoglotekException {
        try {
            String data = get();
            return new ObjectMapper().readValue(data, Response[].class);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    private String get() throws GoglotekException {
        try {
            return RestClient.getInstance().get(BASE_URL + webClient.getGetURL());
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    private String put(String payload) throws GoglotekException {
        try {
            return RestClient.getInstance().put(BASE_URL + webClient.getPutURL(), payload);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public Response sendPut(String payload) throws GoglotekException {
        try {
            String data = put(payload);
            return new ObjectMapper().readValue(data, Response.class);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public Response[] sendPutArrayResponse(String payload) throws GoglotekException {
        try {
            String data = put(payload);
            return new ObjectMapper().readValue(data, Response[].class);
        } catch (Exception e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }

    public List<DataRow> loadData() throws GoglotekException {
        return processServerData(get());
    }

    public List<DataRow> loadData(RowDataType type) throws GoglotekException {
        return processServerData(get(), type);
    }

    public List<DataRow> updateServer(int data) throws GoglotekException {
        String payload = generateResponseData(data);
        return processServerData(put(payload));
    }

    public List<DataRow> updateServer(int data, RowDataType type) throws GoglotekException {
        String payload = generateResponseData(data);
        return processServerData(put(payload), type);
    }


    private List<DataRow> processServerData(String data) throws GoglotekException {
        return processServerData(data, RowDataType.TEXT);
    }

    private List<DataRow> processServerData(String data, RowDataType type) throws GoglotekException {
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

                    if (this.options != null) {
                        row.setRowOptions(options);
                    }
                    row.setDescription(r.getDescription());
                    rows.add(row);
                }
            } catch (JsonProcessingException e) {
                throw new GoglotekException(e.getMessage(), e);
            }
        }
        return rows;
    }

    private String generateResponseData(int data) throws GoglotekException {
        Response r = new Response("" + data, "" + data, "");
        try {
            return new ObjectMapper().writeValueAsString(r);
        } catch (JsonProcessingException e) {
            throw new GoglotekException(e.getMessage(), e);
        }
    }


    public WebClient getWebClient() {
        return webClient;
    }

    public void setWebClient(WebClient webClient) {
        this.webClient = webClient;
    }
}
