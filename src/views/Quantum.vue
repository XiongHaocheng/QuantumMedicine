<template>
  <!-- 动态背景容器（底层） -->
  <div class="gradient-bg">
    <!-- SVG噪声背景 -->
    <svg 
      viewBox="0 0 100vw 100vw"
      xmlns='http://www.w3.org/2000/svg'
      class="noiseBg"
    >
      <filter id='noiseFilterBg'>
        <feTurbulence 
          type='fractalNoise'
          baseFrequency='0.6'
          stitchTiles='stitch' />
      </filter>
      <rect
        width='100%'
        height='100%'
        preserveAspectRatio="xMidYMid meet"
        filter='url(#noiseFilterBg)' />
    </svg>

    <!-- 模糊滤镜定义 -->
    <svg xmlns="http://www.w3.org/2000/svg" class="svgBlur">
      <defs>
        <filter id="goo">
          <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur" />
          <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -8" result="goo" />
          <feBlend in="SourceGraphic" in2="goo" />
        </filter>
      </defs>
    </svg>

    <!-- 渐变光斑容器 -->
    <div class="gradients-container">
      <div class="g1"></div>
      <div class="g2"></div>
      <div class="g3"></div>
      <div class="g4"></div>
      <div class="g5"></div>
      <div class="interactive" ref="interactiveRef"></div> <!-- 绑定ref用于JS控制 -->
    </div>

    <!-- 原有量子介绍内容（上层） -->
    <div class="Quantum-page">
      <!-- 模块列表（原卡片内容） -->
      <div class="module" v-for="(item, index) in modules" :key="index" ref="modulesRef" style="margin-top: 80px;">
        <div class="banner">
          <p class="banner-text">{{ item.title }}</p>
        </div>

        <div class="content-center">
          <div class="colored-bar"></div>

          <div class="card-container">
            <!-- 偶数行反转顺序 -->
            <template v-if="index % 2 === 1">
              <div class="card slide-left">
                <div class="card-right">
                  <div class="row1">
                    <p class="row1-text">{{ item.cardTitle }}</p>
                    <img class="right-icon" src="../assets/logo.png" alt="图标" />
                  </div>
                  <hr class="card-line" />
                  <div class="row3">{{ item.content }}</div>
                </div>
              </div>
              <img class="card-left slide-right" :src="item.img" alt="图片" />
            </template>

            <!-- 其他行布局 -->
            <template v-else>
              <img class="card-left slide-left" :src="item.img" alt="图片" />
              <div class="card slide-right">
                <div class="card-right">
                  <div class="row1">
                    <p class="row1-text">{{ item.cardTitle }}</p>
                    <img class="right-icon" src="../assets/logo.png" alt="图标" />
                  </div>
                  <hr class="card-line" />
                  <div class="row3">{{ item.content }}</div>
                </div>
              </div>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ChinaMobileImg from '../assets/ChinaMobile.png'
import ReconstructionImg from '../assets/reconstruction.png'
import Segmentation from '../assets/Segmentation.png'
import DosePrediction from '../assets/DosePrediction.png'

// 量子模块数据（保持不变）
const modules = [
  {
    title: '移动云量子平台',
    img: ChinaMobileImg,
    cardTitle: '移动云-量子计算云平台',
    content: '移动云量子计算云平台是融合了经典算力和量子算力的全栈量子计算云服务系统...'
  },
  {
    title: '重建技术',
    img: ReconstructionImg,
    cardTitle: '重建技术',
    content: '生成器U-Net潜空间和判别器中间层均嵌入量子增强模块...'
  },
  {
    title: '分割技术',
    img: Segmentation,
    cardTitle: '分割技术',
    content: '该模型基于VGG16-UNet结构，编码器提取多尺度特征并可利用预训练权重加速训练...'
  },
  {
    title: '剂量预测技术',
    img: DosePrediction,
    cardTitle: '剂量预测技术',
    content: '为充分利用医学关键先验信息，我们提出MPDCL方法...'
  }
]

// 动态背景交互相关
const interactiveRef = ref(null) // 绑定交互光斑元素
const modulesRef = ref([]) // 原滚动动画元素

onMounted(() => {
  window.scrollTo(0, 0);

  // 1. 原滚动动画逻辑（保持不变）
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const img = entry.target.querySelector('.card-left')
        const card = entry.target.querySelector('.card')
        if (entry.isIntersecting) {
          img.classList.add('visible')
          card.classList.add('visible')
        } else {
          img.classList.remove('visible')
          card.classList.remove('visible')
        }
      })
    },
    { threshold: 0.2 }
  )
  modulesRef.value.forEach((module) => observer.observe(module))

  // 2. 动态背景鼠标跟随逻辑
  if (interactiveRef.value) {
    let curX = 0
    let curY = 0
    let tgX = 0
    let tgY = 0

    // 光斑移动动画
    const move = () => {
      curX += (tgX - curX) / 20
      curY += (tgY - curY) / 20
      interactiveRef.value.style.transform = `translate(${Math.round(curX)}px, ${Math.round(curY)}px)`
      requestAnimationFrame(move)
    }

    // 监听鼠标移动
    window.addEventListener('mousemove', (event) => {
      tgX = event.clientX
      tgY = event.clientY
    })

    // 启动动画
    move()
  }
})
</script>

<style>
/* 动态背景核心样式 */
:root {
  --color-bg1: rgb(8, 10, 15);
  --color-bg2: rgb(0, 17, 32);
  --color1: 18, 113, 255;
  --color2: 107, 74, 255;
  --color3: 100, 100, 255;
  --color4: 50, 160, 220;
  --color5: 80, 47, 122;
  --color-interactive: 140, 100, 255;
  --circle-size: 80%;
  --blending: hard-light;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  color: #FFF;
  background: transparent;
  border: none;
}

html, body {
  height: 100%;
  width: 100%;
  overflow-x: hidden; /* 避免横向滚动 */
}

/* 动态背景容器 */
.gradient-bg {
  width: 100vw;
  min-height: 100vh; /* 适应内容高度 */
  position: relative;
  background: linear-gradient(40deg, var(--color-bg1), var(--color-bg2));
  overflow: hidden;
}

.gradient-bg .svgBlur {
  display: none; /* 滤镜定义不显示，仅用于引用 */
}

.gradient-bg .noiseBg {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 1;
  mix-blend-mode: soft-light;
  opacity: 0.3;
}

.gradient-bg .gradients-container {
  filter: url(#goo) blur(40px);
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

/* 渐变光斑样式 */
.gradient-bg .g1,
.gradient-bg .g2,
.gradient-bg .g3,
.gradient-bg .g4,
.gradient-bg .g5 {
  position: absolute;
  background: radial-gradient(circle at center, rgba(var(--color1), 0.8) 0, rgba(var(--color1), 0) 50%) no-repeat;
  mix-blend-mode: var(--blending);
  width: var(--circle-size);
  height: var(--circle-size);
}

.gradient-bg .g1 {
  background: radial-gradient(circle at center, rgba(var(--color1), 0.8) 0, rgba(var(--color1), 0) 50%) no-repeat;
  top: calc(50% - var(--circle-size) / 2);
  left: calc(50% - var(--circle-size) / 2);
  animation: moveVertical 30s ease infinite;
}

.gradient-bg .g2 {
  background: radial-gradient(circle at center, rgba(var(--color2), 0.8) 0, rgba(var(--color2), 0) 50%) no-repeat;
  top: calc(50% - var(--circle-size) / 2);
  left: calc(50% - var(--circle-size) / 2);
  transform-origin: calc(50% - 400px);
  animation: moveInCircle 20s reverse infinite;
}

.gradient-bg .g3 {
  background: radial-gradient(circle at center, rgba(var(--color3), 0.8) 0, rgba(var(--color3), 0) 50%) no-repeat;
  top: calc(50% - var(--circle-size) / 2 + 200px);
  left: calc(50% - var(--circle-size) / 2 - 500px);
  transform-origin: calc(50% + 400px);
  animation: moveInCircle 40s linear infinite;
}

.gradient-bg .g4 {
  background: radial-gradient(circle at center, rgba(var(--color4), 0.8) 0, rgba(var(--color4), 0) 50%) no-repeat;
  top: calc(50% - var(--circle-size) / 2);
  left: calc(50% - var(--circle-size) / 2);
  transform-origin: calc(50% - 200px);
  animation: moveHorizontal 40s ease infinite;
  opacity: 0.7;
}

.gradient-bg .g5 {
  background: radial-gradient(circle at center, rgba(var(--color5), 0.8) 0, rgba(var(--color5), 0) 50%) no-repeat;
  width: calc(var(--circle-size) * 2);
  height: calc(var(--circle-size) * 2);
  top: calc(50% - var(--circle-size));
  left: calc(50% - var(--circle-size));
  transform-origin: calc(50% - 800px) calc(50% + 200px);
  animation: moveInCircle 20s ease infinite;
}

.gradient-bg .interactive {
  position: absolute;
  background: radial-gradient(circle at center, rgba(var(--color-interactive), 0.8) 0, rgba(var(--color-interactive), 0) 50%) no-repeat;
  mix-blend-mode: var(--blending);
  width: 100%;
  height: 100%;
  top: -50%;
  left: -50%;
  opacity: 0.7;
}

/* 动画定义 */
@keyframes moveInCircle {
  0% { transform: rotate(0deg); }
  50% { transform: rotate(180deg); }
  100% { transform: rotate(360deg); }
}

@keyframes moveVertical {
  0% { transform: translateY(-50%); }
  50% { transform: translateY(50%); }
  100% { transform: translateY(-50%); }
}

@keyframes moveHorizontal {
  0% { transform: translateX(-50%) translateY(-10%); }
  50% { transform: translateX(50%) translateY(10%); }
  100% { transform: translateX(-50%) translateY(-10%); }
}

/* 原有量子页面样式（适配动态背景） */
.Quantum-page {
  max-width: 1100px;
  margin: 40px auto;
  padding: 0 20px;
  position: relative; /* 确保在背景上层 */
  z-index: 10; /* 高于背景的z-index=1 */
}

.banner {
  position: relative;
  width: 38vw;
  height: 12vh;
  margin: 0 auto;
  background-image: url("https://quantumcomputer.ac.cn/_nuxt/img/labDataimg.959fddd.png");
  background-size: cover;
  background-position: center;
}

.banner-text {
  position: absolute;
  top: 20%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 24px;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6);
}

.content-center {
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.colored-bar {
  background: linear-gradient(120deg, #d2f6f6 60%, #bef2ea 100%);
  border-radius: 10px 10px 0 0;
  height: 30px;
  width: 80%;
}

.card-container {
  display: flex;
  align-items: stretch;
  justify-content: center;
  border-radius: 20px;
  transition: box-shadow 0.3s ease, transform 0.3s ease;
  cursor: pointer;
  width: 80%;
}

.card-container:hover {
  box-shadow: 0 0 30px rgba(32, 124, 158, 0.6), 0 0 40px rgba(74, 181, 220, 0.4);
  transform: translateY(-2px);
}

/* 卡片样式调整为半透明，适配动态背景 */
.card {
  border-radius: 0 10px 10px 0;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.15); /* 半透明背景 */
  backdrop-filter: blur(10px); /* 毛玻璃效果 */
}

.card-left {
  width: 60%;
  border-radius: 10px 0 0 10px;
  object-fit: cover;
}

.card-right {
  width: 100%;
  display: flex;
  flex-direction: column;
  padding: 10px;
  box-sizing: border-box;
}

.row1 {
  display: flex;
  align-items: start;
  justify-content: space-between;
}

.row1-text {
  margin: 0;
  font-size: 25px;
  font-weight: bold;
  color: rgb(255, 255, 255); /* 文字改为白色，适配深色背景 */
}

.right-icon {
  width: 40px;
  height: 40px;
}

.card-line {
  border: none;
  border-top: 2px solid #0882ae;
  margin: 20px 0;
}

.row3 {
  margin-top: 10px;
  font-size: 16px;
  color: rgba(255, 255, 255, 0.9); /* 文字半白，更柔和 */
  line-height: 1.6;
}

/* 滑入动画 */
.slide-left {
  transform: translateX(-100px);
  opacity: 0;
  transition: all 1s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

.slide-right {
  transform: translateX(100px);
  opacity: 0;
  transition: all 1s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

.visible {
  transform: translateX(0);
  opacity: 1;
}
</style>
