package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.service.DacService;
import com.goglotek.mydacapp.service.SystemService;

import java.util.Collections;
import java.util.List;

public class SoundModesProcessor implements DynamicDataProcessor {
    private static SoundModesProcessor loader;

    private SoundModesProcessor() {

    }

    @Override
    public List<DataRow> loadData() throws GoglotekException {
        String data = SystemService.getSoundModes();
        return processServerData(data);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = SystemService.updateSoundMode(data);
        return processServerData(response);
    }

    public static SoundModesProcessor getInstance() {
        if (loader == null) {
            loader = new SoundModesProcessor();
        }
        return loader;
    }
}
