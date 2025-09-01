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

package com.goglotek.mydacapp.util;

import java.util.HashMap;
import java.util.Map;

public class Config {

  private static Map<String, String> configs = new HashMap<String, String>();

  static {
    //configs.put("BASE_URL", "http://10.0.2.2:8000/");
    configs.put("BASE_URL", "http://192.168.137.1:8000/");
    configs.put("CURRENT_VOLUME_ID", "CURRENT_VOLUME");
  }

  public static String getConfig(String name) {
    return configs.get(name);
  }

}
