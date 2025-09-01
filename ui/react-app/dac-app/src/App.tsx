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
 *  along with the DAC_APPLICATION. If not, see <https://www.gnu.org/licenses/>
 */
import './App.css';
import Router from './components/Router';
import { Theme } from '@radix-ui/themes';
import { Provider } from './components/ui/provider';
import store from './state-repo/Store';
import { Provider as ReduxProvider } from 'react-redux';

function App() {
  return (
    <ReduxProvider store={store} >
      <Theme>
        <Provider>
          <Router />
        </Provider>
      </Theme>
    </ReduxProvider>
  )
}
export default App
