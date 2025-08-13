<template>
    <section class="culture-bar">
        <div class="culture-bar-bg"></div>
        <div class="culture-bar-content">
            <h2>团队文化</h2>
            <div class="culture-list">
                <article class="culture-item">
                    <h3>使命</h3>
                    <p>
                        通过创新科技赋能医疗行业，推动人工智能与医疗的深度融合，致力于让优质医疗资源触手可及。
                    </p>
                </article>
                <article class="culture-item">
                    <h3>愿景</h3>
                    <p>
                        成为智能医疗领域的引领者，致力于打造一个协作共赢的数字医疗生态，推动全球健康发展。
                    </p>
                </article>
                <article class="culture-item">
                    <h3>价值观</h3>
                    <p>
                        坚持正直与可靠，倡导协作与创新，始终以用户为中心，追求卓越与可持续的进步。
                    </p>
                </article>
            </div>
        </div>
    </section>
</template>

<script setup>
import { onMounted } from 'vue';

onMounted(() => {
    // 页面加载后依次显示卡片
    const items = document.querySelectorAll('.culture-item');
    items.forEach((item, index) => {
        setTimeout(() => {
            item.classList.add('is-visible');
        }, index * 200);
    });
});
</script>

<style scoped>
.culture-bar {
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    width: 100vw;
    margin-bottom: 48px;
    margin-top: 72px;
}

.culture-bar-bg {
    position: absolute;
    inset: 0 auto auto 0;
    width: 100%;
    min-height: 200px;
    height: 100%;
    background: linear-gradient(135deg, #283593 0%, #1976d2 100%);
    opacity: 0.85;
    z-index: 0;
    filter: blur(10px);
}

.culture-bar-content {
    position: relative;
    z-index: 1;
    max-width: 1100px;
    margin: 0 auto;
    padding: 40px 24px;
    box-sizing: border-box;
    text-align: center;
}

.culture-bar-content h2 {
    color: #fff;
    font-weight: 700;
    font-size: 2rem;
    margin-bottom: 32px;
    letter-spacing: 2px;
    text-shadow: 0 2px 10px rgba(20, 40, 80, 0.2);
}

.culture-list {
    display: flex;
    gap: 32px;
    justify-content: center;
    flex-wrap: wrap;
}

.culture-item {
    flex: 1 1 260px;
    background: #f5f8fd;
    border-radius: 12px;
    padding: 24px 20px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    margin: 0;
    transform: translateY(20px);
    opacity: 0;
    transition: transform 0.5s cubic-bezier(.22, .61, .36, 1), opacity 0.5s cubic-bezier(.22, .61, .36, 1), box-shadow 0.3s;
}

.culture-item.is-visible {
    transform: translateY(0);
    opacity: 1;
}

.culture-item:hover {
    transform: translateY(-10px) scale(1.05);
    box-shadow: 0 12px 20px rgba(20, 40, 80, 0.15);
}

.culture-item h3 {
    color: #1976d2;
    font-weight: 700;
    font-size: 1.1rem;
    margin-bottom: 12px;
}

.culture-item p {
    color: #3a4660;
    font-size: 1rem;
    line-height: 1.6;
}

/* 响应式优化 */
@media (max-width: 900px) {
    .culture-list {
        flex-direction: column;
        gap: 18px;
    }

    .culture-item {
        padding: 20px 12px;
    }
}
</style>
