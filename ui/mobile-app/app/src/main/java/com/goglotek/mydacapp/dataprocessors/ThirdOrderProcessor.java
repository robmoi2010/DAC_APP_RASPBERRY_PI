package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.service.DacService;

import java.util.Collections;
import java.util.List;

public class ThirdOrderProcessor implements DynamicDataProcessor {
    private static ThirdOrderProcessor loader;

    private ThirdOrderProcessor() {

    }

    @Override
    public List<DataRow> loadData() throws GoglotekException {
        String data = DacService.getThirdOrderStatus();
        return processServerToggleData(data);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = DacService.updateThirdOrderStatus(data);
        return processServerToggleData(response);
    }

    public static ThirdOrderProcessor getInstance() {
        if (loader == null) {
            loader = new ThirdOrderProcessor();
        }
        return loader;
    }
}
