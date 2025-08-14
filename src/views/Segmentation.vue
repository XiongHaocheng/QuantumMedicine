<template>
  <div class="reconstruction-page">
    <h1 class="page-title">分割技术</h1>
    <p class="intro">
      图像分割模型可帮助从复杂的医学影像中精准分离出目标区域，如肿瘤或关键器官，为医生提供详细的结构信息。这一技术对于制定放疗计划、保护危及器官、以及评估治疗效果至关重要。
    </p>

  </div>
</template>

<script setup>

import { onMounted } from 'vue'

onMounted(() => {
  // 平滑滚动到顶部
  window.scrollTo(0, 0)
})
</script>

<style scoped>
.reconstruction-page {
  padding: 40px;
  max-width: 1100px;
  margin: auto;
}

.page-title {
  font-size: 2.2rem;
  font-weight: 700;
  margin-bottom: 20px;
  color: #14203c;
}

.intro {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 40px;
  color: #333;
}
</style>
