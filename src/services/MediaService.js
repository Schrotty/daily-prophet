const axios = require('axios');

class MediaService {
    fetchMedia() {
        return axios.get('/media')
    }

    deleteMedia(item) {
        axios.delete('/media', {
            data: {
                id: item.filename
            }
        }).then(function (response) {
            console.log(response)
        }).catch(function (error) {
            console.log(error)
        })
    }

    activateMedia(item) {
        axios.put('/activate', {
            id: item.filename
        }).then(function (response) {
            console.log(response)
        }).catch(function (error) {
            console.log(error)
        })
    }
}

export default MediaService