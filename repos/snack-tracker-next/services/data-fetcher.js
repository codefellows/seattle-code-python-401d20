import jwt_decode from "jwt-decode";
import axios from 'axios';


export default class DataFetcher {

    constructor(apiUrl) {
        this.apiUrl = apiUrl;
        this.accessTokenKey = this.apiUrl + '-access-token';
        this.refreshTokenKey = this.apiUrl + '-refresh-token';
    }

    async logIn(username, password) {

        const url = this.apiUrl + "token/";

        const response = await axios.post(url, { username, password });

        localStorage.setItem(this.accessTokenKey, response.data.access);
        localStorage.setItem(this.refreshTokenKey, response.data.refresh);

        return true

    }

    logOut() {

        localStorage.setItem(this.accessTokenKey, undefined);
        localStorage.setItem(this.refreshTokenKey, undefined);
    }

    async fetchAccessToken() {

        let accessToken = localStorage.getItem(this.accessTokenKey);

        if (!this.tokenIsFresh(accessToken)) {
            accessToken = await this.refreshToken();
            localStorage.setItem(this.accessTokenKey, accessToken);
        }

        return accessToken;

    }

    tokenIsFresh(accessToken) {

        if (!accessToken) return false;

        let decodedToken = jwt_decode(accessToken);

        let currentDate = new Date();

        // JWT exp is in seconds
        if (decodedToken.exp * 1000 < currentDate.getTime()) {
            console.log("Token expired.");
            return false;
        } else {
            return true;
        }
    }

    async refreshToken() {

        let url = this.apiUrl + "token/refresh/";

        const refresh = localStorage.getItem(REFRESH_TOKEN_KEY);

        if (refresh) {

            const response = await axios.post(url, { refresh });

            let JWTToken = response.data.access;

            return JWTToken;

        } else {

            return null;
        }
    }



    async fetchResource(noun, id = null) {

        try {

            const JWTToken = await this.fetchAccessToken();

            let url = `${this.apiUrl}${noun}/`;

            if (id != null) {
                url += `${id}/`;
            }

            let config = { headers: { "Authorization": `Bearer ${JWTToken}` } };

            let response = await axios.get(url, config);

            return response.data;

        } catch (e) {

            console.error("Failed to fetch series data")

            return []
        }
    }
}
