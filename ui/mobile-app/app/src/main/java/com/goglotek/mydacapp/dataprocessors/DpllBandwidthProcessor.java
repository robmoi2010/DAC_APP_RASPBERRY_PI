package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.menu.RowDataType;
import com.goglotek.mydacapp.service.DacService;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DpllBandwidthProcessor implements DynamicDataProcessor {
    private static DpllBandwidthProcessor loader;
    private List<Map<String, String>> options;

    private DpllBandwidthProcessor() {
        options = new ArrayList<>();
        Map<String, String> min = new HashMap<>();
        min.put("MIN", "1");
        Map<String, String> max = new HashMap<>();
        max.put("MAX", "15");
        Map<String, String> step = new HashMap<>();
        step.put("STEP", "1");
        options.add(min);
        options.add(max);
        options.add(step);

    }

    @Override
    public List<DataRow> loadData() throws GoglotekException {
        String data = DacService.getDpllBandwidth();
        return processServerData(data, RowDataType.NUMBER, options);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = DacService.updateDpllBandwidth(data);
        return processServerData(response, RowDataType.NUMBER, options);
    }

    public static DpllBandwidthProcessor getInstance() {
        if (loader == null) {
            loader = new DpllBandwidthProcessor();
        }
        return loader;
    }
}
