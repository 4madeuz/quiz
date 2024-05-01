import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios';
import PrimeVue from 'primevue/config';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from "primevue/button"
import Sidebar from 'primevue/sidebar';
import InputSwitch from 'primevue/inputswitch';
import SelectButton from 'primevue/selectbutton';
import Password from 'primevue/password';
import InputText from 'primevue/inputtext';
import Checkbox from 'primevue/checkbox';
import Card from 'primevue/card';

import { surveyPlugin } from 'survey-vue3-ui'

import App from './App.vue'
import router from './router'
import store from './store';    

import './assets/styles.scss';

const app = createApp(App)

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';  // the FastAPI backend

axios.interceptors.response.use(undefined, function (error) {
  if (error) {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      return router.push('/auth/login')
    }
  }
});

app.use(PrimeVue, { ripple: true });
app.use(store)
app.use(router)
app.use(surveyPlugin)

app.component('Card', Card);
app.component('Checkbox', Checkbox);
app.component('InputText', InputText);
app.component('Password', Password);
app.component('DataTable', DataTable);
app.component('Column', Column);
app.component('Button', Button);
app.component('Sidebar', Sidebar);
app.component('InputSwitch', InputSwitch);
app.component('SelectButton', SelectButton);

app.mount('#app')
