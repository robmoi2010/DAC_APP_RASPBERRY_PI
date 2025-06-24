package com.goglotek.mydacapp.menu;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class MenuUtil {
    private final static String DAC_SETTINGS_NAME = "DacSettings";
    private final static String DSP_SETTINGS_NAME = "DspSettings";
    private final static String SYSTEM_SETTINGS_NAME = "SystemSettings";
    private final static String VOLUME_SETTINGS_NAME = "VolumeSettings";
    private final static String FILTERS_NAME = "Filters";
    private final static String DAC_MODES_NAME = "DacModes";
    private final static String VOLUME_MODES_NAME = "VolumeModes";
    private final static String THD_COMPENSATION_NAME = "ThdCompensation";
    private final static String OVERSAMPLING_NAME = "Oversampling";
    private final static String DSP_INPUT_NAME = "Input";
    private final static String DSP_OUTPUT_NAME = "Output";
    private final static String VOLUME_DEVICE_NAME = "VolumeDevice";
    private final static String VOLUME_ALGORITHM_NAME = "VolumeAlgorithm";
    private final static String SOUND_MODES_NAME = "Sound Modes";
    private final static String ENABLE_NAME = "Enable";
    private final static String DISABLE_NAME = "Disable";
    private final static String SECOND_ORDER_NAME = "SecondOrder";
    private final static String THIRD_ORDER_NAME = "ThirdOrder";
    private final static String DSP_MAIN_OUTPUT_NAME = "MainOutput";
    private final static String DSP_SUBWOOFER_OUTPUT_NAME = "SubwooferOutput";


    public static Stack<Menu> menuStack = new Stack<>();
    private static char[] capitalLetters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    private static DataRow createRow(String name) {
        DataRow row = new MenuRow();
        row.setName(name);
        row.setText(textFromName(row.getName()));
        row.setNext(getNext(name));
        return row;
    }

    public static Menu createEnableDisableMenu() {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        rows.add(createRow(ENABLE_NAME));
        rows.add(createRow(DISABLE_NAME));
        menu.setRows(rows);
        return menu;
    }

    public static Menu createDynamicDataMenu() {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        //empty list that would be populated by server data
        menu.setRows(rows);
        return menu;
    }

    public static Menu createSettingsMenu() {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        rows.add(createRow(DAC_SETTINGS_NAME));
        rows.add(createRow(DSP_SETTINGS_NAME));
        rows.add(createRow(SYSTEM_SETTINGS_NAME));
        menu.setRows(rows);
        return menu;
    }

    public static Menu createThdCompensationMenu() {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        rows.add(createRow(SECOND_ORDER_NAME));
        rows.add(createRow(THIRD_ORDER_NAME));
        menu.setRows(rows);
        return menu;
    }

    public static Menu createDspOutputMenu() {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        rows.add(createRow(DSP_MAIN_OUTPUT_NAME));
        rows.add(createRow(DSP_SUBWOOFER_OUTPUT_NAME));
        menu.setRows(rows);
        return menu;
    }

    private static Menu getNext(String name) {
        if (name == DAC_SETTINGS_NAME) {
            return createDacSettingsMenu();
        }
        if (name == DSP_SETTINGS_NAME) {
            return createDspSettingsMenu();
        }
        if (name == SYSTEM_SETTINGS_NAME) {
            return createSystemSettingsMenu();
        }
        if (name == VOLUME_SETTINGS_NAME) {
            return createEnableDisableMenu();
        }
        if (name == FILTERS_NAME) {
            return createDynamicDataMenu();
        }
        if (name == DAC_MODES_NAME) {
            return createDynamicDataMenu();
        }
        if (name == VOLUME_MODES_NAME) {
            return createDynamicDataMenu();
        }
        if (name == THD_COMPENSATION_NAME) {
            return createThdCompensationMenu();
        }
        if (name == SECOND_ORDER_NAME) {
            return createEnableDisableMenu();
        }
        if (name == THIRD_ORDER_NAME) {
            return createEnableDisableMenu();
        }
        if (name == OVERSAMPLING_NAME) {
            return createEnableDisableMenu();
        }
        if (name == DSP_INPUT_NAME) {
            return createDynamicDataMenu();
        }
        if (name == DSP_OUTPUT_NAME) {
            return createDspOutputMenu();
        }
        if (name == DSP_MAIN_OUTPUT_NAME) {
            return createDynamicDataMenu();
        }
        if (name == DSP_SUBWOOFER_OUTPUT_NAME) {
            return createDynamicDataMenu();
        }
        if (name == VOLUME_DEVICE_NAME) {
            return createDynamicDataMenu();
        }
        if (name == VOLUME_ALGORITHM_NAME) {
            return createDspOutputMenu();
        }
        if (name == SOUND_MODES_NAME) {
            return createDynamicDataMenu();
        }
        return null;
    }

    public static Menu createSystemSettingsMenu() {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        rows.add(createRow(VOLUME_DEVICE_NAME));
        rows.add(createRow(VOLUME_ALGORITHM_NAME));
        rows.add(createRow(SOUND_MODES_NAME));
        menu.setRows(rows);
        return menu;
    }

    public static Menu createDspSettingsMenu() {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        rows.add(createRow(DSP_INPUT_NAME));
        rows.add(createRow(DSP_OUTPUT_NAME));
        menu.setRows(rows);
        return menu;

    }

    public static Menu createDacSettingsMenu() {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        rows.add(createRow(VOLUME_SETTINGS_NAME));
        rows.add(createRow(FILTERS_NAME));
        rows.add(createRow(DAC_MODES_NAME));
        rows.add(createRow(VOLUME_MODES_NAME));
        rows.add(createRow(THD_COMPENSATION_NAME));
        rows.add(createRow(OVERSAMPLING_NAME));
        menu.setRows(rows);
        return menu;
    }


    public static String textFromName(String name) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < name.length(); i++) {
            if (found(capitalLetters, name.charAt(i)) && i != 0) {
                sb.append(" ");
            }
            sb.append(name.charAt(i));
        }
        return sb.toString();
    }

    private static boolean found(char[] caps, char i) {
        for (char c : caps) {
            if (c == i) {
                return true;
            }
        }
        return false;
    }

    public static List<DataRow> loadDynamicData() {
        Menu previous=menuStack.peek();
        for(DataRow row:previous.getRows())
        {
            switch(row.getName())
            {

            }
        }
    }
}
