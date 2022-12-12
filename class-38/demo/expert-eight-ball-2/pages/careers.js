import Link from "next/link";

export default function Careers() {
    return (
        <div className="flex items-center justify-center mx-auto my-8 bg-gray-500 w-72 h-72 text-gray-50">
            <section className="space-y-4">
                <h1 className="text-4xl">Careers Page</h1>
                <Link href="/">
                    <a className="block text-center underline">Return Home</a>
                </Link>
            </section>
        </div>
    );
}
