import React from 'react'

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            message: 'nothing to see here'
        };
    }

    render() {
        return (
            <div>
            <h1>Counter App</h1>
            <h3>{this.state.message}</h3>
            <input></input>
            <button onClick={() => this.setState({message:'Coming Soon!!!'})}>Click Me</button>
            <footer>&copy; 2018 Code Fellows</footer>
            </div>
        );
    }
}

export default App;
