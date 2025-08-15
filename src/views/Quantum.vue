<template>
  <!-- 动态背景容器（底层） -->
  <div class="quantum-gradient-bg">
    <!-- SVG噪声背景 -->
    <svg 
      viewBox="0 0 100vw 100vw"
      xmlns='http://www.w3.org/2000/svg'
      class="quantum-noiseBg"
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
    <svg xmlns="http://www.w3.org/2000/svg" class="quantum-svgBlur">
      <defs>
        <filter id="goo">
          <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur" />
          <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -8" result="goo" />
          <feBlend in="SourceGraphic" in2="goo" />
        </filter>
      </defs>
    </svg>

    <!-- 渐变光斑容器 -->
    <div class="quantum-gradients-container">
      <div class="quantum-g1"></div>
      <div class="quantum-g2"></div>
      <div class="quantum-g3"></div>
      <div class="quantum-g4"></div>
      <div class="quantum-g5"></div>
      <div class="quantum-interactive" ref="interactiveRef"></div>
    </div>

    <!-- 原有量子介绍内容（上层） -->
    <div class="quantum-page">
      <div class="quantum-module" v-for="(item, index) in modules" :key="index" ref="modulesRef" style="margin-top: 80px;">
        <div class="quantum-banner">
          <p class="quantum-banner-text">{{ item.title }}</p>
        </div>

        <div class="quantum-content-center">
          <div class="quantum-colored-bar"></div>

          <div class="quantum-card-container">
            <!-- 偶数行反转顺序 -->
            <template v-if="index % 2 === 1">
              <div class="quantum-card quantum-slide-left">
                <div class="quantum-card-right">
                  <div class="quantum-row1">
                    <p class="quantum-row1-text">{{ item.cardTitle }}</p>
                    <img class="quantum-right-icon" src="../assets/logo.png" alt="图标" />
                  </div>
                  <hr class="quantum-card-line" />
                  <div class="quantum-row3">{{ item.content }}</div>
                </div>
              </div>
              <img class="quantum-card-left quantum-slide-right" :src="item.img" alt="图片" />
            </template>

            <!-- 其他行布局 -->
            <template v-else>
              <img class="quantum-card-left quantum-slide-left" :src="item.img" alt="图片" />
              <div class="quantum-card quantum-slide-right">
                <div class="quantum-card-right">
                  <div class="quantum-row1">
                    <p class="quantum-row1-text">{{ item.cardTitle }}</p>
                    <img class="quantum-right-icon" src="../assets/logo.png" alt="图标" />
                  </div>
                  <hr class="quantum-card-line" />
                  <div class="quantum-row3">{{ item.content }}</div>
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

const interactiveRef = ref(null)
const modulesRef = ref([])

onMounted(() => {
  window.scrollTo(0, 0);

  // 滚动动画逻辑
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const img = entry.target.querySelector('.quantum-card-left')
        const card = entry.target.querySelector('.quantum-card')
        if (entry.isIntersecting) {
          img.classList.add('quantum-visible')
          card.classList.add('quantum-visible')
        } else {
          img.classList.remove('quantum-visible')
          card.classList.remove('quantum-visible')
        }
      })
    },
    { threshold: 0.2 }
  )
  modulesRef.value.forEach((module) => observer.observe(module))

  // 鼠标跟随逻辑
  if (interactiveRef.value) {
    let curX = 0
    let curY = 0
    let tgX = 0
    let tgY = 0

    const move = () => {
      curX += (tgX - curX) / 20
      curY += (tgY - curY) / 20
      interactiveRef.value.style.transform = `translate(${Math.round(curX)}px, ${Math.round(curY)}px)`
      requestAnimationFrame(move)
    }

    window.addEventListener('mousemove', (event) => {
      tgX = event.clientX
      tgY = event.clientY
    })

    move()
  }
})
</script>

<style>
/* 仅作用于量子页面的基础样式（避免全局*选择器污染） */
.quantum-gradient-bg,
.quantum-gradient-bg * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  color: #FFF;
  background: transparent;
  border: none;
}

.quantum-gradient-bg html,
.quantum-gradient-bg body {
  height: 100%;
  width: 100%;
  overflow-x: hidden;
}

/* 动态背景容器 */
.quantum-gradient-bg {
  width: 100vw;
  min-height: 100vh;
  position: relative;
  background: linear-gradient(40deg, var(--color-bg1), var(--color-bg2));
  overflow: hidden;
}

/* 噪声背景 */
.quantum-noiseBg {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 1;
  mix-blend-mode: soft-light;
  opacity: 0.3;
}

.quantum-svgBlur {
  display: none;
}

/* 渐变光斑容器 */
.quantum-gradients-container {
  filter: url(#goo) blur(40px);
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

/* 光斑样式 */
.quantum-g1, .quantum-g2, .quantum-g3, .quantum-g4, .quantum-g5 {
  position: absolute;
  mix-blend-mode: var(--blending);
  width: var(--circle-size);
  height: var(--circle-size);
}

.quantum-g1 {
  background: radial-gradient(circle at center, rgba(var(--color1), 0.8) 0, rgba(var(--color1), 0) 50%) no-repeat;
  top: calc(50% - var(--circle-size) / 2);
  left: calc(50% - var(--circle-size) / 2);
  animation: quantum-moveVertical 30s ease infinite;
}

.quantum-g2 {
  background: radial-gradient(circle at center, rgba(var(--color2), 0.8) 0, rgba(var(--color2), 0) 50%) no-repeat;
  top: calc(50% - var(--circle-size) / 2);
  left: calc(50% - var(--circle-size) / 2);
  transform-origin: calc(50% - 400px);
  animation: quantum-moveInCircle 20s reverse infinite;
}

.quantum-g3 {
  background: radial-gradient(circle at center, rgba(var(--color3), 0.8) 0, rgba(var(--color3), 0) 50%) no-repeat;
  top: calc(50% - var(--circle-size) / 2 + 200px);
  left: calc(50% - var(--circle-size) / 2 - 500px);
  transform-origin: calc(50% + 400px);
  animation: quantum-moveInCircle 40s linear infinite;
}

.quantum-g4 {
  background: radial-gradient(circle at center, rgba(var(--color4), 0.8) 0, rgba(var(--color4), 0) 50%) no-repeat;
  top: calc(50% - var(--circle-size) / 2);
  left: calc(50% - var(--circle-size) / 2);
  transform-origin: calc(50% - 200px);
  animation: quantum-moveHorizontal 40s ease infinite;
  opacity: 0.7;
}

.quantum-g5 {
  background: radial-gradient(circle at center, rgba(var(--color5), 0.8) 0, rgba(var(--color5), 0) 50%) no-repeat;
  width: calc(var(--circle-size) * 2);
  height: calc(var(--circle-size) * 2);
  top: calc(50% - var(--circle-size));
  left: calc(50% - var(--circle-size));
  transform-origin: calc(50% - 800px) calc(50% + 200px);
  animation: quantum-moveInCircle 20s ease infinite;
}

.quantum-interactive {
  position: absolute;
  background: radial-gradient(circle at center, rgba(var(--color-interactive), 0.8) 0, rgba(var(--color-interactive), 0) 50%) no-repeat;
  mix-blend-mode: var(--blending);
  width: 100%;
  height: 100%;
  top: -50%;
  left: -50%;
  opacity: 0.7;
}

/* 量子页面专属动画（添加前缀避免冲突） */
@keyframes quantum-moveInCircle {
  0% { transform: rotate(0deg); }
  50% { transform: rotate(180deg); }
  100% { transform: rotate(360deg); }
}

@keyframes quantum-moveVertical {
  0% { transform: translateY(-50%); }
  50% { transform: translateY(50%); }
  100% { transform: translateY(-50%); }
}

@keyframes quantum-moveHorizontal {
  0% { transform: translateX(-50%) translateY(-10%); }
  50% { transform: translateX(50%) translateY(10%); }
  100% { transform: translateX(-50%) translateY(-10%); }
}

/* 量子页面内容样式 */
.quantum-page {
  max-width: 1100px;
  margin: 40px auto;
  padding: 0 20px;
  position: relative;
  z-index: 10;
}

.quantum-banner {
  position: relative;
  width: 38vw;
  height: 12vh;
  margin: 0 auto;
  background-image: url("https://quantumcomputer.ac.cn/_nuxt/img/labDataimg.959fddd.png");
  background-size: cover;
  background-position: center;
}

.quantum-banner-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 24px;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6);
}

.quantum-content-center {
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.quantum-colored-bar {
  background: linear-gradient(120deg, #d2f6f6 60%, #bef2ea 100%);
  border-radius: 10px 10px 0 0;
  height: 30px;
  width: 80%;
}

.quantum-card-container {
  display: flex;
  align-items: stretch;
  justify-content: center;
  border-radius: 20px;
  transition: box-shadow 0.3s ease, transform 0.3s ease;
  cursor: pointer;
  width: 80%;
}

.quantum-card-container:hover {
  box-shadow: 0 0 30px rgba(32, 124, 158, 0.6), 0 0 40px rgba(74, 181, 220, 0.4);
  transform: translateY(-2px);
}

.quantum-card {
  border-radius: 0 10px 10px 0;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
}

.quantum-card-left {
  width: 60%;
  border-radius: 10px 0 0 10px;
  object-fit: cover;
}

.quantum-card-right {
  width: 100%;
  display: flex;
  flex-direction: column;
  padding: 10px;
  box-sizing: border-box;
}

.quantum-row1 {
  display: flex;
  align-items: start;
  justify-content: space-between;
}

.quantum-row1-text {
  margin: 0;
  font-size: 25px;
  font-weight: bold;
  color: rgb(255, 255, 255);
}

.quantum-right-icon {
  width: 40px;
  height: 40px;
}

.quantum-card-line {
  border: none;
  border-top: 2px solid #0882ae;
  margin: 20px 0;
}

.quantum-row3 {
  margin-top: 10px;
  font-size: 16px;
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.6;
}

/* 滑入动画（带前缀） */
.quantum-slide-left {
  transform: translateX(-100px);
  opacity: 0;
  transition: all 1s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

.quantum-slide-right {
  transform: translateX(100px);
  opacity: 0;
  transition: all 1s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

.quantum-visible {
  transform: translateX(0);
  opacity: 1;
}

/* 变量定义（仅量子页面使用） */
.quantum-gradient-bg {
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
</style>
