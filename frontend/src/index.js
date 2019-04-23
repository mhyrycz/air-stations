import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Stations from './Components/Stations'
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<Stations />, document.getElementById('root'));

registerServiceWorker();
