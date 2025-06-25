package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.service.DacService;
import com.goglotek.mydacapp.service.DspService;

import java.util.Collections;
import java.util.List;

public class DspInputProcessor implements DynamicDataProcessor {

    private static DspInputProcessor loader;

    private DspInputProcessor() {

    }

    @Override
    public List<DataRow> loadData() throws GoglotekException {
        String data = DspService.getInputOptions();
        return processServerData(data);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = DspService.updateInput(data);
        return processServerData(response);
    }

    public static DspInputProcessor getInstance() {
        if (loader == null) {
            loader = new DspInputProcessor();
        }
        return loader;
    }
}
