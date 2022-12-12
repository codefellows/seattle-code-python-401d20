import React from 'react';
import './App.css';

class App extends React.Component {

    constructor(props) {
        super(props);
        this.submitHandler = this.submitHandler.bind(this);
    }

    submitHandler(snack) {
        console.log(snack)
        alert(snack.snackType);
    }

    render() {
        return (
            <div className="App">
            <SnackList />
            <SnackForm onSubmit={this.submitHandler}/>
            </div>
        );
    }
}


class SnackForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          isYummy: true,
          snackType: ''
        };

        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
      }

      handleInputChange(event) {
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;

        this.setState({
          [name]: value
        });
      }

      handleSubmit(event) {
          event.preventDefault();
          this.props.onSubmit(this.state);
      }

      render() {
        return (
          <form onSubmit={this.handleSubmit}>
            <label>
              Is yummy:
              <input
                name="isYummy"
                type="checkbox"
                checked={this.state.isYummy}
                onChange={this.handleInputChange} />
            </label>
            <br />
            <label>
              Snack Type:
              <input
                name="snackType"
                type="text"
                value={this.state.snackType}
                onChange={this.handleInputChange} />
            </label>
            <button>submit</button>
          </form>
        );
      }


}
function SnackItem(props) {
    return <li><p>{JSON.stringify(props.snack)}</p></li>
}

class SnackList extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            snacks: [
                {id: 412, snackType: 'Apple Slices'},
                {id: 543, snackType: 'Funions'},
            ]
        }
    }

    render() {
        return (
            this.state.snacks.length &&
            <ul>
                {this.state.snacks.map(snack => <SnackItem key={snack.id} snack={snack} />)}
            </ul>

        )
    }
}

export default App;
