<template>
    <section class="about-section honor-section" aria-labelledby="honor-title">
        <div class="honor-title-wrap">
            <WheatIcon class="wheat" />
            <h2 id="honor-title" class="honor-title">团队荣誉</h2>
            <WheatIcon class="wheat" />
        </div>

        <div class="honor-carousel" @mouseenter="pause" @mouseleave="play">
            <button class="carousel-btn left" @click="prev" aria-label="上一个">&#8592;</button>
            <div class="viewport" ref="viewportEl">
                <div class="stage" :style="stageStyle">
                    <div v-for="(h, i) in honors" :key="h.title" class="card" :class="{ active: i === center }"
                        :style="cardStyle(i)">
                        <div class="thumb-wrap">
                            <img class="thumb" :src="h.img" :alt="h.title" />
                        </div>
                        <div class="info">
                            <h3 class="name">{{ h.title }}</h3>
                            <p class="desc">{{ h.desc }}</p>
                        </div>
                    </div>
                </div>
            </div>
            <button class="carousel-btn right" @click="next" aria-label="下一个">&#8594;</button>
        </div>

        <div class="dots">
            <button v-for="(h, i) in honors" :key="h.title + '-dot'" class="dot" :class="{ active: i === center }"
                @click="go(i)" />
        </div>
    </section>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const honors = [
    {
        title: '国家自然科学奖二等奖',
        desc: '荣获国家自然科学奖二等奖，项目为“神经网络的若干关键基础理论研究”。',
        img: new URL('@/assets/honor/1.png', import.meta.url).href
    },
    {
        title: '中国图象图形学会自然科学奖一等奖',
        desc: '荣获2022年中国图象图形学会自然科学奖一等奖，项目为“高维数据的潜在结构发现”。',
        img: new URL('@/assets/honor/2.png', import.meta.url).href
    },
    {
        title: '四川省科学技术进步奖二等奖',
        desc: '荣获四川省科学技术进步奖二等奖，项目为“智能精准放射治疗关键技术及应用”。',
        img: new URL('@/assets/honor/3.png', import.meta.url).href
    },
    {
        title: '国家科学技术进步奖二等奖',
        desc: '荣获国家科学技术进步奖二等奖，项目为“面向高端训练和体验服务的全景互动视觉合成技术与应用”。',
        img: new URL('@/assets/honor/4.png', import.meta.url).href
    },
    {
        title: '四川省计算机科学技术奖一等奖',
        desc: '荣获四川省计算机科学技术奖一等奖，项目为“人工智能在医学影像成像与分析中的研究及应用”。',
        img: new URL('@/assets/honor/5.png', import.meta.url).href
    },
    {
        title: '技术转让合同',
        desc: '完成基于CNN的多模态鼻咽部肿瘤联合分割方法等技术转让合同签订。',
        img: new URL('@/assets/honor/6.png', import.meta.url).href
    },
    {
        title: '发明专利证书',
        desc: '获得多项医学影像分割及处理相关发明专利授权。',
        img: new URL('@/assets/honor/7.png', import.meta.url).href
    },
    {
        title: '计算机软件著作权登记证书',
        desc: '获得颅内肿瘤影像智能诊断平台计算机软件著作权登记证书。',
        img: new URL('@/assets/honor/8.png', import.meta.url).href
    },
    {
        title: '发明专利证书',
        desc: '授权发明专利“一种循环肿瘤细胞免疫检查点应用方法”。',
        img: new URL('@/assets/honor/9.png', import.meta.url).href
    },
    {
        title: '天府青城计划证书',
        desc: '入选2023年度“天府青城计划”青年科技人才项目。',
        img: new URL('@/assets/honor/10.png', import.meta.url).href
    },
    {
        title: '获奖证书',
        desc: '作品“慧颜识痛”获“互联网+”大学生创新创业大赛金奖。',
        img: new URL('@/assets/honor/11.png', import.meta.url).href
    },
    {
        title: '医疗器械注册证',
        desc: '获得放射治疗靶区勾画软件医疗器械注册证。',
        img: new URL('@/assets/honor/12.png', import.meta.url).href
    },
    {
        title: '计算机软件著作权登记证书',
        desc: '获得放射治疗靶区勾画软件计算机软件著作权登记证书。',
        img: new URL('@/assets/honor/13.png', import.meta.url).href
    },
    {
        title: 'Nature Communications论文',
        desc: '在Nature Communications发表全身器官勾画加速放疗深度学习研究成果。',
        img: new URL('@/assets/honor/14.png', import.meta.url).href
    },
    {
        title: '高新技术企业证书',
        desc: '上海联影智能医疗科技有限公司获评高新技术企业。',
        img: new URL('@/assets/honor/15.png', import.meta.url).href
    }



]


const ITEM_W = 280
const GAP = 16
const AUTOPLAY_MS = 4000
const SCALE_CENTER = 1
const SCALE_SIDE = 0.86
const OPACITY_CENTER = 1
const OPACITY_SIDE = 0.55
const BLUR_SIDE = 2

const center = ref(0)
let timer = null

function prev() { center.value = (center.value - 1 + honors.length) % honors.length }
function next() { center.value = (center.value + 1) % honors.length }
function go(i) { center.value = i }

function play() { stop(); timer = setInterval(next, AUTOPLAY_MS) }
function pause() { stop() }
function stop() { if (timer) { clearInterval(timer); timer = null } }

onMounted(play)
onBeforeUnmount(stop)

const stageStyle = computed(() => ({
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    gap: `${GAP}px`,
    width: '100%'
}))

function cardStyle(i) {
    const len = honors.length
    // 计算当前卡片与中心卡片的相对位置（循环）
    let diff = (i - center.value + len) % len

    // 当前是中间卡
    if (diff === 0) {
        return {
            transform: `scale(${SCALE_CENTER})`,
            opacity: OPACITY_CENTER,
            filter: `blur(0px)`,
            display: 'block',
            zIndex: 2
        }
    }

    // 右侧卡片（相邻）
    if (diff === 1) {
        return {
            transform: `scale(${SCALE_SIDE})`,
            opacity: OPACITY_SIDE,
            filter: `blur(${BLUR_SIDE}px)`,
            display: 'block',
            zIndex: 1
        }
    }

    // 左侧卡片（相邻）
    if (diff === len - 1) {
        return {
            transform: `scale(${SCALE_SIDE})`,
            opacity: OPACITY_SIDE,
            filter: `blur(${BLUR_SIDE}px)`,
            display: 'block',
            zIndex: 1
        }
    }

    // 其他卡片隐藏
    return { display: 'none' }
}
</script>

<script>
export default {
    components: {
        WheatIcon: {
            name: 'WheatIcon',
            props: { class: String },
            template: `
                <svg :class="$props.class" width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                    <path d="M12 2c1.1 0 2 .9 2 2v3c0 1.657-1.343 3-3 3H9c-1.105 0-2-.895-2-2s.895-2 2-2h2V4c0-1.1.9-2 2-2Z" fill="currentColor" opacity=".9"/>
                    <path d="M9 10c0 1.657 1.343 3 3 3h1c1.657 0 3 1.343 3 3v1c0 1.105-.895 2-2 2s-2-.895-2-2v-1h-2c-1.657 0-3-1.343-3-3v-1c0-1.105.895-2 2-2s2 .895 2 2v1H9v-1Z" fill="currentColor"/>
                    <path d="M12 14v8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
                </svg>
            `
        }
    }
}
</script>

<style scoped>
.honor-section {
    --item-w: 280px;
    --gap: 16px;
    --radius: 16px;
    --title: #0f172a;
    --muted: #475569;
    --accent: #6d28d9;
    padding: 32px 0 8px;
}

.honor-title-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    margin-bottom: 20px;
}

.honor-title {
    font-size: 28px;
    line-height: 1.2;
    color: var(--title);
    font-weight: 800;
}

.wheat {
    color: var(--accent);
}

.honor-carousel {
    display: grid;
    grid-template-columns: 40px 1fr 40px;
    align-items: center;
    gap: 8px;
}

.carousel-btn {
    width: 36px;
    height: 36px;
    border-radius: 999px;
    border: 1px solid #e5e7eb;
    background: #fff;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(0, 0, 0, .06);
    transition: transform .12s ease, box-shadow .2s ease;
}

.carousel-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(0, 0, 0, .08);
}

.carousel-btn:active {
    transform: translateY(0);
}

.viewport {
    overflow: hidden;
    display: flex;
    justify-content: center;
}

.stage {
    display: flex;
    gap: var(--gap);
    will-change: transform;
    bottom-margin: 20px;
    min-height: 260px;
}

.card {
    min-width: var(--item-w);
    max-width: var(--item-w);
    background: #ffffff;
    border: 1px solid #eef2f7;
    border-radius: var(--radius);
    box-shadow: 0 10px 24px rgba(2, 6, 23, 0.06);
    padding: 16px;
    transition: box-shadow .25s ease, transform .25s ease;
}

.card.active {
    transform: translateY(-3px);
    box-shadow: 0 18px 36px rgba(2, 6, 23, 0.08);
}

.thumb-wrap {
    width: 100%;
    height: 160px;
    border-radius: 12px;
    overflow: hidden;
}

.thumb {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

.info {
    margin-top: 12px;
}

.name {
    font-size: 16px;
    font-weight: 700;
    color: #0b1220;
    margin: 0 0 6px;
}

.desc {
    font-size: 13px;
    color: var(--muted);
    line-height: 1.5;
    bottom-margin: 20px;
}

.dots {
    display: flex;
    gap: 8px;
    justify-content: center;
    margin: 18px 0 0;
}

.dot {
    width: 8px;
    height: 8px;
    border-radius: 999px;
    border: 0;
    cursor: pointer;
    background: #e5e7eb;
    transition: transform .2s ease, background .2s ease;
    padding: 0;
}

.dot.active {
    background: var(--accent);
    transform: scale(1.25);
}

/* 响应式 */
@media (max-width: 1024px) {
    .honor-section {
        --item-w: 260px;
    }
}

@media (max-width: 768px) {
    .honor-section {
        --item-w: 240px;
    }

    .honor-carousel {
        grid-template-columns: 32px 1fr 32px;
    }
}

@media (max-width: 520px) {
    .honor-section {
        --item-w: calc(100vw - 72px);
    }

    .honor-carousel {
        grid-template-columns: 28px 1fr 28px;
    }
}
</style>
