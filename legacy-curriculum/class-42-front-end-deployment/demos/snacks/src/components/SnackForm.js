import React, { Component } from 'react';

class SnackForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            title: props.snack.title,
            description: props.snack.description,
        }
        this.changeHandler = this.changeHandler.bind(this);
        this.submitHandler = this.submitHandler.bind(this);
    }

    static defaultProps = {
        snack: {
            title: '',
            description: '',
        }
    }

    changeHandler(event) {

        this.setState({
            [event.target.name]: event.target.value
        })
    }

    submitHandler(event) {
        event.preventDefault();
        const data = {...this.state};
        data.id = this.props.snack.id;
        this.props.onSubmit(data);
        this.setState({
            title: '',
            description: ''
        })
    }

    render() {
        return (
            <>
                <form onSubmit={this.submitHandler}>
                    <fieldset>
                        <legend>
                            Post
                        </legend>
                        <input name="title" type="text" placeholder="title" value={this.state.title} onChange={this.changeHandler} />
                        <textarea name="description" placeholder="description" cols="30" rows="10" value={this.state.description} onChange={this.changeHandler}></textarea>
                        <button>ok</button>
                    </fieldset>
                </form>
            </>
        )
    }
}

export default SnackForm
