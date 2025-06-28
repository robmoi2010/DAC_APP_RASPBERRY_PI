package com.goglotek.mydacapp.util;

import java.util.HashMap;
import java.util.Map;

public class Config {
    private static Map<String, String> configs = new HashMap<String, String>();

    static {
        configs.put("BASE_URL", "http://10.0.2.2:8000/");
        configs.put("CURRENT_VOLUME_ID", "CURRENT_VOLUME");
    }

    public static String getConfig(String name) {
        return configs.get(name);
    }

}
