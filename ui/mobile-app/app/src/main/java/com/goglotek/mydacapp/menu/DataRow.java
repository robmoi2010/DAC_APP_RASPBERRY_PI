package com.goglotek.mydacapp.menu;

import java.io.Serializable;

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
}
