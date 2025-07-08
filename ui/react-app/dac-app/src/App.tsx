
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
