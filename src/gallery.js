import Vue from 'vue'
import Gallery from './components/Gallery.vue'

import "primevue/resources/themes/saga-orange/theme.css"
import "primevue/resources/primevue.min.css"
import "primeicons/primeicons.css"
import 'primeflex/primeflex.css'

Vue.config.productionTip = false

new Vue({
    render: h => h(Gallery)
}).$mount('#app')