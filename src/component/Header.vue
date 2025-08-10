<template>
    <header class="header">
        <!-- 左侧 Logo -->
        <img class="logo" src="../../imgs/logo.png" />

        <!-- 中间导航栏 -->
        <t-head-menu v-model="menu2Value" height="120px" class="nav-menu">
            <t-menu-item value="item1" style="color:white;"> 首页 </t-menu-item>
            <t-menu-item value="item2" style="color:white;"> 重建技术 </t-menu-item>
            <t-menu-item value="item3" style="color:white;"> 分割技术 </t-menu-item>
            <t-menu-item value="item4" style="color:white;"> 剂量预测技术 </t-menu-item>
            <t-menu-item value="item5" style="color:white;"> 新闻资讯 </t-menu-item>
            <t-menu-item value="item6" style="color:white;"> 关于我们 </t-menu-item>
        </t-head-menu>

        <!-- 右侧个人中心 -->
        <div class="user-center">
            <router-link to="/profile" class="icon-link">
                <!-- 这里用 SVG 或者字体图标，比如 fontawesome 的用户图标 -->
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
</script>

<style scoped>
.header {
    background-color: rgb(0, 0, 0);
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 24px;
}

.logo {
    width: 5%;
    border-radius: 20px;
}

.nav-menu {
    flex: 1;
    display: flex;
    justify-content: center;
    background-color: rgb(0, 0, 0) !important;
}

:deep(.t-head-menu) {
    background-color: rgb(0, 0, 0) !important;
}

/* 点击选中的菜单项背景变蓝，文字保持白色 */
:deep(.t-menu__item.t-is-active) {
    background-color: #007bff !important;
    /* 蓝色背景 */
    color: white !important;
}

:deep(.t-menu__item:hover) {
    background-color: rgba(0, 123, 255, 0.2) !important;
    /* 悬停时浅蓝 */
    color: white !important;
}

.user-center a {
    color: white;
    text-decoration: none;
}
</style>
