<template>
  <div id="app">
    <UpperControlPanel v-on:open-uploader="onOpenUploader" />
    <VideoDisplay v-bind:items="items" v-on:activate="onActivateMedia" v-on:open-delete="onOpenDeleteDialog" />

    <!-- TOAST -->
    <Toast position="top-center" />

    <!-- DIALOGS -->
    <Dialog header="Upload New Video" :visible.sync="display" :modal="true" position="center">
      <FileUpload name="media" url="./upload" @upload="onUpload" />
    </Dialog>

    <Dialog v-if="tmpFile !== undefined" header="Delete Media" :visible.sync="displayDeleteDiag" :modal="true" position="center">
      <img v-if="tmpFile.type === 'img'" class="preview-img" :src="'storage/' + tmpFile.filename" :alt="tmpFile.filename">
      <video v-else class="preview-img" :src="'storage/' + tmpFile.filename" :alt="tmpFile.filename" autoplay loop muted></video>
      <template #footer>
        <Button class="p-button-warning" icon="pi pi-times" label="Abort" @click="closeDeleteDialog" />
        <Button class="p-button-danger" icon="pi pi-trash" label="Delete" @click="deleteMedia" />
      </template>
    </Dialog>
  </div>
</template>

<script>
  import UpperControlPanel from "@/components/UpperControlPanel";
  import VideoDisplay from "@/components/VideoDisplay";
  import MediaService from "@/services/MediaService";
  export default {
    name: 'App',
    components: {VideoDisplay, UpperControlPanel},
    data() {
      return {
        mediaService: undefined,
        items: undefined,
        display: false,
        displayDeleteDiag: false,
        tmpFile: undefined,
        tmpFileType: undefined
      }
    },
    created() {
      this.mediaService = new MediaService()
    },
    mounted() {
      this.mediaService.fetchMedia().then(response => (this.items = response.data))
    },
    methods: {
      onOpenUploader: function () {
        this.display = true
      },
      onOpenDeleteDialog: function (item) {
        this.tmpFile = item
        this.displayDeleteDiag = true
      },
      onActivateMedia: function (item) {
        this.mediaService.activateMedia(item)
        location.reload()
      },
      onUpload: function () {
        location.reload()
      },
      closeDeleteDialog() {
        this.displayDeleteDiag = false
      },
      deleteMedia() {
        this.mediaService.deleteMedia(this.tmpFile)
        location.reload()
      }
    }
  }
</script>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Karla&display=swap');

  $upper-bar-height: 75px;
  $background-color: #E8E9E9;

  body {
    font-family: 'Karla', sans-serif;
    background-color: $background-color;
    margin-top: 0;
  }

  a {
    color: inherit;
    text-decoration: none;
    user-select: none;
    cursor: pointer;
  }

  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    margin-top: 0;
  }

  .p-fileupload-buttonbar {
    display: inline-flex;
  }

  .p-card:first-of-type {
    margin-top: $upper-bar-height + 15px;
  }

  #video-display .p-card-content,
  #video-display .p-card-body {
    padding: 5px;
  }

  #app .p-dialog {
    width: 95%;
  }

  .p-dialog-content img,
  .p-dialog-content video {
    width: 100%;
  }
</style>
