
import axios from 'axios';

const isAuthenticated = () => axios.get('checksession')
    .then(response => {
        return response.data
    })
    .catch(function (error) {
        console.log(error)
    });


export { isAuthenticated }