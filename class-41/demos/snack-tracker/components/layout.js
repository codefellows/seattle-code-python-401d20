import Head from 'next/head'
import Link from 'next/link'
import styles from '../styles/layout.module.css'

export default function Layout({ children }) {
    return (
        <div className={styles.container}>
      <Head>
        <title>Snack Tracker</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
      <h1 className={styles.title}>
          <Link href="/">
            <a>Snack Tracker</a>
          </Link>
        </h1>
        {children}
      </main>

      <footer className={styles.footer}>
        <p className={styles.red}>We track snacks so you don't have to</p>
      </footer>
    </div>
    )
  }
