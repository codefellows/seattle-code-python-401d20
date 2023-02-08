export default function QuestionForm({ questionAskedHandler }) {
    return (
        <form
            className="flex w-1/2 p-2 mx-auto my-4 bg-gray-200"
            onSubmit={props.questionAskedHandler}
        >
            <input name="question" className="flex-auto pl-1" />
            <button className="px-2 py-1 bg-gray-500 text-gray-50">Ask</button>
        </form>
    );
}
