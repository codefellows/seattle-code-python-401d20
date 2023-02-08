export default function Header({ answeredQuestions, name, color }) {
    return (
        <header className={`flex items-center justify-between p-4 bg-${color}-500 text-gray-50`}>
            <h1>Expert 8 Ball</h1>
            <p>{answeredQuestions.length} questions answered</p>
            <p>{name}</p>
        </header>
    );
}
