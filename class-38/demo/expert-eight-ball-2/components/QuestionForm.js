export default function QuestionForm({ onQuestion }) {

    function handleSubmit(event) {
        event.preventDefault();
        onQuestion(event.target.question.value);
        event.target.reset();
    }
    return (
        <form onSubmit={handleSubmit} className="flex w-1/2 p-4 mx-auto my-4 bg-gray-200">
            <input name="question" className="flex-auto pl-2" placeholder="Ask Me Anything" required />
            <button className="px-3 py-2 bg-gray-500 text-gray-50">Ask</button>
        </form>
    );
}

