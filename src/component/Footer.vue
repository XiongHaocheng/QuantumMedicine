<template>
  <footer class="footer">
            <div class="logo-area">
            <img class="logo" src="@/assets/logo.png" />
            <span class="brand-name">QUANTUM HEALTHCARE</span>
        </div>
    <div class="footer-top">
      <!-- 第一行 -->
      <div class="footer-row">
        <div class="footer-title">团队介绍</div>
        <div class="footer-links">
          <router-link to="/about" class="footer-link">团队介绍</router-link>
          <span class="separator">|</span>
          <a href="#" class="footer-link">团队资质</a>
          <span class="separator">|</span>
          <a href="#" class="footer-link">行业资讯</a>
          <span class="separator">|</span>
          <a href="#" class="footer-link">联系我们</a>
        </div>
      </div>

      <!-- 第二行 -->
      <div class="footer-row">
        <div class="footer-title">解决方案</div>
        <div class="footer-links">
          <router-link to="/reconstruction" class="footer-link">重建技术</router-link>
          <span class="separator">|</span>
          <router-link to="/segmentation" class="footer-link">分割技术</router-link>
          <span class="separator">|</span>
          <router-link to="/dose-prediction" class="footer-link">剂量预测技术</router-link>
          <span class="separator">|</span>
          <router-link to="/quantum" class="footer-link">量子介绍</router-link>
        </div>
      </div>

      <!-- 第三行 -->
      <div class="footer-row address-contact">
        <div class="footer-title">团队地址</div>
        <div class="footer-text address">四川省成都市四川大学</div>

        <div class="footer-title contact-title">联系方式</div>
        <div class="footer-text contact">电话：+86 123 4567 8901</div>
      </div>
    </div>

    <!-- 分割线 -->
    <hr class="footer-divider" />

    <!-- 底部版权 -->
    <div class="footer-bottom">
      版权所有 © 四川大学
    </div>
  </footer>
</template>

<script setup>
// 这里不需要特殊逻辑，纯静态展示
</script>

<style scoped>
.footer {
  background-color: rgba(20, 30, 60, 0.75);
  color: #ccc;
  padding: 32px 200px;
  font-family: "Microsoft YaHei", sans-serif;
  user-select: none;
  font-size: 14px;
}
.logo-area {
    display: flex;
    align-items: center;
    margin-bottom: 12px;
}

.logo {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    margin-right: 12px;
}
.brand-name {
    font-size: 1.1rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: #ccc;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.18);
}
.footer-top {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.footer-row {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}

.footer-title {
  color: #40a9ff;
  font-weight: 700;
  min-width: 100px;
  flex-shrink: 0;
  font-size: 16px;
}

.footer-links {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.footer-link {
  color: #ccc;
  text-decoration: none;
  cursor: pointer;
  transition: color 0.3s ease;
}

.footer-link:hover {
  color: #40a9ff;
}

.separator {
  color: #ccc;
  user-select: none;
}

.address-contact {
  justify-content: flex-start;
  gap: 40px;
  flex-wrap: nowrap;
  margin-top: 8px;
}

.footer-text {
  color: #ccc;
  white-space: nowrap;
}

.contact-title {
  min-width: 80px;
}

.footer-divider {
  border: none;
  border-top: 2px solid #ccc;
  margin: 24px 0 16px;
  width: 100%;
}

.footer-bottom {
  text-align: center;
  font-size: 13px;
  color: #ccc;
}
@media (max-width: 768px) {
  .footer-top {
    gap: 24px;
  }

  .footer-row {
    flex-direction: column;
    align-items: flex-start;
  }

  .address-contact {
    flex-direction: column;
    gap: 8px;
  }

  .footer-title {
    min-width: auto;
  }
}
</style>
