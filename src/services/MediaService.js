const axios = require('axios');

class MediaService {
    fetchMedia() {
        return axios.get('/media')
    }

    deleteMedia(item) {
        console.log(item)
        axios.delete('/media/' + item.id).then(function (response) {
            console.log(response)
        }).catch(function (error) {
            console.log(error)
        })
    }
}

export default MediaService