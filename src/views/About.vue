<template>
  <div class="about-page">
    <h1 class="page-title">关于我们</h1>

    <!-- 简介区 -->
    <section class="about-section">
      <h2>团队介绍</h2>
      <p class="intro">
        左手医生科技有限公司专注于人工智能与医疗健康领域创新，致力于医学影像智能分析、临床诊疗辅助等方向。团队拥有多项自主研发核心技术，聚焦量子计算、医疗大数据、智能算法等前沿领域，以“让优质医疗触手可及”为使命，服务医院、医生和患者，推动医疗行业数字化升级。
      </p>
    </section>

    <!-- 全宽横条（脱离内容容器，撑满视窗宽度） -->
    <section class="culture-bar">
      <div class="culture-bar-bg"></div>
      <div class="culture-bar-content">
        <h2>团队文化</h2>
        <div class="culture-list">
          <div class="culture-item">
            <h3>使命</h3>
            <p>打造主动式AI，让优质医疗触手可及。</p>
          </div>
          <div class="culture-item">
            <h3>愿景</h3>
            <p>成为智能医疗服务领域的数字平台领导者。</p>
          </div>
          <div class="culture-item">
            <h3>价值观</h3>
            <p>正直、可靠、协作、创新。</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 核心成员：两行网格（上 2、下 4） -->
    <section class="about-section">
      <h2>团队成员</h2>

      <!-- 第一行：2 人（指导老师、组长） -->
      <div class="team-row row-two">
        <article class="member">
          <figure class="avatar-wrap">
            <img src="@/assets/temp.png" alt="老师头像" class="avatar" />
          </figure>
          <h3 class="name">老师</h3>
          <p class="desc">负责团队指导与技术把关。</p>
        </article>

        <article class="member">
          <figure class="avatar-wrap">
            <img src="@/assets/temp.png" alt="队长头像" class="avatar" />
          </figure>
          <h3 class="name">队长</h3>
          <p class="desc">负责整体协调与方案设计。</p>
        </article>
      </div>

      <!-- 第二行：4 人（组员 1-4） -->
      <div class="team-row row-four">
        <article class="member">
          <figure class="avatar-wrap">
            <img src="@/assets/temp.png" alt="组员1头像" class="avatar" />
          </figure>
          <h3 class="name">组员1</h3>
          <p class="desc">负责算法与模型训练。</p>
        </article>

        <article class="member">
          <figure class="avatar-wrap">
            <img src="@/assets/temp.png" alt="组员2头像" class="avatar" />
          </figure>
          <h3 class="name">组员2</h3>
          <p class="desc">负责后端服务与接口。</p>
        </article>

        <article class="member">
          <figure class="avatar-wrap">
            <img src="@/assets/temp.png" alt="组员3头像" class="avatar" />
          </figure>
          <h3 class="name">组员3</h3>
          <p class="desc">负责前端与交互。</p>
        </article>

        <article class="member">
          <figure class="avatar-wrap">
            <img src="@/assets/temp.png" alt="组员4头像" class="avatar" />
          </figure>
          <h3 class="name">组员4</h3>
          <p class="desc">负责测试与质量保障。</p>
        </article>
      </div>
    </section>

    <!-- 团队荣誉板块（SVG 装饰 + Coverflow 环形轮播） -->
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
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const ITEM_W = 300
const GAP = 20
const AUTOPLAY_MS = 4000
const SCALE_CENTER = 1
const SCALE_SIDE = 0.86
const OPACITY_CENTER = 1
const OPACITY_SIDE = 0.55
const BLUR_SIDE = 2

const honors = [
  { title: '全国AI医疗创新大赛一等奖', desc: '荣获2024年全国AI医疗创新大赛一等奖，彰显跨学科研发实力。', img: 'https://images.unsplash.com/photo-1584982751630-42578f02c838?q=80&w=1200&auto=format&fit=crop' },
  { title: '智慧医疗应用金奖', desc: '在智慧医疗应用评选中获得金奖，推动医院场景数字化落地。', img: 'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=1200&auto=format&fit=crop' },
  { title: '量子算法创新奖', desc: '在量子启发式优化算法上取得突破，荣获行业创新奖。', img: 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?q=80&w=1200&auto=format&fit=crop' },
  { title: '最佳学术合作伙伴', desc: '与高校联合课题入选省级重点项目，产学研合作示范。', img: 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?q=80&w=1200&auto=format&fit=crop' },
  { title: '开源贡献卓越团队', desc: '核心仓库连续四个版本位列社区趋势榜前列。', img: 'https://images.unsplash.com/photo-1515879218367-8466d910aaa4?q=80&w=1200&auto=format&fit=crop' }
]

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

const stageStyle = computed(() => {
  const totalWidth = ITEM_W * 3 + GAP * 2
  return {
    width: `${totalWidth}px`,
    display: 'flex',
    justifyContent: 'center',
    gap: `${GAP}px`
  }
})

function cardStyle(i) {
  const len = honors.length
  const d = (i - center.value + len) % len
  // 只显示当前和左右两侧
  if (d === 0) {
    return {
      transform: `scale(${SCALE_CENTER})`,
      opacity: OPACITY_CENTER,
      filter: `blur(0px)`,
      display: 'block'
    }
  } else if (d === 1 || d === len - 1) {
    return {
      transform: `scale(${SCALE_SIDE})`,
      opacity: OPACITY_SIDE,
      filter: `blur(${BLUR_SIDE}px)`,
      display: 'block'
    }
  } else {
    return { display: 'none' }
  }
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
/* ===== 页面基础排版 ===== */
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

.about-section {
  margin-bottom: 48px;
}

.about-section h2 {
  text-align: center;
  color: #1976d2;
  font-weight: 700;
  font-size: 1.4rem;
  margin-bottom: 24px;
}

.intro {
  text-align: justify;
  color: #333;
  line-height: 1.7;
  font-size: 1.08rem;
}

/* ===== 全宽文化横条 ===== */
/* 通过左右各 -50vw 脱离容器限制，达到 100vw 的视觉全宽 */
.culture-bar {
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  width: 100vw;
  margin-bottom: 48px;
}

.culture-bar-bg {
  position: absolute;
  inset: 0 auto auto 0;
  width: 100%;
  height: 200px;
  background: linear-gradient(90deg, #1565c0 0%, #1976d2 100%);
  opacity: .95;
  z-index: 0;
}

.culture-bar-content {
  position: relative;
  /* 盖在渐变背景之上 */
  z-index: 1;
  max-width: 1100px;
  margin: 0 auto;
  padding: 36px 32px 32px;
}

.culture-bar-content h2 {
  text-align: center;
  color: #fff;
  font-weight: 800;
  font-size: 1.6rem;
  margin-bottom: 32px;
  letter-spacing: 2px;
  text-shadow: 0 2px 8px rgba(20, 40, 80, 0.12);
}

/* 三等分卡片（随容器均分） */
.culture-list {
  display: flex;
  gap: 32px;
  justify-content: center;
}

.culture-item {
  flex: 1;
  text-align: center;
  background: #e8f0fb;
  border-radius: 16px;
  padding: 24px 32px;
  box-shadow: 0 2px 12px rgba(20, 40, 80, 0.06);
}

.culture-item h3 {
  color: #1976d2;
  font-weight: 700;
  font-size: 1.1rem;
  margin-bottom: 10px;
}

.culture-item p {
  color: #3a4660;
  font-size: 1rem;
}

/* ===== 成员网格 ===== */
/* 使用两套网格：上 2 列、下 4 列；在小屏降为 1 或 2 列 */
.team-row {
  display: grid;
  gap: 28px 32px;
  margin-bottom: 36px;
  align-items: start;
}

.row-two {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.row-four {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.member {
  text-align: center;
  background: #fff;
  border-radius: 20px;
  padding: 28px 18px 22px;
  box-shadow:
    0 1px 2px rgba(0, 0, 0, .05),
    0 8px 24px rgba(0, 0, 0, .06);
  transition: transform .2s ease, box-shadow .2s ease;
}

.member:hover {
  transform: translateY(-2px);
  box-shadow:
    0 2px 6px rgba(0, 0, 0, .06),
    0 16px 36px rgba(0, 0, 0, .08);
}

/* 头像与文本 */
.avatar-wrap {
  width: 140px;
  height: 140px;
  margin: 0 auto 14px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.avatar {
  width: 120px;
  height: 120px;
  object-fit: cover;
  border-radius: 50%;
  border: 4px solid #1976d2;
  /* 视觉识别的品牌色描边 */
  background: #fff;
  display: block;
}

.name {
  color: #111827;
  font-weight: 700;
  font-size: 18px;
  margin: 6px 0 4px;
}

.desc {
  color: #6b7280;
  font-size: 13px;
  line-height: 1.6;
}

/* ===== 团队荣誉板块 ===== */
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
}

.stage {
  display: flex;
  gap: var(--gap);
  will-change: transform;
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
  margin: 0;
}

/* 指示点 */
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
