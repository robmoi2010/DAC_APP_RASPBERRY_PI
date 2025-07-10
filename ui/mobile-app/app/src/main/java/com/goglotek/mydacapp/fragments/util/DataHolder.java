package com.goglotek.mydacapp.fragments.util;

import android.content.res.ColorStateList;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.appcompat.widget.SwitchCompat;
import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.RecyclerView;

import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.menu.RowDataType;
import com.google.android.material.checkbox.MaterialCheckBox;
import com.google.android.material.slider.LabelFormatter;
import com.google.android.material.slider.Slider;

import java.util.Map;

public class DataHolder extends RecyclerView.ViewHolder {
    DataAdapter.onSwitchChangeListener onSwitchChangeListener;
    DataAdapter.onSliderChangeListener onSliderChangeListener;

    public DataHolder(View view, DataAdapter.onSwitchChangeListener onSwitchChangeListener, DataAdapter.onSliderChangeListener onSliderChangeListener) {
        super(view);
        this.onSwitchChangeListener = onSwitchChangeListener;
        this.onSliderChangeListener = onSliderChangeListener;
    }

    public void bind(final DataRow dataRow, final DataAdapter.OnItemClickListener listener) {
        LinearLayout layout = createLinearLayout();
        if (dataRow.getType() == RowDataType.TOGGLE) {
            SwitchCompat switchBtn = createSwitch(dataRow.isSelected(), dataRow);
            switchBtn.setChecked(dataRow.isSelected());
            layout.addView(switchBtn);
        } else if (dataRow.getType() == RowDataType.NUMBER) {
            Slider slider = createSlider(dataRow);
            layout.addView(slider);
        } else {
            if (dataRow.isSelected()) {
                layout.addView(createCheckBox(dataRow.isSelected()));
            }
            layout.addView(createTextView(dataRow.getText()));
        }
        ((ViewGroup) itemView).removeAllViews();
        ((ViewGroup) itemView).addView(layout);
        itemView.setOnClickListener(v -> listener.onItemClick(dataRow));
    }

    private TextView createTextView(String text) {
        TextView textView = new TextView(itemView.getContext());
        textView.setTextSize(18);
        textView.setText(text);
        textView.setPadding(20, 20, 20, 20);
        textView.setLayoutParams(new ViewGroup.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        ));
        textView.setFocusable(false);
        return textView;
    }

    private CheckBox createCheckBox(boolean checked) {
        com.google.android.material.checkbox.MaterialCheckBox checkBox = new MaterialCheckBox(itemView.getContext());
        checkBox.setChecked(checked);
        checkBox.setEnabled(false);
        checkBox.setFocusable(false);
        checkBox.setButtonTintList(ColorStateList.valueOf(ContextCompat.getColor(itemView.getContext(), R.color.teal_700)));
        return checkBox;
    }

    private LinearLayout createLinearLayout() {
        LinearLayout linearLayout = new LinearLayout(itemView.getContext());
        linearLayout.setOrientation(LinearLayout.HORIZONTAL);
        linearLayout.setLayoutParams(new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        ));
        linearLayout.setPadding(24, 24, 24, 24);
        return linearLayout;
    }

    private SwitchCompat createSwitch(boolean checked, DataRow row) {

        SwitchCompat defaultSwitch = new SwitchCompat(itemView.getContext());
        defaultSwitch.setThumbDrawable(ContextCompat.getDrawable(itemView.getContext(), R.drawable.custom_thumb));
        defaultSwitch.setTrackDrawable(ContextCompat.getDrawable(itemView.getContext(), R.drawable.custom_track));
        if (checked) {
            defaultSwitch.setText("On");
        } else {
            defaultSwitch.setText("Off");
        }
        defaultSwitch.setChecked(checked);


        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        );
        //params.gravity = Gravity.CENTER;
        defaultSwitch.setLayoutParams(params);
        defaultSwitch.setOnCheckedChangeListener((buttonView, isChecked) -> {
            onSwitchChangeListener.handleSwitchChange(isChecked, row);
        });
        return defaultSwitch;
    }

    private Slider createSlider(DataRow row) {
        int min = 0;
        int max = 0;
        int step = 0;
        for (Map<String, String> map : row.getRowOptions()) {
            if (map.containsKey("MIN")) {
                min = Integer.parseInt(map.get("MIN"));
            }
            if (map.containsKey("MAX")) {
                max = Integer.parseInt(map.get("MAX"));
            }
            if (map.containsKey("STEP")) {
                step = Integer.parseInt(map.get("STEP"));
            }
        }
        Slider slider = new Slider(itemView.getContext());
        slider.setValueFrom(min);
        slider.setValueTo(max);
        slider.setStepSize(step);
        slider.setValue(Integer.parseInt(row.getText()));
        slider.setLabelBehavior(LabelFormatter.LABEL_FLOATING);
        slider.setLayoutParams(new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        ));
        slider.addOnSliderTouchListener(new Slider.OnSliderTouchListener() {
                                            @Override
                                            public void onStartTrackingTouch(@NonNull Slider slider) {

                                            }

                                            @Override
                                            public void onStopTrackingTouch(@NonNull Slider slider) {
                                                onSliderChangeListener.handleSliderChange((int) slider.getValue(), row);
                                            }
                                        }
        );

        return slider;
    }
}
