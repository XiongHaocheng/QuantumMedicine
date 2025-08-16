<template>
    <section class="why-choose-us">
        <h2 class="why-title">为什么选择我们？</h2>
        <div class="why-list">
            <div class="why-item">
                <img src="@/assets/why_us1.png" alt="自主研发" class="why-img" />
                <div class="why-info">
                    <h3>核心技术自主研发</h3>
                    <p>我们拥有自主设计和开发的量子芯片与医学智能算法，技术壁垒高，保障产品持续创新与领先。</p>
                </div>
            </div>
            <div class="why-item">
                <img src="@/assets/why_us2.png" alt="医疗融合" class="why-img" />
                <div class="why-info">
                    <h3>深度融合医疗场景</h3>
                    <p>产品与医学影像、临床诊疗深度结合，覆盖重建、分割、剂量预测等核心环节，助力精准放射治疗。</p>
                </div>
            </div>
            <div class="why-item">
                <img src="@/assets/why_us3.png" alt="商业化落地" class="why-img" />
                <div class="why-info">
                    <h3>商业化与服务能力</h3>
                    <p>已实现多地医院落地应用，提供全流程技术支持与定制化服务，推动智能医疗行业发展。</p>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
// 可根据实际情况扩展
</script>

<style scoped>
.why-choose-us {
    max-width: 1100px;
    margin: 100px auto 0;
    padding: 0 32px 80px 32px;
    background: #f7fafd;
    border-radius: 32px;
    box-shadow: 0 8px 32px rgba(20, 40, 80, 0.06);
}

.why-title {
    text-align: center;
    font-size: 2.4rem;
    font-weight: 800;
    color: #1a2a4a;
    margin-bottom: 48px;
    letter-spacing: 2px;
}

.why-list {
    display: flex;
    flex-direction: row;
    gap: 40px;
    justify-content: space-between;
}

.why-item {
    flex: 1;
    background: linear-gradient(120deg, #e8f0fb 60%, #f7fafd 100%);
    border-radius: 20px;
    box-shadow: 0 4px 24px rgba(20, 40, 80, 0.08);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 32px 18px 28px 18px;
    transition: box-shadow 0.3s;
    cursor: pointer;
}

.why-item:hover {
    box-shadow: 0 8px 32px rgba(20, 40, 80, 0.16);
}

/* 图片更大，3:2比例 */
.why-img {
    width: 300px;
    height: 200px;
    object-fit: cover;
    border-radius: 16px;
    margin-bottom: 24px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    background: #fff;
}

.why-info h3 {
    font-size: 1.3rem;
    font-weight: 700;
    color: #1976d2;
    margin-bottom: 14px;
    text-align: center;
}

.why-info p {
    font-size: 1.08rem;
    color: #3a4660;
    line-height: 1.7;
    text-align: center;
}

@media (max-width: 900px) {
    .why-list {
        flex-direction: column;
        gap: 32px;
    }

    .why-choose-us {
        padding: 0 8px 48px 8px;
    }

    .why-img {
        width: 100%;
        height: auto;
        aspect-ratio: 3 / 2;
        max-width: 400px;
        margin-left: auto;
        margin-right: auto;
    }
}
</style>