import Link from 'next/link';

export default function Footer() {
    return (
        <footer className="p-4 mt-8 bg-green-500 text-gray-50">
            <Link href="/careers">Careers</Link>
        </footer>
    );
}
