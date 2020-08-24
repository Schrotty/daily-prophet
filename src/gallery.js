import Vue from 'vue'
import Gallery from './Gallery.vue'

Vue.config.productionTip = false

import Galleria from 'primevue/galleria';
Vue.component("Galleria", Galleria)

import "primevue/resources/themes/saga-orange/theme.css"
import "primevue/resources/primevue.min.css"
import "primeicons/primeicons.css"
import 'primeflex/primeflex.css'

new Vue({
    render: h => h(Gallery)
}).$mount('#app')