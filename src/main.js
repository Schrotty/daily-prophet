import Vue from 'vue'
import App from './App.vue'

import Card from 'primevue/card'
import FileUpload from 'primevue/fileupload';
import Carousel from 'primevue/carousel';
import Button from 'primevue/button';
import Toast from 'primevue/toast';
import Dialog from 'primevue/dialog';

import ToastService from 'primevue/toastservice';

Vue.use(ToastService);
Vue.config.productionTip = false
Vue.component("Card", Card)
Vue.component("FileUpload", FileUpload)
Vue.component("Carousel", Carousel)
Vue.component("Button", Button)
Vue.component("Toast", Toast)
Vue.component("Dialog", Dialog)

import "primevue/resources/themes/saga-orange/theme.css"
import "primevue/resources/primevue.min.css"
import "primeicons/primeicons.css"
import 'primeflex/primeflex.css'

new Vue({
  render: h => h(App)
}).$mount('#app')