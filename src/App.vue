
<template>
  <div class="app-container">
    <!-- 顶部 -->
    <Header />

    <!-- 页面主体内容 -->
    <router-view />

    <!-- 底部 -->
    <Footer />
  </div>
</template>


<script setup>
// 引入顶部和底部组件
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
  flex: 1; /* 主体内容占满中间 */
}
</style>
