import React from 'react';
import ReactDOM from 'react-dom';

import App from './app.js';

class Main extends React.Component {


  render() {

    let greeting = 'Good day';

    const user = {
        name:'Terrell',
        role:'Developer'
    }

    return <App greeting={greeting} user={user}  />;
  }
}

const rootElement = document.getElementById('root');
ReactDOM.render(<Main />, rootElement);
