package com.goglotek.mydacapp.menu;

public class MenuRow implements DataRow {
    private Menu next;
    private String text;
    private String name;
    private boolean selected;
    private int index;
    private RowDataType type;

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
        return this.type == other.getType() && this.selected == other.isSelected() && this.name == other.getName() && this.text == other.getText();
    }
}
