import React from 'react';
import Form from './form.js';
import Person from './person.js'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      results: [],
    };
  }

  handleForm = (results) => {
    console.log(results);
    this.setState({ results });
  };

  render() {
    return (
      <React.Fragment>
        <Form prompt="Click for Star Wars Peeps!" handler={this.handleForm} />
        
        <ul>
        {this.state.results.map(person => (
          <Person name={person.name} url={person.url} />
        ))}
        </ul>
      </React.Fragment>
    );
  }
}

export default App;
