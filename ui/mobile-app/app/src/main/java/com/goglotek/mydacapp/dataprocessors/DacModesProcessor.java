package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.models.Response;
import com.goglotek.mydacapp.service.DacService;

import java.util.Collections;
import java.util.List;

public class DacModesProcessor implements DynamicDataProcessor {
    private static DacModesProcessor loader;

    private DacModesProcessor() {

    }

    @Override
    public List<DataRow> loadData() throws GoglotekException {
        String data = DacService.getDacModes();
        return processServerData(data);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = DacService.updateDacMode(data);
        return processServerData(response);
    }

    public static DynamicDataProcessor getInstance() {
        if (loader == null) {
            loader = new DacModesProcessor();
        }
        return loader;
    }
}
