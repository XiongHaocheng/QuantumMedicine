<template>
  <div class="reconstruction-page">
    <h1 class="page-title">剂量预测技术</h1>
    <p class="intro">
      该模型结合临床需求进行剂量预测，帮助提高治疗效率，并降低辐射风险。它能够在低剂量成像条件下，快速进行高质量的影像重建与精准的分割与剂量预测，进一步提升治疗效果的精确度。
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
