import React from 'react';

class App extends React.Component {


    render() {
    return <div>
        <h1>Hello, {this.props.user.name}. I am App </h1>
        <p>{this.props.greeting}</p>
        <p>{this.props.user.role} is what you are</p>
    </div>
    }
}

export default App
