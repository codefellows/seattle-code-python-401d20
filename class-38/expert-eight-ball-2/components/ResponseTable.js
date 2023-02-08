export default function ResponseTable({ answeredQuestions, tableHeaders }) {
    return answeredQuestions.length > 0 ? (
        <table className="w-1/2 mx-auto my-4">
            <thead>
                <tr>
                    {tableHeaders.map((item, idx) =>
                        answeredQuestions.length % 2 == 0 ? (
                            <th className="border border-blue-700" key={idx}>
                                {item}
                            </th>
                        ) : (
                            <th className="border border-red-700" key={idx}>
                                {item}
                            </th>
                        )
                    )}
                </tr>
            </thead>
            <tbody>
                {answeredQuestions.map((item) => {
                    if (answeredQuestions.length % 2 == 0) {
                        const color = "blue";
                    } else {
                        const color = "red";
                    }

                    return (
                        <tr key={item.id}>
                            <td className="pl-2 border border--700">
                                {item.id}
                            </td>
                            <td className="pl-2 border border--700">
                                {item.question}
                            </td>
                            <td className="pl-2 border border--700">
                                {item.reply}
                            </td>
                        </tr>
                    );
                })}
            </tbody>
        </table>
    ) : (
        <h1 className="text-center text-4xl">No Questions Asked Yet</h1>
    );
}
