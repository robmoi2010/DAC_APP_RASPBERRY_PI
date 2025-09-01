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

import java.io.Serializable;
import java.util.List;
import java.util.Map;

public interface DataRow extends Serializable {

  public Menu getNext();

  public String getText();

  public void setText(String text);

  public String getName();

  public void setNext(Menu next);

  public void setName(String name);

  public boolean isSelected();

  public void setSelected(Boolean selected);

  public int getIndex();

  public void setIndex(int index);

  public void setType(RowDataType type);

  public RowDataType getType();

  public boolean equals(Object obj);

  public List<Map<String, String>> getRowOptions();

  public void setRowOptions(List<Map<String, String>> options);

  public String getDescription();

  public void setDescription(String description);
}
