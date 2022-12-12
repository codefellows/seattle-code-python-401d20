import React from 'react';
import axios from 'axios';

import {
    BrowserRouter as Router,
    Switch,
    Route,
    Redirect,
  } from "react-router-dom";

import './App.scss';
import LoginForm from './components/LoginForm';
import SnackList from './components/SnackList';
import SnackDetail from './components/SnackDetail';


const url = 'http://167.172.203.221:8000/api/';

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            accessToken: '',
            refreshToken:'',
            snacks: null,
        }
        this.loginHandler = this.loginHandler.bind(this);
        this.createHandler = this.createHandler.bind(this);
        this.updateHandler = this.updateHandler.bind(this);
        this.deleteHandler = this.deleteHandler.bind(this);
        this.renderSnackDetail = this.renderSnackDetail.bind(this);
    }

    async loginHandler({access, refresh}) {
        this.setState({
            accessToken : access,
            refreshToken : refresh,
        });

        try {
            const headers = {
                headers: {
                    Authorization: `Bearer ${this.state.accessToken}`
                }
            }
            const response = await axios.get(url + 'v1/', headers);

            console.log(response.data);

            this.setState({
                snacks: response.data
            });

        } catch (error) {
            console.error('ruhroh');
        }

    }

    async createHandler(data) {

        const headers = {
            headers: {
                Authorization: `Bearer ${this.state.accessToken}`
            }
        }

        const response = await axios.post(url + 'v1/', data, headers);

        console.log(response.data);

        this.setState({
            snacks: this.state.snacks.concat(response.data)
        })


    }

    async updateHandler(data) {

        const headers = {
            headers: {
                Authorization: `Bearer ${this.state.accessToken}`
            }
        }

        const path = `${url}v1/${data.id}`;

        console.log('path', path);
        const response = await axios.put(path, data, headers);

        console.log(response.data);

        this.setState({
            snacks: this.state.snacks.map(snack => {
                if (snack.id === data.id) {
                    return data;
                } else {
                    return snack;
                }
            })
        })

    }

    async deleteHandler(id) {

        const headers = {
            headers: {
                Authorization: `Bearer ${this.state.accessToken}`
            }
        }

        const path = `${url}v1/${id}`;

        console.log('path', path);

        const response = await axios.delete(path, headers);

        console.log(response.data);

        this.setState({
            snacks: this.state.snacks.filter(snack => snack.id !== id)
        })

    }

    renderSnackDetail(props) {

        if (!this.state.accessToken) {
            return <Redirect to="/" />
        }

        const snackId = parseInt(props.match.params.id);

        const snack = this.state.snacks && this.state.snacks.find(snack => snack.id === snackId);

        if (snack) {
            return <SnackDetail snack={snack} onSubmit={this.updateHandler} onDelete={this.deleteHandler} />
        } else {
            return <Redirect to="/" />
        }
    }


    render() {
        return (
            <Router>

            <div className="App">

                <Switch>

                    <Route exact path="/">

                        {this.state.snacks ?
                            <SnackList snacks={this.state.snacks} onSubmit={this.createHandler} /> :
                            <LoginForm onSuccess={this.loginHandler} />}

                    </Route>

                    <Route path="/:id" render={this.renderSnackDetail} />

                </Switch>

            </div>
            </Router>
        );
    }
}

export default App;
