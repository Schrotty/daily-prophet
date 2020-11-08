const axios = require('axios');

class MediaService {
    fetchMedia() {
        return axios.get('/media/')
    }

    fetchRandom() {
        return axios.get('/media/random/')
    }

    deleteMedia(item) {
        return axios.delete('/media/' + item.id)
    }

    updateMedia(item) {
        return axios.put('/media/' + item.id)
    }
}

export default MediaService