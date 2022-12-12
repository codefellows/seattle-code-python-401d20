import React from 'react'
import './Plane.css'

class Plane extends React.Component {

    constructor(props) {

        super(props);

        this.state = {
            player: {
                x_pos: 4,
                y_pos: 3,
            },
            rows: [[
                {
                    cell_type: 'entrance',
                    x_pos: 0,
                    y_pos: 0,
                },
                {
                    cell_type: 'aisle',
                },
                {
                    cell_type: 'aisle',
                },
                {
                    cell_type: 'aisle',
                },
                {
                    cell_type: 'aisle',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'wall',
                },
            ],[
                {
                    cell_type: 'wall',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'aisle',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'wall',
                },
            ],[
                {
                    cell_type: 'wall',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'aisle',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'wall',
                },
            ],[
                {
                    cell_type: 'wall',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                    x_pos: 4,
                    y_pos: 3,
                },
                {
                    cell_type: 'aisle',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'seat',
                },
                {
                    cell_type: 'wall',
                },
            ]]
        }
    }


    /**
     * API data like this
     * [{x_pos:0,y_pos:0}....] all in one array (order gauranteed????)
     * We want ideally in nested arrays
     */
    renderRows() {

        const rowsToRender = []

        for (let row of this.state.rows) {

            let cellsToRender = row.map(cell => {

                let className = 'Cell ' + cell.cell_type;

                if (cell.x_pos === this.state.player.x_pos &&
                    cell.y_pos === this.state.player.y_pos) {
                        className += ' player'
                    }


                return <div className={className}>{cell.cell_type}</div>
            })

            rowsToRender.push(cellsToRender);

        }

        return rowsToRender;
    }

 


    render() {
        return (<div className="Plane">
            {this.renderRows()}
        </div>)
    }
}

export default Plane