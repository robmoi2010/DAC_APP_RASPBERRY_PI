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

package com.goglotek.mydacapp.fragments.util;

import androidx.recyclerview.widget.DiffUtil;
import com.goglotek.mydacapp.menu.DataRow;
import java.util.List;

public class DiffCallBack extends DiffUtil.Callback {

  private List<DataRow> oldList;
  private List<DataRow> newList;

  public DiffCallBack(List<DataRow> oldList, List<DataRow> newList) {
    this.oldList = oldList;
    this.newList = newList;
  }

  @Override
  public int getOldListSize() {
    return oldList.size();
  }

  @Override
  public int getNewListSize() {
    return newList.size();
  }

  @Override
  public boolean areItemsTheSame(int oldItemPosition, int newItemPosition) {
    DataRow oldItem = this.oldList.get(oldItemPosition);
    DataRow newItem = this.newList.get(newItemPosition);
    return sameItem(oldItem, newItem);
  }

  @Override
  public boolean areContentsTheSame(int oldItemPosition, int newItemPosition) {
    DataRow oldItem = this.oldList.get(oldItemPosition);
    DataRow newItem = this.newList.get(newItemPosition);
    return sameItem(oldItem, newItem);
  }

  private boolean sameItem(DataRow oldItem, DataRow newItem) {
    return oldItem.getText() == newItem.getText() && oldItem.getName() == newItem.getName()
        && oldItem.isSelected() == newItem.isSelected();
  }
}
