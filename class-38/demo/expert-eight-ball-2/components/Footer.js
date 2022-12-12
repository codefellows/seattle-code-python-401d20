import Link from 'next/link';

export default function Footer() {
    return (
        <footer className='p-4 bg-gray-500 text-gray-50'>
            <Link href={'/careers'}>
                <a className="px-3 py-2 bg-gray-700 rounded-lg">Careers</a>
            </Link>
        </footer>
    );
}
