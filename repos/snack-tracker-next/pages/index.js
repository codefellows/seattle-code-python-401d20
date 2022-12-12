import { Component } from 'react'
import DataFetcher from '../services/data-fetcher'

export default class Home extends Component {

    constructor(props) {
        super(props);
        this.fetcher = new DataFetcher("https://snack-tracker-api.herokuapp.com/api/v1/");
        this.state = {
            loggedIn: false,
            snacks: []
        }
    }

    async logInHandler() {

        const loggedIn = await this.fetcher.logIn("jb", "jb");

        this.setState({ loggedIn });

    }

    logOutHandler() {

        this.fetcher.logOut();

        this.setState({ loggedIn: false, snacks: [] })
    }

    async getSnacksHandler() {
        const snacks = await this.fetcher.fetchResource('snacks');
        this.setState({ snacks });
    }

    render() {
        return (
            <div className="container">
                {this.state.loggedIn ? (
                    <button onClick={() => this.logOutHandler()}>Log Out</button>
                ) : (

                <button onClick={() => this.logInHandler()}>Log In</button>
                )}

                <button onClick={() => this.getSnacksHandler()}>Get Snacks</button>

                <ul>
                    {this.state.snacks.map(snack => (
                        <li key={snack.id}>{snack.name}</li>
                    ))}
                </ul>
            </div>
        )
    }
}

