import React, { Component } from 'react'
import axios from 'axios'

import Footer from './components/Footer';
import Header from './components/Header';
import ThingContainer from './components/ThingContainer';


class App extends Component {

    constructor(props) {
        super(props);

        this.state = {
            things : []
        }
        this.createThingHandler = this.createThingHandler.bind(this);
        this.deleteHandler = this.deleteHandler.bind(this);
    }

    async componentDidMount() {

        const response = await axios.get('/data/things.json');

        this.setState({
            things : response.data
        })

    }

    createThingHandler(thing) {
        thing.id = Math.floor(Math.random() * 1000); // DANGER: don't really do this. Just until API

        this.setState({
            things : this.state.things.concat(thing)
        })
    }

    deleteHandler(thingToDelete) {

        const newThings = this.state.things.filter(thing => thing.id !== thingToDelete.id);

        this.setState({
            things : newThings
        })
    }

    render() {
        return (
            <>
                <Header thing-count={this.state.things.length} />
                <ThingContainer things={this.state.things} onCreated={this.createThingHandler} onDelete={this.deleteHandler}  />
                <Footer copyright="1999" />
            </>
        )
    }

}

export default App;
