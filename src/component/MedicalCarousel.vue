<template>
    <div class="carousel-bg">
        <div v-for="(img, idx) in images" :key="idx" class="carousel-img" :style="{
            backgroundImage: `url(${img.url})`,
            opacity: idx === currentIndex ? 1 : 0,
            filter: idx === currentIndex ? 'blur(0px)' : 'blur(12px)',
            zIndex: idx === currentIndex ? 2 : 1
        }"></div>
        <div class="carousel-overlay">
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
import { ref, onMounted, onUnmounted } from 'vue'

const images = [
    {
        url: new URL('@/assets/home1.png', import.meta.url).href,
        alt: '量子医疗1',
        caption: '量子医疗 · 智能健康新纪元'
    },
    {
        url: new URL('@/assets/home2.png', import.meta.url).href,
        alt: '量子医疗2',
        caption: '量子计算 · 引领医疗创新'
    },
    {
        url: new URL('@/assets/home3.png', import.meta.url).href,
        alt: '量子医疗3',
        caption: '智慧医疗 · 商业化量子解决方案'
    }
]

const currentIndex = ref(0)
let timer = null

function goToImage(idx) {
    currentIndex.value = idx
}

function nextImage() {
    currentIndex.value = (currentIndex.value + 1) % images.length
}

onMounted(() => {
    timer = setInterval(nextImage, 4000)
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
    transition: opacity 0.8s, filter 0.8s;
    will-change: opacity, filter;
}

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
    /* 新增，确保文字在图片之上 */
    position: relative;
    /* 新增，激活z-index */
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
    /* 确保小圆点在图片之上 */
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
    /* 始终不透明 */
    transition: none;
    /* 禁用过渡效果 */
}

.carousel-indicators .active {
    background: #1976d2;
}

.fade-caption-enter-active,
.fade-caption-leave-active {
    transition: opacity 0.3s, filter 0.3s;
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