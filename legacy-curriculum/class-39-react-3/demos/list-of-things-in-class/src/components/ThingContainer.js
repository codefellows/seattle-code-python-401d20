import React, { Component } from 'react';


export default props => (
    <>
    <h1>List of things</h1>
    <ul>
        {props.things.map(thing => <ThingItem key={thing.id} thing={thing} onDelete={props.onDelete} />)}
    </ul>
    <ThingForm onCreated={props.onCreated}/>
    </>
)

function ThingItem(props) {
    return (
        <>
        <li>
            <p>{props.thing.name}</p>
            <button onClick={() => props.onDelete(props.thing)}>delete</button>
        </li>
        </>
    )
}

class ThingForm extends Component {

    constructor(props) {
        super(props)
        this.createThing = this.createThing.bind(this);
        this.changeHandler = this.changeHandler.bind(this);
        this.state = {
            formThing : '',
        }
    }

    createThing(event) {
        // let somebody know what was just created
        event.preventDefault();
        this.props.onCreated({name:this.state.formThing})

    }

    changeHandler(event) {
        this.setState({
            formThing: event.target.value
        })
    }

    render() {
        return (
            <form onSubmit={this.createThing}>
                <fieldset>
                    <legend>Enter Thing</legend>
                    <input value={this.state.formThing} onChange={this.changeHandler} type="text"/>
                    <button>OK</button>
                </fieldset>
            </form>
        )
    }


}
