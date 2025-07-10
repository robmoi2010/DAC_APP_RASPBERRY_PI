package com.goglotek.mydacapp.menu;

import com.goglotek.mydacapp.dataprocessors.DacModesProcessor;
import com.goglotek.mydacapp.dataprocessors.DpllBandwidthProcessor;
import com.goglotek.mydacapp.dataprocessors.DspInputProcessor;
import com.goglotek.mydacapp.dataprocessors.DspMainOutputProcessor;
import com.goglotek.mydacapp.dataprocessors.DspSubwooferOutputProcessor;
import com.goglotek.mydacapp.dataprocessors.DynamicDataProcessor;
import com.goglotek.mydacapp.dataprocessors.FiltersProcessor;
import com.goglotek.mydacapp.dataprocessors.OversamplingProcessor;
import com.goglotek.mydacapp.dataprocessors.SecondOrderProcessor;
import com.goglotek.mydacapp.dataprocessors.SoundModesProcessor;
import com.goglotek.mydacapp.dataprocessors.ThirdOrderProcessor;
import com.goglotek.mydacapp.dataprocessors.VolumeAlgorithmProcessor;
import com.goglotek.mydacapp.dataprocessors.VolumeDeviceProcessor;
import com.goglotek.mydacapp.dataprocessors.VolumeModesProcessor;
import com.goglotek.mydacapp.dataprocessors.VolumeSettingsProcessor;

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

    private final static String SECOND_ORDER_NAME = "SecondOrder";
    private final static String THIRD_ORDER_NAME = "ThirdOrder";
    private final static String DSP_MAIN_OUTPUT_NAME = "MainOutput";
    private final static String DSP_SUBWOOFER_OUTPUT_NAME = "SubwooferOutput";
    private final static String DPLL_BANDWIDTH_NAME = "DpllBandwidth";


    public static Stack<Menu> menuStack = new Stack<>();
    private static char[] capitalLetters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    private static DataRow createRow(String name, RowDataType type) {
        DataRow row = new MenuRow();
        row.setName(name);
        row.setText(textFromName(row.getName()));
        row.setNext(getNext(name, row));
        row.setType(type);
        return row;
    }

    public static Menu createAppMenus() {
        return createSettingsMenu(null);
    }

    public static Menu createDynamicDataMenu(DataRow root) {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        //empty list that would be populated by server data
        menu.setRows(rows);
        menu.setDataType(MenuDataType.DYNAMIC);
        menu.setRoot(root);
        return menu;
    }

    public static Menu createSettingsMenu(DataRow root) {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        rows.add(createRow(DAC_SETTINGS_NAME, RowDataType.TEXT));
        rows.add(createRow(DSP_SETTINGS_NAME, RowDataType.TEXT));
        rows.add(createRow(SYSTEM_SETTINGS_NAME, RowDataType.TEXT));
        menu.setRows(rows);
        menu.setDataType(MenuDataType.STATIC);
        menu.setRoot(root);
        return menu;
    }

    public static Menu createThdCompensationMenu(DataRow root) {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        rows.add(createRow(SECOND_ORDER_NAME, RowDataType.TEXT));
        rows.add(createRow(THIRD_ORDER_NAME, RowDataType.TEXT));
        menu.setRows(rows);
        menu.setDataType(MenuDataType.STATIC);
        menu.setRoot(root);
        return menu;
    }

    public static Menu createDspOutputMenu(DataRow root) {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        rows.add(createRow(DSP_MAIN_OUTPUT_NAME, RowDataType.TEXT));
        rows.add(createRow(DSP_SUBWOOFER_OUTPUT_NAME, RowDataType.TEXT));
        menu.setRows(rows);
        menu.setDataType(MenuDataType.STATIC);
        menu.setRoot(root);
        return menu;
    }

    private static Menu getNext(String name, DataRow root) {
        if (name == DAC_SETTINGS_NAME) {
            return createDacSettingsMenu(root);
        }
        if (name == DSP_SETTINGS_NAME) {
            return createDspSettingsMenu(root);
        }
        if (name == SYSTEM_SETTINGS_NAME) {
            return createSystemSettingsMenu(root);
        }
        if (name == VOLUME_SETTINGS_NAME) {
            return createDynamicDataMenu(root);
        }
        if (name == FILTERS_NAME) {
            return createDynamicDataMenu(root);
        }
        if (name == DAC_MODES_NAME) {
            return createDynamicDataMenu(root);
        }
        if (name == VOLUME_MODES_NAME) {
            return createDynamicDataMenu(root);
        }
        if (name == THD_COMPENSATION_NAME) {
            return createThdCompensationMenu(root);
        }
        if (name == SECOND_ORDER_NAME) {
            return createDynamicDataMenu(root);
        }
        if (name == THIRD_ORDER_NAME) {
            return createDynamicDataMenu(root);
        }
        if (name == OVERSAMPLING_NAME) {
            return createDynamicDataMenu(root);
        }
        if (name == DSP_INPUT_NAME) {
            return createDynamicDataMenu(root);
        }
        if (name == DSP_OUTPUT_NAME) {
            return createDspOutputMenu(root);
        }
        if (name == DSP_MAIN_OUTPUT_NAME) {
            return createDynamicDataMenu(root);
        }
        if (name == DSP_SUBWOOFER_OUTPUT_NAME) {
            return createDynamicDataMenu(root);
        }
        if (name == VOLUME_DEVICE_NAME) {
            return createDynamicDataMenu(root);
        }
        if (name == VOLUME_ALGORITHM_NAME) {
            return createDynamicDataMenu(root);
        }
        if (name == SOUND_MODES_NAME) {
            return createDynamicDataMenu(root);
        }
        if (name == DPLL_BANDWIDTH_NAME) {
            return createDynamicDataMenu(root);
        }
        return null;
    }

    public static Menu createSystemSettingsMenu(DataRow root) {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        rows.add(createRow(VOLUME_DEVICE_NAME, RowDataType.TEXT));
        rows.add(createRow(VOLUME_ALGORITHM_NAME, RowDataType.TEXT));
        rows.add(createRow(SOUND_MODES_NAME, RowDataType.TEXT));
        menu.setRows(rows);
        menu.setDataType(MenuDataType.STATIC);
        menu.setRoot(root);
        return menu;
    }

    public static Menu createDspSettingsMenu(DataRow root) {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        rows.add(createRow(DSP_INPUT_NAME, RowDataType.TEXT));
        rows.add(createRow(DSP_OUTPUT_NAME, RowDataType.TEXT));
        menu.setRows(rows);
        menu.setDataType(MenuDataType.STATIC);
        menu.setRoot(root);
        return menu;

    }

    public static Menu createDacSettingsMenu(DataRow root) {
        Menu menu = new AppMenu();
        List<DataRow> rows = new ArrayList<>();
        rows.add(createRow(VOLUME_SETTINGS_NAME, RowDataType.TEXT));
        rows.add(createRow(FILTERS_NAME, RowDataType.TEXT));
        rows.add(createRow(DAC_MODES_NAME, RowDataType.TEXT));
        rows.add(createRow(VOLUME_MODES_NAME, RowDataType.TEXT));
        rows.add(createRow(THD_COMPENSATION_NAME, RowDataType.TEXT));
        rows.add(createRow(OVERSAMPLING_NAME, RowDataType.TEXT));
        rows.add(createRow(DPLL_BANDWIDTH_NAME, RowDataType.TEXT));
        menu.setRows(rows);
        menu.setDataType(MenuDataType.STATIC);
        menu.setRoot(root);
        return menu;
    }


    public static String textFromName(String name) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < name.length(); i++) {
            if (Character.isUpperCase(name.charAt(i)) && i != 0) {
                sb.append(" ");
            }
            sb.append(name.charAt(i));
        }
        return sb.toString();
    }

    public static DynamicDataProcessor getDataProcessor(DataRow root) {

        String name = root.getName();

        if (name == VOLUME_SETTINGS_NAME) {
            return VolumeSettingsProcessor.getInstance();
        }
        if (name == FILTERS_NAME) {
            return FiltersProcessor.getInstance();
        }
        if (name == DAC_MODES_NAME) {
            return DacModesProcessor.getInstance();
        }
        if (name == VOLUME_MODES_NAME) {
            return VolumeModesProcessor.getInstance();
        }
        if (name == SECOND_ORDER_NAME) {
            return SecondOrderProcessor.getInstance();
        }
        if (name == THIRD_ORDER_NAME) {
            return ThirdOrderProcessor.getInstance();
        }
        if (name == OVERSAMPLING_NAME) {
            return OversamplingProcessor.getInstance();
        }
        if (name == DSP_INPUT_NAME) {
            return DspInputProcessor.getInstance();
        }
        if (name == DSP_MAIN_OUTPUT_NAME) {
            return DspMainOutputProcessor.getInstance();
        }
        if (name == DSP_SUBWOOFER_OUTPUT_NAME) {
            return DspSubwooferOutputProcessor.getInstance();
        }
        if (name == VOLUME_DEVICE_NAME) {
            return VolumeDeviceProcessor.getInstance();
        }
        if (name == SOUND_MODES_NAME) {
            return SoundModesProcessor.getInstance();
        }
        if (name == VOLUME_ALGORITHM_NAME) {
            return VolumeAlgorithmProcessor.getInstance();
        }
        if (name == DPLL_BANDWIDTH_NAME) {
            return DpllBandwidthProcessor.getInstance();
        }
        return null;
    }

}
