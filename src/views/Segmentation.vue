<template>
  <div class="doseprediction-page">
    <SegmentationQuantumLoading v-if="isProcessing" />
    <!-- 新增的两个横排卡片 -->
    <div class="card-section">
      <div class="card-container">

        <!-- 左侧卡片 -->
        <div class="simple-card">
          <h3>参数配置</h3>
          <hr class="card-line" />
          <h4>当前工作流</h4>
          <div class="pet-content">图像分割</div>
          <hr class="card-line" />
          <div class="input-section">
            <h4>输入参数</h4>
            <div class="upload-prompt">
              <span class="required-asterisk">*</span>
              <p>上传文件</p>
              <div class="tooltip-icon">
                <span class="icon">?</span>
                <span class="tooltip-text">上传待分割的png图像</span>
              </div>
            </div>
            <!-- 文件上传区域 -->
            <div class="upload-box" @click="triggerFileInput" :class="{ 'error': fileError }">
              <input type="file" ref="fileInput" @change="handleFileChange" accept=".png" class="file-input">
              <div v-if="!selectedFile" class="upload-placeholder">
                <i class="upload-icon">🖼️</i>
                <p>点击或拖拽上传图像(.png)</p>
              </div>
              <div v-else>
                <i class="upload-icon">🖼️</i>
                <span>{{ selectedFile.name }}</span>
                <button @click.stop="removeFile" class="remove-btn">×</button>
              </div>
              <div v-if="fileError" class="error-message">
                {{ fileError }}
              </div>
            </div>

            <!-- 开始处理按钮 -->
            <hr class="card-line" />
            <div class="button-container">
              <t-button class="button" @click="handleClick()">点击开始处理</t-button>
            </div>
          </div>
        </div>


        <!-- 右侧卡片 -->
        <div class="simple-card">
          <h3>处理结果</h3>
          <hr class="card-line" />
          <!--结果展示区域-->
          <div class="result-cards">

            <div class="result-card">
              <div class="card-header">分割结果</div>

              <div class="image-placeholder">
                <!-- 更安全的判断方式，避免resultData未定义时报错 -->
                <span v-if="!resultData?.PredictImage">待显示图像</span>
                <img v-else :src="resultData.PredictImage" alt="预测结果" class="dose-img" />
              </div>

              <div class="card-footer">
                <t-button class="button" type="primary" size="small" @click="downloadpredictImage()">
                  点击下载
                </t-button>
              </div>

            </div>

            <div class="result-card">
              <div class="card-header">Ground Truth</div>
              <div class="image-placeholder">
                <!-- 更安全的判断方式，避免resultData未定义时报错 -->
                <span v-if="!resultData?.GroundTruthImage">待显示图像</span>
                <img v-else :src="resultData.GroundTruthImage" alt="Ground Truth" class="dose-img" />
              </div>
              <div class="card-footer">
                <t-button class="button" type="primary" size="small" @click="downrecongroundtruthImage()">
                  点击下载
                </t-button>
              </div>
            </div>

          </div>


          <h3>指标结果</h3>
          <hr class="card-line" />

          <div class="metric-container">

            <div class="metric-row">
              <p class="metric-label">Dice系数</p>
              <div class="pet-result">{{ resultData ? resultData.Dice : '--' }}</div>
            </div>

            <div class="metric-row">
              <p class="metric-label">Recall</p>
              <div class="pet-result">{{ resultData ? resultData.Recall : '--' }}</div>
            </div>

          </div>
          <div class="metric-container">
            <div class="metric-row">
              <p class="metric-label">Precision</p>
              <div class="pet-result">{{ resultData ? resultData.Precision : '--' }}</div>
            </div>

            <div class="metric-row">
              <p class="metric-label">Hausdorff距离</p>
              <div class="pet-result">{{ resultData ? resultData.Hausdorff : '--' }}</div>
            </div>

          </div>

        </div>
      </div>
    </div>
  </div>

</template>

<script setup>
import { ref, onMounted } from 'vue';
import { ElMessage, ElLoading } from 'element-plus';

const PredictImage = new URL('../assets/seg/predict.png', import.meta.url).href;
const GroundTruthImage = new URL('../assets/seg/groundtruth.png', import.meta.url).href;
import SegmentationQuantumLoading from "../components/Segmentation/SegmentationQuantumLoading.vue"; // 引入组件

const fileInput = ref(null);
const selectedFile = ref(null);
const fileError = ref(null);

// 处理状态
const isProcessing = ref(false);
const resultData = ref(null);

const triggerFileInput = () => {
  fileInput.value.click();
};

const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (!file) return;
  if (file.type !== 'png' && !file.name.endsWith('.png')) {
    fileError.value = '只能上传png图像';
    selectedFile.value = null;
    return;
  }
  selectedFile.value = file;
  fileError.value = null;
  resultData.value = null;
}

const removeFile = () => {
  selectedFile.value = null;
  fileInput.value.value = '';
  fileError.value = null;
  resultData.value = null;
};

const handleClick = async () => {
  if (!selectedFile.value) {
    fileError.value = '请先上传文件';
    return;
  }

  isProcessing.value = true;
  try {
    // 调用后端上传并执行
    // const result = await uploadAndRunAPI(selectedFile.value);
    // if (result.error) console.error("错误输出:", result.error);

    await new Promise(resolve => setTimeout(resolve, 10000));
    resultData.value = {
      PredictImage: PredictImage,
      GroundTruthImage: GroundTruthImage,
      Dice: 0.8774,
      Recall: 0.8855,
      Precision: 0.9008,
      Hausdorff: 8.0711
    };
    isProcessing.value = false;
    ElMessage.success("分割成功");
  } catch (error) {
    console.error('处理失败:', error);
    fileError.value = '处理失败: ' + (error.message || error);
  } finally {
    isProcessing.value = false;
  }
};

const downloadpredictImage = () => {
  const imageData = resultData.value?.PredictImage;
  if (!imageData) {
    ElMessage.warning('没有可下载的图片');
    return;
  }
  const link = document.createElement('a');
  link.href = imageData;
  link.download = 'predict.png';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};

const downrecongroundtruthImage = () => {
  const imageData = resultData.value?.GroundTruthImage;
  if (!imageData) {
    ElMessage.warning('没有可下载的图片');
    return;
  }
  const link = document.createElement('a');
  link.href = imageData;
  link.download = 'groundtruth.png';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};

onMounted(() => {
  window.scrollTo(0, 0);
});
</script>


<style scoped>
.doseprediction-page {
  padding: 40px;
  max-width: 1100px;
  margin: 20px auto;
}

/* 新增卡片区域样式 */
.card-section {
  margin: 40px 0;
}

.card-container {
  display: flex;
  gap: 30px;
  /* 卡片间距 */
  justify-content: center;
}

.simple-card {
  flex: 1;
  min-width: 500px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 24px;
  transition: all 0.3s ease;
}

.simple-card h3 {
  color: #333;
  font-size: 1.2rem;
  margin-bottom: 16px;
}



.result-cards {
  display: flex;
  gap: 20px;
  margin-top: 16px;
}

.result-card {
  flex: 1;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
}

.card-header {
  background-color: #f5f5f5;
  padding: 12px;
  font-weight: bold;
  text-align: center;
  border-bottom: 1px solid #e0e0e0;
}

.card-footer {
  height: 4vh;
  padding: 12px;
  text-align: center;
  border-top: 1px solid #f0f0f0;
}

.button-container {
  text-align: center;
}

.card-line {
  border: none;
  border-top: 1px solid #c6c8c9b8;
  margin: 20px 0;
}

.pet-content {
  color: white;
  display: inline-block;
  /* 关键改动：让宽度随内容伸缩 */
  background-color: #40a9ff;
  border-radius: 10px;
  padding: 8px 16px;
  /* 增加内边距 */
  line-height: 1.6;
  margin: 5px 0;
  /* 添加外边距 */
}

.metric-container {
  margin-top: 30px;
  display: flex;
  gap: 8px;
}

.metric-row {
  display: grid;
  grid-template-columns: 120px 80px;
  /* 标签列和结果列固定宽度 */
  align-items: center;
}

.metric-label {
  color: white;
  /* 白色字体 */
  background-color: #40a9ff;
  /* 蓝色背景 */
  border-radius: 6px;
  /* 圆角稍减小 */
  padding: 4px 8px;
  /* 更紧凑的内边距 */
  margin: 0;
  font-size: 14px;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.pet-result {
  min-height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.input-section {
  margin: 10px 0;
}

.upload-prompt {
  margin-top: -20px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
}

.required-asterisk {
  color: red;
  font-weight: bold;
  font-size: 20px;
  margin-top: 5px;
}

.tooltip-icon {
  position: relative;
  display: inline-flex;
  cursor: help;
}

.tooltip-icon .icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 16px;
  height: 16px;
  background-color: #ccc;
  color: white;
  border-radius: 50%;
  font-size: 12px;
  font-weight: bold;
}

.tooltip-icon .tooltip-text {
  visibility: hidden;
  width: 220px;
  background-color: #555;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 8px;
  position: absolute;
  z-index: 1;
  bottom: 125%;
  left: 50%;
  transform: translateX(-50%);
  opacity: 0;
  transition: opacity 0.3s;
}

.tooltip-icon:hover .tooltip-text {
  visibility: visible;
  opacity: 1;
}

/* 文件上传框样式 */
.upload-box {
  border: 2px dashed #ccc;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
  cursor: pointer;
  margin-top: 10px;
  transition: all 0.3s;
  position: relative;
}

.upload-box:hover {
  border-color: #1976d2;
  background-color: #f5f9ff;
}

.upload-box.error {
  border-color: #ff4d4f;
  background-color: #fff2f0;
}

.file-input {
  display: none;
}

.upload-placeholder {
  color: #666;
}

.upload-icon,
.file-icon {
  font-size: 24px;
  display: block;
  margin-bottom: 8px;
}


.remove-btn {
  background: none;
  border: none;
  color: #ff4d4f;
  font-size: 20px;
  cursor: pointer;
  margin-top: 15px;
}

.error-message {
  color: #ff4d4f;
  margin-top: 8px;
  font-size: 12px;
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 6px 16px;
  margin: 0 auto -20px auto;
  background: linear-gradient(135deg, #40a9ff 0%, #1890ff 100%);
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s;
  white-space: nowrap;
  /* 防止文字换行 */
}

.button:hover {
  background-color: #1890ff;
  transform: translateY(-1px);
}

.image-placeholder {
  height: 200px;
  /* 固定高度 */
  width: 100%;
  /* 宽度填满容器 */
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f5f5f5;
  /* 与卡片header背景一致 */
  overflow: hidden;
  /* 防止图片溢出 */
  position: relative;
  border-radius: 0 0 6px 6px;
  /* 与卡片圆角匹配 */
}

.image-placeholder img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  /* 保持比例完整显示图片 */
  object-position: center;
  transition: transform 0.3s ease;
  /* 添加悬停效果 */
}

/* 悬停时轻微放大 */
.image-placeholder:hover img {
  transform: scale(1.02);
}

/* 无图片时的占位样式 */
.image-placeholder span {
  color: #999;
  font-size: 14px;
  padding: 8px 12px;
  background-color: #fafafa;
  border-radius: 4px;
}

/* 特定图片的定制样式（如果需要） */
.dose-img {
  /* 可以添加特定滤镜效果 */
  filter: grayscale(20%);
  cursor: pointer;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .card-container {
    flex-direction: column;
  }

  .simple-card {
    min-width: auto;
  }
}
</style>