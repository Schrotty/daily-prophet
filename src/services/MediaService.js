const axios = require('axios');

class MediaService {
    fetchMedia() {
        return axios.get('/media/')
    }

    deleteMedia(item) {
        return axios.delete('/media/' + item.id)
    }
}

export default MediaService