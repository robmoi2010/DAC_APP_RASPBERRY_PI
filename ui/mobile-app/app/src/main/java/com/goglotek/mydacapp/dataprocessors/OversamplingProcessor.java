package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.menu.RowDataType;
import com.goglotek.mydacapp.service.DacService;

import java.util.Collections;
import java.util.List;

public class OversamplingProcessor implements DynamicDataProcessor {
    private static OversamplingProcessor loader;

    private OversamplingProcessor() {

    }

    @Override
    public List<DataRow> loadData() throws GoglotekException {
        String data = DacService.getOversamplingStatus();
        return processServerData(data, RowDataType.TOGGLE);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = DacService.updateOversamplingStatus(data);
        return processServerData(data, RowDataType.TOGGLE);
    }

    public static OversamplingProcessor getInstance() {
        if (loader == null) {
            loader = new OversamplingProcessor();
        }
        return loader;
    }
}
