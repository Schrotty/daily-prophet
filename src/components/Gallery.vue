<template>
  <div id="app" v-if="image !== null && image !== undefined">
    <div :style="{ backgroundImage: 'url(\'storage/' + image.filename + '\')' }" class="bg"
         v-if="image.type === 'image'"></div>
    <video :alt="image.filename" :src="'storage/' + image.filename" autoplay loop muted ref="player" v-else></video>
  </div>
</template>

<script>
import MediaService from "@/services/MediaService";

export default {
  name: "Gallery",
  data() {
    return {
      image: null,
      mediaService: undefined,
      duration: 5,
      timer: ''
    }
  },
  created() {
    this.mediaService = new MediaService()
    this.timer = setInterval(this.fetchRandom, 3000)
  },
  mounted() {
    this.fetchRandom()
  },
  methods: {
    fetchRandom() {
      this.mediaService.fetchRandom().then(response => {
        clearInterval(this.timer)
        if (this.image === null) {
          this.image = response.data
        }

        if (this.image !== response.data) {
          this.image = response.data
        }

        if (this.image !== null) {
          this.duration = this.image.duration
        }

        this.timer = setInterval(this.fetchRandom, (this.duration * 1000))
      }).catch(() => {
        clearInterval(this.timer)
        this.timer = setInterval(this.fetchRandom, (30 * 1000))
      })
    }
  }
}
</script>

<style scoped lang="scss">
  #app {
    position: absolute;
    background-color: black;
    width: 100%;
    height: 100%;
  }

  video {
    width: 100vw;
    height: 100vh;
  }

  .p-galleria-item {
    height: 100vh;
    width: 100%;
  }

  .bg {
    /* Full height */
    height: 100vh;
    width: 100vw;

    /* Center and scale the image nicely */
    background-position: center;
    background-repeat: no-repeat;
    background-size: contain;
    position: relative;
  }
</style>