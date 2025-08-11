// main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// 引入 TDesign Vue3 组件库
import TDesign from 'tdesign-vue-next'
import 'tdesign-vue-next/es/style/index.css'

createApp(App)
  .use(TDesign)
  .use(router)
  .mount('#app')
