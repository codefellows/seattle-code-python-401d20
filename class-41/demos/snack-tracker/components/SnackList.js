import Link from 'next/link'
import styles from '../styles/snack-list.module.css'

function SnackList({ snacks }) {
    return (<ul className={styles.snackList}>
        {snacks.map(snack => (
            <SnackItem key={snack.id} snack={snack} />
        ))}
    </ul>
    )
}

function SnackItem({ snack }) {
    return (
        <li>
            <Link href="/snacks/[id].js" as={`/snacks/${snack.id}`}>
                <a>
                    {snack.name}
                </a>
            </Link>
        </li>
    )
}

export default SnackList;
