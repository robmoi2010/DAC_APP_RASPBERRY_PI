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

import java.util.List;

public class AppMenu implements Menu {

  private List<DataRow> rows;
  private MenuDataType dataType;
  private DataRow root;

  @Override
  public List<DataRow> getRows() {
    return this.rows;
  }

  @Override
  public void setRows(List<DataRow> rows) {
    this.rows = rows;
  }

  @Override
  public void addRow(DataRow row) {
    rows.add(row);
  }

  @Override
  public MenuDataType getDataType() {
    return this.dataType;
  }

  @Override
  public void setDataType(MenuDataType dataType) {
    this.dataType = dataType;
  }

  @Override
  public DataRow getRoot() {
    return this.root;
  }

  @Override
  public void setRoot(DataRow root) {
    this.root = root;
  }


}
