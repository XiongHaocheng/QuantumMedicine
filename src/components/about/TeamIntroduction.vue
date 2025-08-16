<template>
    <section class="about-section intro-flex">
        <div class="intro-text">
            <h2 class="intro-title">团队介绍</h2>
            <p class="intro">
                视觉合成图形图像技术国家级重点实验室（智能医学和脑科学实验室）依托四川大学雄厚的科研实力，
                专注于计算机视觉与人工智能的前沿探索与应用转化。
                研究方向涵盖医学图像重建与生成、
                图像分割、多模态数据分析、剂量预测、智能精准放疗及类脑计算等领域。
                实验室配备高速稳定的网络、强大服务器集群以及舒适现代的科研环境，
                形成了从算法研发、系统实现到应用落地的全链条能力。
                我们致力于将科研成果转化为医疗健康、智慧疗养等行业的创新解决方案，助力产业升级与智能化发展。
            </p>
        </div>
        <div class="intro-img-wrap">
            <img class="intro-img" src="@/assets/wangjiang.jpg" alt="团队图片" />
        </div>
    </section>
</template>

<script setup>
// 这里暂时没有复杂的逻辑
</script>

<style scoped>
.intro-flex {
    display: flex;
    align-items: center;
    gap: 40px;
    flex-wrap: nowrap;
    /* 不自动换行，保证左右结构 */
    flex-direction: row;
    margin-top: 100px;
}

/* 7:3 比例 */
.intro-text {
    flex: 1 1 70%;
    min-width: 320px;
    order: 1;
    flex-shrink: 1;
}

.intro-img-wrap {
    flex: 0 0 420px;
    /* 增大图片容器宽度 */
    min-width: 320px;
    /* 同步增大最小宽度 */
    display: flex;
    justify-content: center;
    align-items: center;
    order: 2;
    flex-shrink: 0;
    /* 不允许缩小 */
}

/* 标题与文字左对齐 */
.intro-title {
    text-align: left;
    color: #1976d2;
    font-weight: 700;
    font-size: 1.6rem;
    margin-bottom: 24px;
}

.intro {
    text-align: left;
    color: #333;
    line-height: 1.7;
    font-size: 1.08rem;
}

/* 图片不做圆角/不裁成方形，仅加轻微阴影，保持原始比例 */
.intro-img {
    max-width: 100%;
    /* 保证不超出容器 */
    width: 100%;
    height: auto;
    object-fit: contain;
    box-shadow: 0 8px 28px rgba(20, 40, 80, 0.12);
    /* 无边框、无圆角 */
    border: none;
    border-radius: 0;
    background: transparent;
}

@media (max-width: 900px) {
    .intro-flex {
        flex-direction: column;
        gap: 24px;
        align-items: stretch;
        flex-wrap: wrap;
        /* 小屏允许换行 */
    }

    .intro-text,
    .intro-img-wrap {
        flex: 1 1 100%;
        min-width: 0;
        order: unset;
    }
}
</style>
