import { createApp } from 'vue'
// import BootstrapVue3 from "bootstrap-vue-3";
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { plugin, defaultConfig } from '@formkit/vue'
import '@formkit/themes/genesis'



axios.defaults.baseURL = 'http://127.0.0.1:8000'
// App.http.options.root = 'http://127.0.0.1:8000/'

const app = createApp(App)
// fsd


app.use(store)
app.use(router)
// app.use(BootstrapVue3)
app.use(VueAxios, axios)
app.use(plugin, defaultConfig)
app.mount('#app')


// app.use(plugin, defaultConfig({
//     config: {
//       classes: {
//         inner: 'form-inputs',
//       }
//     }
//   }))

