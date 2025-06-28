package com.goglotek.mydacapp.dataprocessors;

import com.goglotek.mydacapp.exceptions.GoglotekException;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.service.DacService;

import java.util.Collections;
import java.util.List;

public class FiltersProcessor implements DynamicDataProcessor {
    private static FiltersProcessor loader;

    private FiltersProcessor() {

    }

    @Override
    public List<DataRow> loadData() throws GoglotekException {
        String data = DacService.getFilters();
        return processServerData(data);
    }

    @Override
    public List<DataRow> updateServerData(int index) throws GoglotekException {
        String data = generateResponseData(index);
        String response = DacService.updateFilter(data);
        return processServerData(response);
    }

    public static FiltersProcessor getInstance() {
        if (loader == null) {
            loader = new FiltersProcessor();
        }
        return loader;
    }

    public static interface ServerUpdater {
        List<DataRow> updateServer();
    }
}
