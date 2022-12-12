import React from 'react';
import axios from 'axios';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  NavLink,
  useRouteMatch,
  Redirect,
} from 'react-router-dom';

import './App.scss';

class App extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      things: []
    }
    this.createThingHandler = this.createThingHandler.bind(this);
    this.updateThingHandler = this.updateThingHandler.bind(this);
    this.deleteThingHandler = this.deleteThingHandler.bind(this);
    this.renderThingDetail = this.renderThingDetail.bind(this);
  }


  async componentDidMount() {

    // Soon will get from API
    const response = await axios.get('/data/things.json')

    this.setState({
      things: response.data
    })
  }

  createThingHandler(thing) {

    thing.id = Math.floor(Math.random() * 1000); // DANGER: don't do this in production, just getting to temporarily work until we get an api

    const things = [...this.state.things, thing]// same as this.state.things.concat(thing) but more common in react

    this.setState({
      things: things // see alternate style below
    })
  }

  updateThingHandler(updatedThing) {

    const things = this.state.things.map(thing => {
      if (thing.id === updatedThing.id) {
        thing.name = updatedThing.name
      }
      return thing;
    })

    this.setState({ things }) // huh??? No colon?
  }

  deleteThingHandler(thingToDelete) {
    const things = this.state.things.filter(thing => thing.id !== thingToDelete.id)
    this.setState({ things })
  }

  renderThingDetail(props) {

    // DANGER: what happens with no casting?
    const id = parseInt(props.match.params.id);

    const thing = this.state.things.find(thing => thing.id === id);

    return thing ? <ThingDetail thing={thing} onUpdateThing={this.updateThingHandler} onDeleteThing={this.deleteThingHandler} /> : <Redirect to="/things" />
  }

  render() {

    return (
      <Router>
        <div className="App">
          <Nav />
          <Switch>
            <Route path="/" exact>
              <h1>Home Page</h1>
            </Route>
            <Route path="/about" >
              <h1>About Page</h1>
            </Route>
            <Route path="/things" exact>
              <>
                <ThingCounter things={this.state.things} />
                <ThingsList things={this.state.things} />
                <ThingForm onSubmitThing={this.createThingHandler} />
              </>
            </Route>
            <Route path="/things/:id" render={this.renderThingDetail} />
          </Switch>
        </div>
      </Router>
    );
  }
}

function Nav(props) {
  return (
    <nav>
      <ul>
        <li><NavLink to="/">Home</NavLink></li>
        <li><NavLink to="/about">About</NavLink></li>
        <li><NavLink to="/things">Things</NavLink></li>
      </ul>
    </nav>
  )
}


function ThingsList(props) {

  return (
    <>
      <h2>ThingsList</h2>
      <ul>
        {props.things.map(thing => <ThingItem key={thing.id} thing={thing} />)}
      </ul>
    </>
  )

}

function ThingDetail(props) {

  // need to do some extra stuff inside a functional component.
  // No prob. Functions can be defined inside another function

  function deleteThingHandler() {
    props.onDeleteThing(props.thing);
  }

  return (
    <>
      <h3>{props.thing.name}</h3>
      <ThingForm onSubmitThing={props.onUpdateThing} initialThing={props.thing} />
      <button onClick={deleteThingHandler}>delete</button>
    </>

  )

}
function ThingItem(props) {
  const match = useRouteMatch();
  return <li><Link to={`${match.path}/${props.thing.id}`}>{props.thing.name}</Link></li>
}

class ThingForm extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      thingName: props.initialThing ? props.initialThing.name : '',
      id: props.initialThing && props.initialThing.id,
    }
    this.changeHandler = this.changeHandler.bind(this);
    this.submitHandler = this.submitHandler.bind(this);
  }

  changeHandler(event) {
    this.setState({
      thingName: event.target.value,
    })
  }

  submitHandler(event) {
    event.preventDefault();
    this.props.onSubmitThing({
      name: this.state.thingName,
      id: this.state.id,
    });
    this.setState({ thingName: '', id: null })
  }



  render() {
    return (
      <form onSubmit={this.submitHandler}>
        <fieldset>
          <legend>Name of thing</legend>
          <input onChange={this.changeHandler} name="thingName" type="text" value={this.state.thingName} />
          <button>ok</button>
        </fieldset>
      </form>
    )
  }
}

function ThingCounter({ things }) {
  return <p># of things : {things.length}</p>
}


export default App;
