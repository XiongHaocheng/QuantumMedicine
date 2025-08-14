<template>
  <div class="Quantum-page">

    <!-- 模块列表 -->
    <div class="module" v-for="(item, index) in modules" :key="index" ref="modulesRef" style="margin-top: 80px;">
      <div class="banner">
        <p class="banner-text">{{ item.title }}</p>
      </div>

      <div class="content-center">
        <div class="colored-bar"></div>

        <div class="card-container">
          <!-- 偶数行（index 从 0 开始，所以是 index % 2 === 1）反转顺序 -->
          <template v-if="index % 2 === 1">
            <!-- 卡片在左 -->
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
            <!-- 图片在右 -->
            <img class="card-left slide-right" :src="item.img" alt="图片" />
          </template>

          <!-- 其他行保持原来布局 -->
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
    content:
      '移动云量子计算云平台是融合了经典算力和量子算力的全栈量子计算云服务系统，提供“多制式”量子算力服务、“多形态”量子应用程序设计和“多场景”量子应用算法，能够为金融、交通、生物医药等对于大规模复杂问题求解有实际需求的垂直行业用户和高校科研用户提供云上可便捷调用的量子计算一站式服务，拓展量子计算的应用边界。'
  },
  {
    title: '重建技术',
    img: ReconstructionImg,
    cardTitle: '重建技术',
    content:
      '生成器U-Net潜空间和判别器中间层均嵌入量子增强模块，通过4比特变分量子电路（RX、RY、RZ旋转门与CNOT门）对高维特征进行非线性映射与纠缠融合，并通过测量与残差回传到经典网络，实现端到端联合优化，从而提升低剂量PET图像的细节恢复和噪声抑制能力。'
  },
  {
    title: '分割技术',
    img: Segmentation,
    cardTitle: '分割技术',
    content:
      '该模型基于VGG16-UNet结构，编码器提取多尺度特征并可利用预训练权重加速训练，解码器通过上采样和跳跃连接恢复空间分辨率。在编码器与解码器之间嵌入量子增强模块，通过4比特变分量子电路（RX、RY、RZ旋转门与CNOT门）建立纠缠，对高维特征进行非线性映射与特征融合。量子特征经后网络扩展并通过残差与经典特征融合，实现端到端联合训练。'
  },
  {
    title: '剂量预测技术',
    img: DosePrediction,
    cardTitle: '剂量预测技术',
    content:
      '为充分利用医学关键先验信息，我们提出MPDCL方法。该方法分为三阶段：第一阶段全局剂量学习（GDN）通过3D U-Net对CT图像及PTV、OAR掩膜生成粗略剂量分布；第二阶段射束方向剂量细化（BDN）采用ResUnet对不同角度射束路径进行剂量调整；第三阶段全局剂量细化结合边缘强化与Mixed DVH Constraints模块改进最终剂量图。在GDN和BDN阶段，我们创新性地引入量子增强模块，通过变分量子电路在高维Hilbert空间中对特征进行非线性映射与纠缠融合，增强模型对复杂剂量模式和细节的捕捉能力，从而显著提升剂量预测精度与模型表现。'
  }
]

const modulesRef = ref([])
onMounted(() => {
  window.scrollTo(0, 0);
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const img = entry.target.querySelector('.card-left')
        const card = entry.target.querySelector('.card')
        if (entry.isIntersecting) {
          img.classList.add('visible')
          card.classList.add('visible')
        } else {
          // 离开视口时移除动画类，每次滚动都会触发
          img.classList.remove('visible')
          card.classList.remove('visible')
        }
      })
    },
    { threshold: 0.2 }
  )

  modulesRef.value.forEach((module) => observer.observe(module))
})
</script>

<style scoped>
.Quantum-page {
  max-width: 1100px;
  margin: 40px auto;
  padding: 0;
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
  border-radius: 20px;
  cursor: pointer;
}

.card-container:hover {
  box-shadow: 0 0 30px rgba(32, 124, 158, 0.6), 0 0 40px rgba(74, 181, 220, 0.4);
  transform: translateY(-2px);
}

.card {
  border-radius: 0 10px 10px 0;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(120deg, #b7efef 60%, #82e8d9 100%);
}

/* 左侧图片部分 */
.card-left {
  width: 60%;
}

/* 右侧内容部分 */
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
  color: rgb(0, 0, 0);
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
  color: rgb(0, 0, 0);
}

/* 滑入动画初始状态 */
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

/* 滑入可见状态 */
.visible {
  transform: translateX(0);
  opacity: 1;
}
</style>
