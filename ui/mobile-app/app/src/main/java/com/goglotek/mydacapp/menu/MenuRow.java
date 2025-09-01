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
import java.util.Map;

public class MenuRow implements DataRow {

  private Menu next;
  private String text;
  private String name;
  private boolean selected;
  private int index;
  private RowDataType type;
  private String description;
  private List<Map<String, String>> rowOptions;

  @Override
  public Menu getNext() {
    return this.next;
  }

  @Override
  public String getText() {
    return this.text;
  }

  @Override
  public void setText(String text) {
    this.text = text;
  }

  @Override
  public String getName() {
    return this.name;
  }

  @Override
  public void setNext(Menu next) {
    this.next = next;
  }

  @Override
  public void setName(String name) {
    this.name = name;
  }

  @Override
  public boolean isSelected() {
    return this.selected;
  }

  @Override
  public void setSelected(Boolean selected) {
    this.selected = selected;
  }

  @Override
  public int getIndex() {
    return this.index;
  }

  @Override
  public void setIndex(int index) {
    this.index = index;
  }

  @Override
  public void setType(RowDataType type) {
    this.type = type;
  }

  @Override
  public RowDataType getType() {
    return this.type;
  }

  @Override
  public boolean equals(Object obj) {
    if (this == obj) {
      return true;
    }
    DataRow other = (DataRow) obj;
    return this.type == other.getType() && this.selected == other.isSelected()
        && this.name == other.getName() && this.text == other.getText();
  }

  @Override
  public List<Map<String, String>> getRowOptions() {
    return this.rowOptions;
  }

  @Override
  public void setRowOptions(List<Map<String, String>> options) {
    this.rowOptions = options;
  }

  @Override
  public String getDescription() {
    return this.description;
  }

  @Override
  public void setDescription(String description) {
    this.description = description;
  }
}
