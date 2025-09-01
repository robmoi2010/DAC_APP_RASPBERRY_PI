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

package com.goglotek.mydacapp.models;

public class WebClient {

  private String getURL;
  private String postURL;
  private String putURL;
  private WebClientType clientType;

  private WebClient(String getURL, String postURL, String putURL, WebClientType clientType) {
    this.getURL = getURL;
    this.postURL = postURL;
    this.putURL = putURL;
    this.clientType = clientType;
  }

  private WebClient() {

  }

  public static WebClient getInstance() {
    return new WebClient();
  }

  public static WebClient getInstance(String getURL, String postURL, String putURL,
      WebClientType clientType) {
    return new WebClient(getURL, postURL, putURL, clientType);
  }

  public String getGetURL() {
    return getURL;
  }

  public void setGetURL(String getURL) {
    this.getURL = getURL;
  }

  public String getPostURL() {
    return postURL;
  }

  public void setPostURL(String postURL) {
    this.postURL = postURL;
  }

  public String getPutURL() {
    return putURL;
  }

  public void setPutURL(String putURL) {
    this.putURL = putURL;
  }

  public WebClientType getClientType() {
    return clientType;
  }

  public void setClientType(WebClientType clientType) {
    this.clientType = clientType;
  }
}
