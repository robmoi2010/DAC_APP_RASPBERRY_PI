package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.service.DacService;

import java.util.Collections;
import java.util.List;

public class VolumeSettingsProcessor implements DynamicDataProcessor {
    private static VolumeSettingsProcessor loader;

    private VolumeSettingsProcessor() {

    }

    @Override
    public List<DataRow> loadData() throws GoglotekException {
        String data = DacService.getVolumeDisableStatus();
        return processServerToggleData(data);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = DacService.updateVolumeStatus(data);
        return processServerToggleData(response);
    }

    public static VolumeSettingsProcessor getInstance() {
        if (loader == null) {
            loader = new VolumeSettingsProcessor();
        }
        return loader;
    }
}
