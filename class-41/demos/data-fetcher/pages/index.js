import axios from 'axios'
import Head from 'next/head'
import styles from '../styles/Home.module.css'

export default function Home({albums}) {
  return (
    <div className={styles.container}>
      <Head>
        <title>Data Fetcher</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Data Fetcher
        </h1>
        <p>{albums.length} albums fetched</p>
        </main>
    </div>
  )
}

export async function getStaticProps() {
    const response = await axios.get('https://jsonplaceholder.typicode.com/albums');
    return {
        props: { albums: response.data },
    }
}

