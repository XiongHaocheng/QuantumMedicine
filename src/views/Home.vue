<template>
  <div>
    <!-- 医疗轮播 -->
    <MedicalCarousel />

    <!-- 模型展示 -->
    <ModelShowcase />

    <!-- 我们的优势 -->
    <WhyChooseUs />
  </div>
</template>

<script setup>
import MedicalCarousel from '../components/index/MedicalCarousel.vue'
import ModelShowcase from '../components/index/ModelShowcase.vue'
import WhyChooseUs from '../components/index/WhyChooseUs.vue'
import { onMounted } from 'vue'

onMounted(() => {
  // 平滑滚动到顶部
  window.scroll(0,0)
})
</script>
