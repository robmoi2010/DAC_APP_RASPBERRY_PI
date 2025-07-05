package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.service.DacService;
import com.goglotek.mydacapp.service.SystemService;

import java.util.Collections;
import java.util.List;

public class VolumeDeviceProcessor implements DynamicDataProcessor {
    private static VolumeDeviceProcessor loader;

    private VolumeDeviceProcessor() {

    }

    @Override
    public List<DataRow> loadData() throws GoglotekException {
       String data = SystemService.getVolumeDevice();
        return processServerData(data);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = SystemService.updateVolumeDevice(data);
        return processServerData(response);
    }

    public static VolumeDeviceProcessor getInstance() {
        if (loader == null) {
            loader = new VolumeDeviceProcessor();
        }
        return loader;
    }
}
