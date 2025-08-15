import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Home from "../views/Home.vue";
import Reconstruction from "../views/Reconstruction.vue";
import Segmentation from "../views/Segmentation.vue";
import DosePrediction from "../views/Dose-Prediction.vue";
import Quantum from "../views/Quantum.vue";
import About from "../views/About.vue";

const routes = [
  { path: "/", name: "Login", component: Login },
  { path: "/home", name: "Home", component: Home },
  {
    path: "/reconstruction",
    name: "Reconstruction",
    component: Reconstruction,
  },
  { path: "/segmentation", name: "Segmentation", component: Segmentation },
  {
    path: "/dose-prediction",
    name: "DosePrediction",
    component: DosePrediction,
  },
  { path: "/quantum", name: "Quantum", component: Quantum },
  { path: "/about", name: "About", component: About },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.path !== "/" && localStorage.getItem("isLogin") !== "true") {
    next("/");
  } else {
    next();
  }
});

export default router;
