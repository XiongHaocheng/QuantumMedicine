<template>
  <div class="about-page">
    <h1 class="page-title">关于我们</h1>

    <!-- 引入子组件 -->
    <TeamIntroduction />
    <TeamCulture />
    <TeamMembers />
    <TeamHonors />
  </div>
</template>

<script setup>
// 引入子组件
import TeamIntroduction from '@/components/about/TeamIntroduction.vue'
import TeamCulture from '@/components/about/TeamCulture.vue'
import TeamMembers from '@/components/about/TeamMembers.vue'
import TeamHonors from '@/components/about/TeamHonors.vue'

import { onMounted } from 'vue'

onMounted(() => {
  // 平滑滚动到顶部
  window.scrollTo(0, 0)
})
</script>

<style scoped>
/* 页面基础样式 */
.about-page {
  max-width: 1100px;
  margin: 60px auto 0;
  padding: 40px 16px;
}

.page-title {
  text-align: center;
  color: #14203c;
  font-weight: 700;
  font-size: 2.2rem;
  margin-bottom: 32px;
}
</style>
