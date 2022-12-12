import React from 'react'
import { Link } from "react-router-dom"
import SnackForm from './SnackForm'


export default props => (
    <>
        <Link to="/"><p>Snack List</p></Link>
        <button onClick={() => props.onDelete(props.snack.id)}>delete</button>
        <SnackForm onSubmit={props.onSubmit} snack={props.snack} />
    </>
)
