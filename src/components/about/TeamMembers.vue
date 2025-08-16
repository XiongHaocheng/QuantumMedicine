<template>
    <section class="about-section">
        <h2 class="intro-title">指导老师</h2>

        <!-- 第一行：2 位指导老师 -->
        <div class="team-row row-two">
            <article class="member">
                <figure class="avatar-wrap">
                    <img src="@/assets/avatar/wangyan.jpg" alt="王艳" class="avatar" />
                </figure>
                <h3 class="name">王艳</h3>
                <p class="desc">
                    团队指导老师；四川大学计算机学院教授、博士生导师、软件工程系主任，深度学习和智能医学研究专家，拥有多篇论文及专利。
                </p>
            </article>

            <article class="member">
                <figure class="avatar-wrap">
                    <img src="@/assets/avatar/wangpeng.jpg" alt="王鹏" class="avatar" />
                </figure>
                <h3 class="name">王鹏</h3>
                <p class="desc">
                    团队指导老师；四川大学计算机学院副教授、学生科科长；多类竞赛获奖团队指导老师，拥有多篇论文及专利。
                </p>
            </article>
        </div>
 <h2 class="intro-title">团队成员</h2>
        <!-- 第二行：5 位团队成员 -->
        <div class="team-row row-five">
            <article class="member">
                <figure class="avatar-wrap">
                    <img src="@/assets/avatar/zhouqi.jpg" alt="周琪" class="avatar" />
                </figure>
                <h3 class="name">周琪</h3>
                <p class="desc">
                    团队队长；四川大学计算机学院优秀学生、曾担任国家级学生创新项目负责人。
                </p>
            </article>

            <article class="member">
                <figure class="avatar-wrap">
                    <img src="@/assets/avatar/xionghaocheng.jpg" alt="熊浩宬" class="avatar" />
                </figure>
                <h3 class="name">熊浩宬</h3>
                <p class="desc">
                    团队核心成员；四川大学计算机学院研究生在读，研究方向量子机器学习、医学重建。
                </p>
            </article>

            <article class="member">
                <figure class="avatar-wrap">
                    <img src="@/assets/avatar/guozheng.jpg" alt="郭政" class="avatar" />
                </figure>
                <h3 class="name">郭政</h3>
                <p class="desc">
                    团队核心成员；四川大学软件学院本科在读，获得多项国家级、省级奖项，参与模型重建和前端开发。
                </p>
            </article>

            <article class="member">
                <figure class="avatar-wrap">
                    <img src="@/assets/avatar/heyumeng.jpg" alt="和雨萌" class="avatar" />
                </figure>
                <h3 class="name">和雨萌</h3>
                <p class="desc">
                    团队成员；四川大学计算机学院大四学生，曾获得两项国家级奖项以及五项省级奖项，拥有一篇CCFC论文及一个处于优先审查阶段的专利。
                </p>
            </article>

            <article class="member">
                <figure class="avatar-wrap">
                    <img src="@/assets/avatar/luoxuwei.jpg" alt="罗旭威" class="avatar" />
                </figure>
                <h3 class="name">罗旭威</h3>
                <p class="desc">
                    团队成员；四川大学软件学院24级学生，量子网络分割模型核心成员，参与多项研究工作。
                </p>
            </article>
        </div>
    </section>
</template>

<script setup>
// 这里不再用 v-for，因为信息较多且结构分成了两组
</script>

<style scoped>
.intro-title {
    text-align: center;
    color: #1976d2;
    font-weight: 700;
    font-size: 1.6rem;
    margin-bottom: 24px;
}

.team-row {
    display: grid;
    gap: 28px 32px;
    margin-bottom: 36px;
    align-items: start;
}

.row-two {
    display: grid;
    grid-template-columns: repeat(2, 260px);
    /* 老师卡片宽度更大 */
    gap: 28px 180px;
    /* 间距可根据需要调整 */
    justify-content: center;
    margin-bottom: 36px;
    align-items: start;
}

.row-five {
    grid-template-columns: repeat(5, 1fr);
    /* 学生卡片宽度自适应 */
}

.member {
    text-align: center;
    background: #fff;
    border-radius: 20px;
    padding: 28px 12px 22px;
    /* 老师卡片更窄时内边距略小 */
    box-shadow:
        0 1px 2px rgba(0, 0, 0, 0.05),
        0 8px 24px rgba(0, 0, 0, 0.06);
    display: flex;
    flex-direction: column;
    height: 340px;
}

.row-two .member {
    width: 260px;
    /* 同步宽度 */
    min-width: 0;
    max-width: 100%;
    height: 300px;
    /* 老师卡片高度更短 */
}

.row-five .member {
    width: auto;
    /* 学生卡片宽度自适应 */
}

.avatar-wrap {
    width: 140px;
    height: 140px;
    margin: 0 auto 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.avatar {
    width: 120px;
    height: 120px;
    object-fit: cover;
    border-radius: 50%;
    border: 2px solid #000000;
    /* 边框更细 */
    background: #fff;
}

.name {
    color: #111827;
    font-weight: 700;
    font-size: 18px;
    margin: 6px 0 4px;
    flex-shrink: 0;
}

.desc {
    color: #6b7280;
    font-size: 13px;
    line-height: 1.6;
    flex: 1 1 auto;
    /* 让描述自动填充剩余空间，保证底部对齐 */
}
</style>
