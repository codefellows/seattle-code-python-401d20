import Head from 'next/head';
import { useState } from 'react';

export default function Home() {

    const [question, setQuestion] = useState("Ask me anything...");
    const [reply, setReply] = useState("Thinking...")

    function questionAskedHandler(event) {
        event.preventDefault();
        setQuestion(event.target.question.value);
        event.target.reset();
        const randomReply = Math.random() > .5 ? "Yes" : "No";
        setReply(randomReply);
    }

    return (
        <div>
            <Head>
                <title>Expert Eight Ball</title>
            </Head>
            <Header />
            <main className="flex flex-col items-center py-4 space-y-8">
                <QuestionForm onSubmit={questionAskedHandler} />
                <EightBall question={question} />
                <Response reply={reply} />
            </main>
            <Footer copyright="2022" />
        </div>
    )
}

function Header() {
    return (
        <header className='p-4 text-4xl bg-gray-500 text-gray-50'>
            <h1>Expert 8 Ball</h1>
        </header>
    )
}

function Footer(props) {
    return (
        <footer className='p-4 bg-gray-500 text-gray-50'>
            <p>&copy;{props.copyright}</p>
        </footer>
    )
}

function QuestionForm(props) {
    return (
        <form onSubmit={props.onSubmit} className="flex w-1/2 p-2 bg-gray-200">
            <input name="question" className='flex-auto pl-2' type="text" placeholder='Ask me anything...' required />
            <button type="submit" className="px-4 py-2 bg-gray-400 text-gray-50">Ask</button>
        </form>
    );
}

function EightBall(props) {
    return (
        <div className='bg-gray-900 rounded-full w-96 h-96'>
            <div className="relative flex items-center justify-center w-56 h-56 rounded-full top-12 left-12 bg-gray-50">
                <p>{props.question}</p>
            </div>
        </div>
    )
}

function Response(props) {
    return (<h1 className="text-4xl">{props.reply}</h1>)
}

