import axios from 'axios'

export async function fetchAll(web=true) {

    // switch between the real and mock here

    if (web) {
        return webFetchAll();
    } else {
        return mockFetchAll();
    }
}

export async function fetchOne(id, web=true) {

    if (web) {
        return webFetchOne(id);
    } else {
        return mockFetchOne(id);
    }
}

function mockFetchAll() {

    return [
        {id: 1, name:"Snickers",description:"Frozen, please"},
        {id: 2, name:"Hummus",description:"Drizzle with olive oil"},
    ]
}

function mockFetchOne(id) {

    const snacks = mockFetchAll();

    for(let snack of snacks) {
        if (snack.id == id) {
            return snack;
        }
    }

    return null;
}


async function webFetchAll() {

    const base = 'https://snacks-circle-back.herokuapp.com'

    try {

        const tokenResponse = await axios.post(base + '/api/token/', {
            username: "jb",
            password: "jb",
        });

        const { refresh, access } = tokenResponse.data;

        const config = {
            headers: { Authorization: `Bearer ${access}` }
        };

        const snacksResponse = await axios.get(base + "/api/v1/snacks/", config);

        return snacksResponse.data

    } catch (error) {
        console.error(error);
    }


    return [];
}

async function webFetchOne(id) {

    const base = 'https://snacks-circle-back.herokuapp.com'

    try {

        const tokenResponse = await axios.post(base + '/api/token/', {
            username: "jb",
            password: "jb",
        });

        const { refresh, access } = tokenResponse.data;

        const config = {
            headers: { Authorization: `Bearer ${access}` }
        };

        const snacksResponse = await axios.get(`${base}/api/v1/snacks/${id}/`, config);

        return snacksResponse.data

    } catch (error) {
        console.error(error);
    }


    return null;
}
