export default function ResponseTable(props) {
    return props.answeredQuestions.length > 0 ? (
        <table className="w-1/2 mx-auto my-4">
            <thead>
                <tr>
                    <th className="border border-gray-700">No.</th>
                    <th className="border border-gray-700">Question</th>
                    <th className="border border-gray-700">Response</th>
                </tr>
            </thead>
            <tbody>
                {props.answeredQuestions.map((item) => {
                    return (
                        <tr key={item.id}>
                            <td className="pl-2 border border-gray-700">
                                {item.id}
                            </td>
                            <td className="pl-2 border border-gray-700">
                                {item.question}
                            </td>
                            <td className="pl-2 border border-gray-700">
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