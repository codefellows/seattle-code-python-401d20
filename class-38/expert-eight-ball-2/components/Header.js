export default function Header(props) {
  return (
    <header className='flex items-center justify-between p-4 bg-gray-500 text-gray-50'>
      <h1>Expert 8 Ball</h1>
      <p>{answeredQuestions.length} questions answered</p>
    </header>
  );
}
