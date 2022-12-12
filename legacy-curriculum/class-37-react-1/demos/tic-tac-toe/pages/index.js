import Head from 'next/head'
import { useState } from 'react'

export default function Home() {

    const emptyBoard = [
        [null, null, null],
        [null, null, null],
        [null, null, null],
    ]

    const [board, setBoard] = useState(emptyBoard);

    const [mover, setMover] = useState('X');

    function turnTakenHandler(row, column) {

        if (board[row][column]) return;

        const updatedBoard = [...board];

        updatedBoard[row][column] = mover;

        setBoard(updatedBoard);

        setMover(mover === 'X' ? 'O' : 'X');

        const winner = victoryCheck();

        if (winner) {
            alert(winner);
        }

    }

    function hasThreeInRow(squares) {
        const [a, b, c] = squares;
        if (a && a === b && a === c) {
            return a;
        }
    }

    function victoryCheck() {

        let values, winner = null;

        // go through rows
        for (let row of board) {
            values = row;
            winner = hasThreeInRow(values);
            if (winner) {
                return winner;
            }
        }

        // go through columns
        for (let i in [0, 1, 2]) {
            values = [board[0][i], board[1][i], board[2][i]];
            winner = hasThreeInRow(values);
            if (winner) {
                return winner;
            }
        }

        // top left diagonal
        values = [board[0][0], board[1][1], board[2][2]];
        winner = hasThreeInRow(values);
        if (winner) {
            return winner;
        }

        // top right diagonal
        values = [board[0][2], board[1][1], board[2][0]];
        winner = hasThreeInRow(values);
        if (winner) {
            return winner;
        }

        return null;

    }

    return (
        <div className="">
            <Head>
                <title>Tic Tac Toe</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <main>
                <h1 className="p-4 text-4xl font-bold text-center">Tic Tac Toe</h1>

                <section className="grid w-1/2 grid-cols-3 grid-rows-3 gap-4 mx-auto bg-red-500 place-content-center h-96">
                    {
                        board.map((row, rowIndex) => {
                            return row.map((column, columnIndex) => (
                                <Cell
                                    key={rowIndex + '' + columnIndex}
                                    row={rowIndex}
                                    column={columnIndex}
                                    value={column}
                                    onTurnTaken={turnTakenHandler}
                                />
                            ))

                        })
                    }
                </section>
            </main>
        </div>
    )
}

function Cell({ row, column, onTurnTaken, value }) {

    return (
        <div onClick={() => onTurnTaken(row, column)} className="flex items-center justify-center h-full text-4xl font-bold text-green-800 bg-red-100">{value}</div>
    )
}
