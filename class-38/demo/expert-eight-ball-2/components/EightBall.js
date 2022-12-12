export default function EightBall({ answer }) {
    return (
        <div className="mx-auto bg-black rounded-full w-96 h-96">
            <div className="relative flex items-center justify-center w-48 h-48 bg-white rounded-full left-16 top-16">
                <p className="text-xl">{answer || 'Waiting...'}</p>
            </div>
        </div>
    );
}
