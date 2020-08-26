import Vue from 'vue'
import VueRouter from 'vue-router'
import App from '@/components/App.vue'
import Gallery from '@/components/Gallery.vue'

import Card from 'primevue/card'
import FileUpload from 'primevue/fileupload';
import Carousel from 'primevue/carousel';
import Button from 'primevue/button';
import Toast from 'primevue/toast';
import Dialog from 'primevue/dialog';

import ToastService from 'primevue/toastservice';
import "primevue/resources/themes/saga-orange/theme.css"
import "primevue/resources/primevue.min.css"
import "primeicons/primeicons.css"
import 'primeflex/primeflex.css'

Vue.use(ToastService);
Vue.config.productionTip = false
Vue.component("Card", Card)
Vue.component("FileUpload", FileUpload)
Vue.component("Carousel", Carousel)
Vue.component("Button", Button)
Vue.component("Toast", Toast)
Vue.component("Dialog", Dialog)

Vue.use(VueRouter)
const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', component: App },
        { path: '/gallery', component: Gallery }
    ]
})

/* eslint-disable no-new */
new Vue({
    router
}).$mount('#comp')