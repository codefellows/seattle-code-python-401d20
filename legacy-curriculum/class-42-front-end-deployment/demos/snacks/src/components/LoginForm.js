import React, { Component } from 'react';
import axios from 'axios';

const url = 'http://167.172.203.221:8000/api/';

class LoginForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            username: '',
            password: '',
        }
        this.obtainTokens = this.obtainTokens.bind(this);
        this.changeHandler = this.changeHandler.bind(this);
    }

    changeHandler(event) {
        this.setState({
            [event.target.name] : event.target.value
        })
    }


    async obtainTokens(event) {

        event.preventDefault();

        try {
            const response = await axios.post(url + 'token/', {
                username: this.state.username,
                password: this.state.password,
            });

            this.props.onSuccess(response.data);

        } catch (error) {
            console.error('ugh', error);
        }


    }

    render() {
        return (<>
            <form onSubmit={this.obtainTokens}>
                <input name="username" type="text" value={this.state.username} placeholder="username" onChange={this.changeHandler}/>
                <input name="password" type="password" value={this.state.password} placeholder="password" onChange={this.changeHandler}/>
                <button>ok</button>
            </form>
        </>)
    }

}

export default LoginForm;
