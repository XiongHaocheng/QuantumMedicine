<template>
  <div class="app-container">
    <!-- 顶部导航 -->
    <Header />

    <!-- 页面主体内容（不同路由切换） -->
    <router-view />

    <!-- 底部 -->
    <Footer />
  </div>
</template>

<script setup>
import Header from './component/Header.vue'
import Footer from './component/Footer.vue'
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
  overflow-x: hidden;
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
