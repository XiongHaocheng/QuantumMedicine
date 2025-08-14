<template>
  <div class="carousel-bg">
    <div v-for="(img, idx) in images" :key="idx" :class="[
      'carousel-img',
      {
        current: idx === currentIndex,
        prev: idx === lastIndex,
        'slide-in-from-right': !isFirstRender && slideDirection === 'right' && idx === currentIndex,
        'slide-in-from-left': !isFirstRender && slideDirection === 'left' && idx === currentIndex,
        'slide-out-to-left': !isFirstRender && slideDirection === 'right' && idx === lastIndex,
        'slide-out-to-right': !isFirstRender && slideDirection === 'left' && idx === lastIndex,
      }
    ]" :style="{ backgroundImage: `url(${img.url})` }"></div>

    <div class="carousel-overlay">
      <!-- 左箭头 -->
      <div class="carousel-arrow left" @click="prevImage">&#10094;</div>
      <!-- 右箭头 -->
      <div class="carousel-arrow right" @click="nextImage">&#10095;</div>

      <div class="carousel-caption">
        <Transition name="fade-caption" mode="out-in">
          <h1 :key="images[currentIndex].caption">{{ images[currentIndex].caption }}</h1>
        </Transition>
      </div>

      <div class="carousel-indicators">
        <span v-for="(img, idx) in images" :key="idx" :class="{ active: idx === currentIndex }"
          @click="goToImage(idx)"></span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'

const images = [
  {
    url: new URL('@/assets/home1.png', import.meta.url).href,
    alt: '量子医疗1',
    caption: '量子计算 · 引领医疗创新',
  },
  {
    url: new URL('@/assets/home2.png', import.meta.url).href,
    alt: '量子医疗2',
    caption: '量子医疗 · 智能健康新纪元',
  },
  {
    url: new URL('@/assets/home3.png', import.meta.url).href,
    alt: '量子医疗3',
    caption: '智慧医疗 · 商业化量子解决方案',
  },
]

const currentIndex = ref(0)
const lastIndex = ref(-1)
const slideDirection = ref('right')
const isFirstRender = ref(true) // 新增

let timer = null

function goToImage(idx) {
  if (idx === currentIndex.value) return
  slideDirection.value = idx > currentIndex.value ? 'right' : 'left'
  lastIndex.value = currentIndex.value
  currentIndex.value = idx
}

function nextImage() {
  slideDirection.value = 'right'
  lastIndex.value = currentIndex.value
  currentIndex.value = (currentIndex.value + 1) % images.length
  if (!initialized.value) initialized.value = true
}

function prevImage() {
  slideDirection.value = 'left'
  lastIndex.value = currentIndex.value
  currentIndex.value = (currentIndex.value - 1 + images.length) % images.length
  if (!initialized.value) initialized.value = true
}

onMounted(() => {
  timer = setInterval(nextImage, 4000)
  nextTick(() => {
    isFirstRender.value = false // 首次渲染后关闭首次标志
  })
})

onUnmounted(() => {
  clearInterval(timer)
})
</script>
<style scoped>
.carousel-bg {
  width: 100vw;
  height: 100vh;
  background-color: #14203c;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.carousel-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-size: cover;
  background-position: center;
  opacity: 0;
  pointer-events: none;
  z-index: 1;
}

/* 当前显示图片 */
.carousel-img.current {
  opacity: 1;
  pointer-events: auto;
  z-index: 3;
  transform: translateX(0);
  transition: none;
}

/* 上一张图片 */
.carousel-img.prev {
  pointer-events: none;
  z-index: 2;
}

/* 右切换：新图从右进 */
.carousel-img.slide-in-from-right {
  animation: slideInFromRight 0.6s forwards;
  opacity: 1;
  pointer-events: auto;
  z-index: 3;
}

/* 左切换：新图从左进 */
.carousel-img.slide-in-from-left {
  animation: slideInFromLeft 0.6s forwards;
  opacity: 1;
  pointer-events: auto;
  z-index: 3;
}

/* 右切换：旧图向左出 */
.carousel-img.slide-out-to-left {
  animation: slideOutToLeft 0.6s forwards;
  opacity: 1;
  pointer-events: none;
  z-index: 2;
}

/* 左切换：旧图向右出 */
.carousel-img.slide-out-to-right {
  animation: slideOutToRight 0.6s forwards;
  opacity: 1;
  pointer-events: none;
  z-index: 2;
}

@keyframes slideInFromRight {
  from {
    transform: translateX(100%);
  }

  to {
    transform: translateX(0);
  }
}

@keyframes slideInFromLeft {
  from {
    transform: translateX(-100%);
  }

  to {
    transform: translateX(0);
  }
}

@keyframes slideOutToLeft {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-100%);
    opacity: 0;
  }
}

@keyframes slideOutToRight {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(100%);
    opacity: 0;
  }
}

/* 其他覆盖样式保持不变 */
.carousel-overlay {
  width: 100vw;
  height: 100vh;
  background: rgba(10, 24, 48, 0.55);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: 0;
  left: 0;
  pointer-events: none;
}

.carousel-caption {
  color: #fff;
  text-align: center;
  font-size: 2.8rem;
  font-weight: 700;
  letter-spacing: 2px;
  text-shadow: 0 4px 32px rgba(0, 0, 0, 0.4);
  margin-bottom: 60px;
  min-height: 3.5em;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: auto;
  z-index: 10;
  position: relative;
}

.carousel-indicators {
  position: absolute;
  bottom: 48px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  gap: 18px;
  pointer-events: auto;
  z-index: 20;
}

.carousel-indicators span {
  display: inline-block;
  width: 18px;
  height: 18px;
  background: #fff;
  border-radius: 50%;
  cursor: pointer;
  border: 2px solid #1976d2;
  opacity: 1;
  transition: none;
}

.carousel-indicators .active {
  background: #1976d2;
}

.carousel-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-size: 32px;
  color: white;
  cursor: pointer;
  z-index: 30;
  width: 56px;
  /* 新增：固定宽高 */
  height: 56px;
  /* 新增：固定宽高 */
  background: rgba(0, 0, 0, 0.3);
  border-radius: 50%;
  /* 新增：圆形 */
  pointer-events: auto;
  transition: background 0.3s;
  display: flex;
  /* 新增：居中内容 */
  align-items: center;
  /* 新增：垂直居中 */
  justify-content: center;
  /* 新增：水平居中 */
  border: 2px solid #fff;
  /* 可选：加个白色边框更明显 */
  box-sizing: border-box;
  /* 防止边框撑大 */
  padding: 0;
  /* 去除原有内边距 */
}

.carousel-arrow:hover {
  background: rgba(0, 0, 0, 0.6);
}

.carousel-arrow.left {
  left: 20px;
}

.carousel-arrow.right {
  right: 20px;
}

/* fade-caption 动画保持不变 */
.fade-caption-enter-active,
.fade-caption-leave-active {
  transition: opacity 0.1s, filter 0.1s;
}

.fade-caption-enter-from,
.fade-caption-leave-to {
  opacity: 0;
  filter: blur(12px);
}

.fade-caption-enter-to,
.fade-caption-leave-from {
  opacity: 1;
  filter: blur(0px);
}
</style>
