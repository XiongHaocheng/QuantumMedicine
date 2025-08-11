<template>
    <section class="model-showcase">
        <div v-for="(model, idx) in models" :key="model.title" class="model-item" :class="{ visible: visible[idx] }"
            :ref="el => setModelRef(el, idx)">
            <div v-if="idx % 2 === 0" class="model-left">
                <img src="@/assets/temp.png" class="model-img" alt="模型图片" />
            </div>
            <div class="model-info">
                <h3>{{ model.title }}</h3>
                <p>{{ model.desc }}</p>
            </div>
            <div v-if="idx % 2 !== 0" class="model-right">
                <img src="@/assets/temp.png" class="model-img" alt="模型图片" />
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const models = [
    {
        title: '图像重建模型',
        desc: '该模型通过低剂量采集的数据进行重建，能够恢复高分辨率和高信噪比的医学影像，为医生提供精准的病灶和解剖结构信息。可应用于各种影像类型的重建，帮助医护人员更加清晰地观察疾病发展。'
    },
    {
        title: '图像分割模型',
        desc: '图像分割模型可帮助从复杂的医学影像中精准分离出目标区域，如肿瘤或关键器官，为医生提供详细的结构信息。这一技术对于制定放疗计划、保护危及器官、以及评估治疗效果至关重要。'
    },
    {
        title: '剂量预测模型',
        desc: '该模型结合临床需求进行剂量预测，帮助提高治疗效率，并降低辐射风险。它能够在低剂量成像条件下，快速进行高质量的影像重建与精准的分割与剂量预测，进一步提升治疗效果的精确度。'
    }
]

const visible = ref([false, false, false])
const modelRefs = ref([])

function setModelRef(el, idx) {
    if (el) modelRefs.value[idx] = el
}

onMounted(() => {
    modelRefs.value.forEach((el, idx) => {
        const observer = new IntersectionObserver(
            entries => {
                if (entries[0].isIntersecting) {
                    visible.value[idx] = true
                } else {
                    visible.value[idx] = false
                }
            },
            { threshold: 0.1 }
        )
        if (el) observer.observe(el)
    })
})
</script>

<style scoped>
.model-showcase {
    display: flex;
    flex-direction: column;
    gap: 56px;
    margin: 120px auto 0;
    max-width: 1200px;
    padding: 0 32px;
    margin-bottom: 120px;
    /* 增加底部间距 */
}

.model-item {
    display: flex;
    align-items: stretch;
    background: linear-gradient(90deg, #f7fafd 60%, #e8f0fb 100%);
    border-radius: 24px;
    box-shadow: 0 8px 32px rgba(20, 40, 80, 0.08);
    opacity: 0;
    transform: translateY(60px) scale(0.98);
    transition: opacity 0.8s ease-out, transform 0.8s ease-out;
    gap: 0;
    overflow: hidden;
    min-height: 220px;
    border: 1px solid #e3eaf3;
}

.model-item.visible {
    opacity: 1;
    transform: translateY(0) scale(1);
}

.model-left,
.model-right {
    display: flex;
    flex: 1;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #e3eaf3 0%, #f7fafd 100%);
    opacity: 0;
    transform: translateX(-60px);
    transition: opacity 0.8s 0.2s ease-out, transform 0.8s 0.2s ease-out;
}

.model-item.visible .model-left,
.model-item.visible .model-right {
    opacity: 1;
    transform: translateX(0);
}

.model-right {
    transform: translateX(60px);
}

.model-img {
    width: 320px;
    height: 200px;
    object-fit: cover;
    border-radius: 18px;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.10);
    border: 1.5px solid #d1dbe6;
    transition: transform 0.4s ease-out;
}

.model-item.visible .model-img {
    transform: scale(1.04);
}

.model-info {
    flex: 2;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 32px 40px;
    background: transparent;
    opacity: 0;
    transform: translateY(40px);
    transition: opacity 0.8s 0.4s ease-out, transform 0.8s 0.4s ease-out;
}

.model-item.visible .model-info {
    opacity: 1;
    transform: translateY(0);
}

.model-info h3 {
    font-size: 2rem;
    font-weight: 800;
    margin-bottom: 18px;
    color: #1a2a4a;
    letter-spacing: 1.2px;
    text-shadow: 0 2px 8px rgba(180, 200, 255, 0.08);
}

.model-info p {
    font-size: 1.18rem;
    color: #3a4660;
    line-height: 1.85;
    margin-bottom: 0;
    text-align: justify;
    letter-spacing: 0.2px;
}

@media (max-width: 900px) {
    .model-showcase {
        gap: 32px;
        padding: 0 8px;
    }

    .model-item {
        flex-direction: column;
        min-height: 0;
    }

    .model-left,
    .model-right {
        width: 100%;
        padding: 16px 0;
        transform: none !important;
    }

    .model-info {
        padding: 24px 16px;
        transform: none !important;
    }

    .model-img {
        width: 100%;
        height: auto;
    }
}
</style>