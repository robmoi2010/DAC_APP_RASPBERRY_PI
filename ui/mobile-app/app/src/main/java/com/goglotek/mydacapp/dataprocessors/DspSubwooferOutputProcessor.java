package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.service.DacService;
import com.goglotek.mydacapp.service.DspService;

import java.util.Collections;
import java.util.List;

public class DspSubwooferOutputProcessor implements DynamicDataProcessor {
    private static DspSubwooferOutputProcessor loader;

    private DspSubwooferOutputProcessor() {

    }

    @Override
    public List<DataRow> loadData() throws GoglotekException {
        String data = DspService.getSubwooferOutputOptions();
        return processServerData(data);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = DspService.updateSubwooferOutput(data);
        return processServerData(response);
    }

    public static DspSubwooferOutputProcessor getInstance() {
        if (loader == null) {
            loader = new DspSubwooferOutputProcessor();
        }
        return loader;
    }
}
