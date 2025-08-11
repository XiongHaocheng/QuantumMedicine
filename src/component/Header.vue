<template>
    <header class="header">
        <!-- 左侧 Logo及名称 -->
        <div class="logo-area">
            <img class="logo" src="@/assets/logo.png" />
            <span class="brand-name">QUANTUM HEALTHCARE</span>
        </div>

        <!-- 中间导航栏 -->
        <nav class="nav-menu">
            <a v-for="item in menuItems" :key="item.value" :href="item.href"
                :class="['nav-link', { active: menu2Value === item.value }]" @click.prevent="menu2Value = item.value">
                {{ item.label }}
                <span v-if="menu2Value === item.value" class="active-underline"></span>
            </a>
        </nav>

        <!-- 右侧个人中心 -->
        <div class="user-center">
            <router-link to="/profile" class="icon-link">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z" />
                </svg>
            </router-link>
        </div>
    </header>
</template>

<script setup>
import { ref } from 'vue'

const menu2Value = ref('item1')
const menuItems = [
    { value: 'item1', label: '首页', href: '#' },
    { value: 'item2', label: '重建技术', href: '#' },
    { value: 'item3', label: '分割技术', href: '#' },
    { value: 'item4', label: '剂量预测技术', href: '#' },
    { value: 'item5', label: '量子介绍', href: '#' },
    { value: 'item6', label: '关于我们', href: '#' }
]
</script>

<style scoped>
.header {
    width: 100%;
    background: rgba(20, 30, 60, 0.75);
    /* 半透明深色背景 */
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 32px;
    height: 72px;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 100;
    backdrop-filter: blur(8px);
    /* 毛玻璃效果，可选 */
}

.logo-area {
    display: flex;
    align-items: center;
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
    color: #fff;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.18);
}

.nav-menu {
    flex: 1;
    display: flex;
    justify-content: center;
    gap: 32px;
    background: transparent;
}

.nav-link {
    position: relative;
    color: #fff;
    font-size: 1.05rem;
    font-weight: 500;
    text-decoration: none;
    padding: 0 6px;
    transition: color 0.2s;
    cursor: pointer;
    line-height: 48px;
}

.nav-link:hover {
    color: #40a9ff;
}

.nav-link.active {
    font-weight: 700;
    color: #40a9ff;
}

.active-underline {
    position: absolute;
    left: 0;
    bottom: 6px;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, #40a9ff 0%, #1976d2 100%);
    border-radius: 2px;
    animation: underline-in 0.4s cubic-bezier(.68, -0.55, .27, 1.55);
}

@keyframes underline-in {
    from {
        width: 0;
        opacity: 0;
    }

    to {
        width: 100%;
        opacity: 1;
    }
}

.user-center a {
    color: white;
    text-decoration: none;
}
</style>
