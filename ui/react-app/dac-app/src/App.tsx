import { Theme } from '@radix-ui/themes';
import './App.css';
import Router from './components/Router';
import { Provider } from 'react-redux';
import store from "./state-repo/Store";

function App() {
  return (

    <Provider store={store}>
      <Theme>
        <Router />
      </Theme>
    </Provider>

  )
}

export default App
