package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.service.DacService;
import com.goglotek.mydacapp.service.DspService;

import java.util.Collections;
import java.util.List;


public class DspMainOutputProcessor implements DynamicDataProcessor {
    private static DspMainOutputProcessor loader;

    private DspMainOutputProcessor() {

    }


    @Override
    public List<DataRow> loadData() throws GoglotekException {
        String data = DspService.getMainsOutputOptions();
        return processServerData(data);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = DspService.updateMainsOutput(data);
        return processServerData(response);
    }

    public static DspMainOutputProcessor getInstance() {
        if (loader == null) {
            loader = new DspMainOutputProcessor();
        }
        return loader;
    }
}
