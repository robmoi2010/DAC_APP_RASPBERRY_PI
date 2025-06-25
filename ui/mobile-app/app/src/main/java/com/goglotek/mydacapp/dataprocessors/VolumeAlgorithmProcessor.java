package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.service.DacService;
import com.goglotek.mydacapp.service.SystemService;

import java.util.List;

public class VolumeAlgorithmProcessor implements DynamicDataProcessor {
    private static VolumeAlgorithmProcessor loader;

    private VolumeAlgorithmProcessor() {

    }

    @Override
    public List<DataRow> loadData() throws GoglotekException {
        String data = SystemService.getVolumeAlgorithm();
        return processServerData(data);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = SystemService.updateVolumeAlgorithm(data);
        return processServerData(response);
    }

    public static VolumeAlgorithmProcessor getInstance() {
        if (loader == null) {
            loader = new VolumeAlgorithmProcessor();
        }
        return loader;
    }

    public static interface ServerUpdater {
        List<DataRow> updateServer();
    }
}
