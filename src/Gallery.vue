<template>
  <div id="app">
    <Galleria :value="images" :numVisible="5" :circular="true" :autoPlay="true" :transitionInterval="30000" :showThumbnails="false">
      <template #item="slotProps">
        <div class="bg" :style="{ backgroundImage: 'url(\'../storage/' + slotProps.item.filename + '\')' }"></div>
      </template>
    </Galleria>
  </div>
</template>

<script>
import MediaService from "@/services/MediaService";

export default {
  name: "Gallery",
  data() {
    return {
      images: undefined,
      mediaService: undefined,
      timer: ''
    }
  },
  created() {
    this.mediaService = new MediaService()
    this.timer = setInterval(this.fetchMedia, 300000)
  },
  mounted() {
    this.fetchMedia()
  },
  methods: {
    fetchMedia() {
      this.mediaService.fetchMedia().then(response => {
        if (this.images === undefined) {
          this.images = response.data
        }

        if (this.images !== response.data) {
          this.images = response.data
        }
      })
    }
  }
}
</script>

<style lang="scss">
  html, body {
    height: 100%;
  }

  body {
    margin: 0;
    padding: 0;
    background-color: black;
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