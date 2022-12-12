import React from 'react'
import { Link } from "react-router-dom"

import SnackForm from './SnackForm'


export default props => (
    <>
        <h2>Snack List</h2>
        <ul>
            {props.snacks.map(snack => <SnackItem key={snack.id} snack={snack} />)}
        </ul>
        <SnackForm onSubmit={props.onSubmit} />
    </>
)

const SnackItem = props => (
    <li>
        <Link to={`/${props.snack.id}`}>
            <p>
                {props.snack.title}
            </p>
        </Link>
    </li>
)
