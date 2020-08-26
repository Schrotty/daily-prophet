<template>
  <div id="video-display" v-if="items !== undefined  && items.length > 0">
    <template v-for="item in items" >
      <Card :key="item.id">
        <template slot="content">
          <div class="p-grid">
            <div class="p-col-12">
              <img v-if="item.type === 'image'" class="preview-img" :src="'storage/' + item.filename" :alt="item.filename">
              <video v-if="item.type === 'video'" class="preview-img" :src="'storage/' + item.filename" :alt="item.filename" autoplay loop muted>
                Your browser doesn't support embedded videos!
              </video>
            </div>

            <div class="p-col-12">
              <Button v-bind:disabled="item.selected" label="Delete" class="p-button-danger" icon="pi pi-trash" v-on:click="$emit('open-delete', item)"></Button>
            </div>
          </div>
        </template>
      </Card>
    </template>
  </div>
  <div v-else>
    <Card>
      <template slot="title">Nothing here to show!</template>
      <template slot="content">Upload files to see them displayed here!</template>
    </Card>
  </div>
</template>

<script>
  export default {
    name: "VideoDisplay",
    props: ['items']
  }
</script>

<style lang="scss" scoped>
  .p-card {
    width: 100%;
    margin-bottom: 8px;
  }

  .p-card > .p-card-content {
    padding: 0;
  }

  .p-button {
    width: 100%;
    text-align: center;
  }

  .preview-img {
    width: 100%;
  }
</style>