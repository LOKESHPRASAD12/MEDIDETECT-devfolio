import React from 'react';
import Login from './Login';
import Home from './Home';
import Braintumor from './braintumor';
import Brestcancer from './brestcancer';
import Covid from './covid';
import Cataract from './cataract';
import Skin from './skin';
import Reportannotation from './reportannotation';
import { BrowserRouter as Router,Routes,Route } from 'react-router-dom';

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path='/' element={<Login/>}/>
          <Route path='/home' element={<Home/>}/>
          <Route path='/braintumor' element={<Braintumor/>}/>
          <Route path='/brestcancer' element={<Brestcancer/>}/>
          <Route path='/covid' element={<Covid/>}/>
          <Route path='/cataract' element={<Cataract/>}/>
          <Route path='/skin' element={<Skin/>}/>
          <Route path='/reportannotation' element={<Reportannotation/>}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;

