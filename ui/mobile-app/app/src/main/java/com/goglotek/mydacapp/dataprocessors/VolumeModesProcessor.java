package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.service.DacService;

import java.util.Collections;
import java.util.List;

public class VolumeModesProcessor implements DynamicDataProcessor {
    private static VolumeModesProcessor loader;

    private VolumeModesProcessor() {

    }

    @Override
    public List<DataRow> loadData() throws GoglotekException {
        String data = DacService.getVolumeModes();
        return processServerData(data);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = DacService.updateVolumeModes(data);
        return processServerData(response);
    }

    public static VolumeModesProcessor getInstance() {
        if (loader == null) {
            loader = new VolumeModesProcessor();
        }
        return loader;
    }
}
