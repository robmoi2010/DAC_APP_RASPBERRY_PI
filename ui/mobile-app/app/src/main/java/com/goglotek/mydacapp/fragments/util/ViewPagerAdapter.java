package com.goglotek.mydacapp.fragments.util;

import android.util.SparseArray;
import android.widget.FrameLayout;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.viewpager2.adapter.FragmentStateAdapter;

import com.goglotek.mydacapp.fragments.MainTabFragment;
import com.goglotek.mydacapp.fragments.MenuFragment;
import com.goglotek.mydacapp.menu.DataRow;
import com.goglotek.mydacapp.menu.Menu;

import timber.log.Timber;

public class ViewPagerAdapter extends FragmentStateAdapter {
    private Menu menu;
    private SparseArray<MenuFragment> fragments = new SparseArray<>();

    public ViewPagerAdapter(@NonNull Fragment fragment, Menu menu) {
        super(fragment);
        this.menu = menu;
    }

    @NonNull
    @Override
    public Fragment createFragment(int position) {
        try {
            DataRow row = menu.getRows().get(position);
            MenuFragment fragment = MenuFragment.newInstance(row.getNext());
            fragments.put(position, fragment);
            return fragment;
            //} else {
            // MenuFragment fragment = MenuFragment.newInstance(menu);
            //  fragments.put(position, fragment);
            // return fragment;
            // }

//        if (menu.getDataType() == MenuDataType.STATIC) {
//            DisplayFragment fragment = DisplayFragment.newInstance(row.getNext());
//            fragments.put(position, fragment);
//            return fragment;
//        } else {
//            DisplayFragment fragment = DisplayFragment.newInstance(menu);
//            fragments.put(position, fragment);
//            return fragment;
//        }
        } catch (Exception e) {
            Timber.e(e, e.getMessage());
        }
        return null;
    }

    public MenuFragment getFragment(int pos) {
        return fragments.get(pos);
    }

    @Override
    public int getItemCount() {
        return this.menu.getRows().size();
    }
}
