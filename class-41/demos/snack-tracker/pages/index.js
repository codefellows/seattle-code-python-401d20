import {fetchAll} from '../services/fetcher'
import Layout from '../components/layout'
import SnackList from '../components/SnackList'
import SnackCounter from '../components/SnackCounter'

function Home({snacks}) {
  return (
      <Layout>
        <SnackCounter count={snacks.length} />
        <SnackList snacks={snacks} />
      </Layout>

  )
}

export async function getStaticProps() {
    const snacks = await fetchAll();

    return {
        props: { snacks },
        revalidate: 1,
    }

}

export default Home;
