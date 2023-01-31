import logo from './logo.svg';
import './App.css';
import  LoginButton  from './LoginButton';
import LogoutButton from './LogoutButton';

function App() {
  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        
      </header> */}
      <LoginButton/>
      <LogoutButton/>
    </div>
  );
}

export default App;
