/*
 * Copyright (C) 2025 Robert Moi, Goglotek LTD
 *
 *  This file is part of the DAC_APPLICATION System.
 *
 *  The DAC_APPLICATION System is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  The DAC_APPLICATION is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with the Fraud Detector System. If not, see <https://www.gnu.org/licenses/>
 */

package com.goglotek.mydacapp.dataprocessors;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.menu.MenuRow;
import com.goglotek.mydacapp.menu.MenuUtil;
import com.goglotek.mydacapp.menu.RowDataType;
import com.goglotek.mydacapp.models.Request;
import com.goglotek.mydacapp.models.Response;
import com.goglotek.mydacapp.models.WebClient;
import com.goglotek.mydacapp.util.Config;
import com.goglotek.mydacapp.util.RestClient;
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

  public static GenericDataProcessor getInstance(WebClient webClient,
      List<Map<String, String>> options) {
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
    String payload = generateRequestData(data);
    return processServerData(put(payload));
  }

  public List<DataRow> updateServer(int data, RowDataType type) throws GoglotekException {
    String payload = generateRequestData(data);
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

  private String generateRequestData(int data) throws GoglotekException {
    Request r = new Request("" + data, "" + data);
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
