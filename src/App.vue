<template>
  <div class="app-container">
    <!-- 只在非登录页显示头部和底部 -->
    <Header v-if="$route.path !== '/'" />
    <router-view />
    <Footer v-if="$route.path !== '/'" />
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
const $route = useRoute()
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

router-view {
  flex: 1;
}
</style>

<style>
html,
body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  background: #ffffff;
}

#app {
  width: 100%;
  min-height: 100vh;
  overflow-x: hidden;
}

/* 隐藏 Vue Devtools 浮动按钮 */
div[id^="vue-devtools"],
div[class*="vue-devtools"],
div[id^="__VUE"],
#__VUE_DEVTOOLS_TOAST__ {
  display: none !important;
}
</style>
