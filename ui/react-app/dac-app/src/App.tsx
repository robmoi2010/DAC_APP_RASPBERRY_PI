
import './App.css';
import Router from './components/Router';
import { Theme } from '@radix-ui/themes';
import { Provider } from './components/ui/provider';

function App() {
  return (
    <Theme>
      <Provider>
        <Router />
      </Provider>
    </Theme>
  )
}
export default App
