import { fetchOne } from '../../services/fetcher'
import Layout from '../../components/layout'


const SnackDetail = ({ snack }) => (

    <Layout>
        <h2>{snack && snack.name}</h2>
        <p>{snack && snack.description}</p>
        <ul>
            <li>Just</li>
            <li>Showing</li>
            <li>Off</li>
            <li>Isolated</li>
            <li>Styling</li>
        </ul>
    </Layout>
)

export default SnackDetail;

/*
export async function getStaticPaths() {
    return {
        // Only `/snacks/1` and `/snacks/2` are generated at build time
        paths: [{ params: { id: '1' } }, { params: { id: '2' } }],
        // Enable statically generating additional pages
        // For example: `/snacks/3`
        fallback: true,
    }
}

export async function getStaticProps(context) {

    // const id = context.query.id;
    const id = context.params.id;

    const snack = await fetchOne(id);

    return {
        props: {
            snack,
        },
        // Next.js will attempt to re-generate the page:
        // - When a request comes in
        // - At most once every second
        revalidate: 1, // In seconds
    }
}
//*/

//*
export async function getServerSideProps(context) {

    const id = context.query.id;

    const snack = await fetchOne(id);

    return {
        props: {
            snack,
        },
    }
}
//*/
