<template>
  <div class="p-grid">
    <div class="upper-bar p-shadow-4 p-d-flex p-jc-between p-justify-between">
      <a href="#" class="p-d-md-inline-flex">Look I'am a wizard!</a>
      <ul class="p-jc-end">
        <li><a href="#" class="pi pi-plus" v-on:click="$emit('open-uploader')"></a></li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: "UpperControlPanel"
  }
</script>

<style lang="scss" scoped>
  $upper-bar-height: 75px;
  $side-padding: 8px;

  .upper-bar {
    padding-left: $side-padding;
    padding-right: $side-padding;
    height: $upper-bar-height;
    width: 100%;
    background-color: #db401b;
    display: flex;
    position: fixed;
    overflow: hidden;
    z-index: 999;
    top: 0;
    color: white;
  }

  .upper-bar > ul {
    list-style-type: none;
    height: $upper-bar-height;
    padding: 0;
    margin: 0;
    display: flex;
    width: 20%;
    text-align: center;
  }

  .upper-bar > ul > li {
    height: 100%;
    line-height: $upper-bar-height;
  }

  .upper-bar > a,
  .upper-bar > ul > li > a {
    line-height: $upper-bar-height;
    min-width: 60px;
    font-size: 1.5rem;
    height: 100%;
    color: inherit;
    text-decoration: none;
    user-select: none;
    cursor: pointer;
  }

  .upper-bar > ul > li > a:hover {
    border-bottom: 2px solid white;
  }
</style>