import Head from 'next/head';
import Header from '../components/Header';
import QuestionForm from '../components/QuestionForm';
import EightBall from '../components/EightBall';
import History from '../components/History';
import Footer from '../components/Footer';
import { replies } from '../data';
import { useState } from 'react';


export default function Home() {

    const [questions, setQuestions] = useState([]);

    function handleQuestion(question) {
        // we need to add the question
        const randIndex = Math.floor(Math.random() * replies.length);
        const answer = replies[randIndex];
        const questionObj = {
            id: questions.length + 1,
            question: question,
            answer: answer,
        };

        setQuestions([...questions, questionObj]);
    }

    function getAnswer() {
        if (questions.length === 0) {
            return "";
        } else {
            return questions[questions.length - 1].answer;
        }
    }

    return (
        <>
            <Head>
                <title>Expert Eight Ball</title>
            </Head>
            <div className='space-y-8'>
                <Header answerCount={questions.length} />
                <main>
                    <QuestionForm onQuestion={handleQuestion} />
                    <EightBall answer={getAnswer()} />
                    <History questionList={questions} />
                </main>
                <Footer />

            </div>
        </>
    );
}











