package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.service.DacService;

import java.util.Collections;
import java.util.List;

public class SecondOrderProcessor implements DynamicDataProcessor {
    private static SecondOrderProcessor loader;

    private SecondOrderProcessor() {

    }

    @Override
    public List<DataRow> loadData() throws GoglotekException {
        String data = DacService.getSecondOrderStatus();
        return processServerToggleData(data);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = DacService.updateSecondOrderStatus(data);
        return processServerToggleData(response);
    }

    public static SecondOrderProcessor getInstance() {
        if (loader == null) {
            loader = new SecondOrderProcessor();
        }
        return loader;
    }
}
