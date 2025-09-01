/*
 * Copyright (C) 2025 Robert Moi, Goglotek LTD
 *
 *  This file is part of the DAC_APPLICATION System.
 *
 *  The DAC_APPLICATION System is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  The DAC_APPLICATION is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with the Fraud Detector System. If not, see <https://www.gnu.org/licenses/>
 */

package com.goglotek.mydacapp.menu;

import java.util.ArrayList;
import java.util.List;

public class MenuUtil {

  public final static String DAC_SETTINGS_NAME = "DacSettings";
  public final static String DSP_SETTINGS_NAME = "DspSettings";
  public final static String SYSTEM_SETTINGS_NAME = "SystemSettings";
  public final static String VOLUME_SETTINGS_NAME = "VolumeSettings";
  public final static String FILTERS_NAME = "Filters";
  public final static String DAC_MODES_NAME = "DacModes";
  public final static String VOLUME_MODES_NAME = "VolumeModes";
  public final static String THD_COMPENSATION_NAME = "ThdCompensation";
  public final static String OVERSAMPLING_NAME = "Oversampling";
  public final static String DSP_INPUT_NAME = "Input";
  public final static String DSP_OUTPUT_NAME = "Output";
  public final static String VOLUME_DEVICE_NAME = "VolumeDevice";
  public final static String VOLUME_ALGORITHM_NAME = "VolumeAlgorithm";
  public final static String SOUND_MODES_NAME = "Sound Modes";
  public final static String SECOND_ORDER_NAME = "SecondOrder";
  public final static String THIRD_ORDER_NAME = "ThirdOrder";
  public final static String DSP_MAIN_OUTPUT_NAME = "MainOutput";
  public final static String DSP_SUBWOOFER_OUTPUT_NAME = "SubwooferOutput";
  public final static String DPLL_BANDWIDTH_NAME = "DpllBandwidth";
  public static final String BASIC_DAC_SETTINGS_NAME = "Basic";
  public static final String ADVANCED_DAC_SETTINGS_NAME = "Advanced";
  public static final String VOLUME_RAMP_NAME = "VolumeRamp";

  //public static Stack<Menu> menuStack = new Stack<>();

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
    rows.add(createRow(SECOND_ORDER_NAME, RowDataType.TOGGLE));
    rows.add(createRow(THIRD_ORDER_NAME, RowDataType.TOGGLE));
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
    if (name == BASIC_DAC_SETTINGS_NAME) {
      return createBasicDacSettingsMenu(root);
    }
    if (name == ADVANCED_DAC_SETTINGS_NAME) {
      return createAdvancedDacSettingsMenu(root);
    }
    if (name == VOLUME_RAMP_NAME) {
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
    rows.add(createRow(VOLUME_RAMP_NAME, RowDataType.TOGGLE));
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
    rows.add(createRow(BASIC_DAC_SETTINGS_NAME, RowDataType.TEXT));
    rows.add(createRow(ADVANCED_DAC_SETTINGS_NAME, RowDataType.TEXT));
    menu.setRows(rows);
    menu.setDataType(MenuDataType.STATIC);
    menu.setRoot(root);
    return menu;
  }

  public static Menu createBasicDacSettingsMenu(DataRow root) {
    Menu menu = new AppMenu();
    List<DataRow> rows = new ArrayList<>();
    rows.add(createRow(VOLUME_SETTINGS_NAME, RowDataType.TOGGLE));
    rows.add(createRow(FILTERS_NAME, RowDataType.TEXT));
    rows.add(createRow(VOLUME_MODES_NAME, RowDataType.TEXT));
    menu.setRows(rows);
    menu.setDataType(MenuDataType.STATIC);
    menu.setRoot(root);
    return menu;
  }

  public static Menu createAdvancedDacSettingsMenu(DataRow root) {
    Menu menu = new AppMenu();
    List<DataRow> rows = new ArrayList<>();
    rows.add(createRow(THD_COMPENSATION_NAME, RowDataType.TEXT));
    rows.add(createRow(DAC_MODES_NAME, RowDataType.TEXT));
    rows.add(createRow(OVERSAMPLING_NAME, RowDataType.TOGGLE));
    rows.add(createRow(DPLL_BANDWIDTH_NAME, RowDataType.NUMBER));
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

}
