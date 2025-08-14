import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Reconstruction from '../views/Reconstruction.vue'
import Segmentation from '../views/Segmentation.vue'
import DosePrediction from '../views/Dose-Prediction.vue'
import Quantum from '../views/Quantum.vue'
import About from '../views/About.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/reconstruction', name: 'Reconstruction', component: Reconstruction },
  { path: '/segmentation', name: 'Segmentation', component: Segmentation },
  { path: '/dose-prediction', name: 'DosePrediction', component: DosePrediction },
  { path: '/quantum', name: 'Quantum', component: Quantum },
  { path: '/about', name: 'About', component: About }
]

export default createRouter({
  history: createWebHistory(),
  routes,
  
})
