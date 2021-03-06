<template>
  <div id="app">
    <UpperControlPanel v-on:open-uploader="onOpenUploader" />
    <VideoDisplay v-bind:items="items" v-on:open-delete="onOpenDeleteDialog" v-on:update-status="updateStatus" />

    <!-- TOAST -->
    <Toast position="top-center" />

    <!-- DIALOGS -->
    <Dialog header="Upload New" :visible.sync="display" :modal="true" position="center">
      <FileUpload accept="image/*, video/*" name="file[]" :multible="true" url="media/" uploadLabel="" cancelLabel="" @upload="onUpload" @error="onError"/>
    </Dialog>

    <Dialog v-if="tmpFile !== undefined" header="Delete Media" :visible.sync="displayDeleteDiag" :modal="true" position="center">
      <img v-if="tmpFile.type === 'image'" class="preview-img" :src="'storage/' + tmpFile.filename" :alt="tmpFile.filename">
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
      this.fetchData()
    },
    methods: {
      fetchData() {
        this.mediaService.fetchMedia().then(response => (this.items = response.data))
      },
      onOpenUploader: function () {
        this.display = true
      },
      onOpenDeleteDialog: function (item) {
        this.tmpFile = item
        this.displayDeleteDiag = true
      },
      onUpload: function () {
        this.fetchData()
        this.display = false
      },
      onError: function (e) {
        this.$toast.add({severity:'error', summary: e.xhr.status + ' ' + e.xhr.statusText, detail: "Backend not available!", life: 3000});
      },
      closeDeleteDialog() {
        this.displayDeleteDiag = false
      },
      deleteMedia() {
        this.mediaService.deleteMedia(this.tmpFile).then(response => (this.items = response.data))
        this.closeDeleteDialog()
      },
      updateStatus: function (item) {
        this.mediaService.updateMedia(item).then(response => (this.items = response.data))
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
    background-color: $background-color !important;
    margin: 0;
    padding: 0;
  }

  a {
    color: inherit;
    text-decoration: none;
    user-select: none;
    cursor: pointer;
  }
  .p-fileupload-buttonbar {
    width: 100%;
  }

  .p-fileupload .p-fileupload-buttonbar .p-button  {
    height: 40px;
    min-width: 40px;
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

  #app > .p-toast-top-center {
    left: 0;
    margin-left: 0.4rem;
  }
</style>

<style scoped>
  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    margin-top: 0;
    padding: 8px;
  }
</style>
