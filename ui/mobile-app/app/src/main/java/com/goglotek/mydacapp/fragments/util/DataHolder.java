package com.goglotek.mydacapp.fragments.util;

import android.content.res.ColorStateList;
import android.graphics.Color;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.appcompat.widget.SwitchCompat;
import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.RecyclerView;

import com.goglotek.mydacapp.R;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.menu.RowDataType;
import com.google.android.material.button.MaterialButton;
import com.google.android.material.card.MaterialCardView;
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
        LinearLayout layout = createLinearLayout(new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        ), LinearLayout.VERTICAL, Gravity.CENTER);
        LinearLayout detailsLayout = createLinearLayout(new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        ), LinearLayout.VERTICAL, Gravity.CENTER);
        ImageView detailsImg = createImageView();
        if (dataRow.getType() == RowDataType.TOGGLE) {
            SwitchCompat switchBtn = createSwitch(dataRow.isSelected(), dataRow);
            switchBtn.setChecked(dataRow.isSelected());
            layout.addView(switchBtn);
        } else if (dataRow.getType() == RowDataType.NUMBER) {
            Slider slider = createSlider(dataRow);
            layout.addView(slider);
        } else {
            LinearLayout cardLayout = createLinearLayout(new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT
            ), LinearLayout.VERTICAL, Gravity.CENTER);
            if (dataRow.isSelected()) {
                cardLayout.addView(createCheckBox(dataRow.isSelected()));
            }
            cardLayout.addView(createTextView(new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.WRAP_CONTENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT
            ), dataRow.getText(), Color.BLACK));
            MaterialButton button = createButton("Select");
            button.setOnClickListener(v -> {
                listener.onItemClick(dataRow);
            });
            cardLayout.addView(button);

            detailsImg.setOnClickListener(V -> {
                toggleDetailsView(detailsLayout, detailsImg);
            });
            cardLayout.addView(detailsImg);
            layout.addView(cardLayout);

            detailsLayout.addView(createTextView(new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT
            ), dataRow.getDescription(), Color.GRAY));
            detailsLayout.setVisibility(View.GONE);

            layout.addView(detailsLayout);
        }
        ((ViewGroup) itemView).removeAllViews();
        ((ViewGroup) itemView).addView(layout);
    }

    private void toggleDetailsView(LinearLayout detailsLayout, ImageView arrow) {
        boolean visible = detailsLayout.getVisibility() == View.VISIBLE;
        detailsLayout.setVisibility(visible ? View.GONE : View.VISIBLE);
        arrow.animate().rotation(visible ? 0 : 180).setDuration(200).start();
    }

    private TextView createTextView(ViewGroup.LayoutParams params, String text, int textColor) {
        TextView textView = new TextView(itemView.getContext());
        textView.setTextSize(18);
        textView.setText(text);
        textView.setPadding(20, 20, 20, 20);
        textView.setLayoutParams(params);
        textView.setFocusable(false);
        textView.setTextColor(textColor);
        return textView;
    }

    private MaterialButton createButton(String text) {
        MaterialButton button = new MaterialButton(itemView.getContext());

        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.WRAP_CONTENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        );
        button.setLayoutParams(params);
        button.setBackgroundColor(Color.TRANSPARENT);
        button.setRippleColor(ColorStateList.valueOf(Color.TRANSPARENT));
        button.setElevation(0f);
        button.setStateListAnimator(null);
        button.setStrokeColor(ColorStateList.valueOf(Color.BLUE)); // outline color
        button.setStrokeWidth(1); // border thickness
        button.setText(text);
        button.setCornerRadius(16);
        button.setAllCaps(false);
        button.setTextColor(Color.GRAY);
        button.setBackgroundTintList(ColorStateList.valueOf(Color.TRANSPARENT));
        return button;
    }

    private CheckBox createCheckBox(boolean checked) {
        com.google.android.material.checkbox.MaterialCheckBox checkBox = new MaterialCheckBox(itemView.getContext());
        checkBox.setChecked(checked);
        checkBox.setEnabled(false);
        checkBox.setFocusable(false);
        checkBox.setButtonTintList(ColorStateList.valueOf(Color.parseColor("#4CAF50")));
        return checkBox;
    }

    private LinearLayout createLinearLayout(ViewGroup.LayoutParams params, int orientation, int gravity) {
        LinearLayout linearLayout = new LinearLayout(itemView.getContext());
        linearLayout.setOrientation(orientation);
        linearLayout.setGravity(gravity);
        linearLayout.setLayoutParams(params);
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

    private ImageView createImageView() {
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.WRAP_CONTENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        );
        params.setMargins(0, 50, 0, 0);
        ImageView arrow = new ImageView(itemView.getContext());
        arrow.setImageResource(R.drawable.angle_small_down_green);
        arrow.setRotation(0f);
        arrow.setLayoutParams(params);
        return arrow;
    }
}
