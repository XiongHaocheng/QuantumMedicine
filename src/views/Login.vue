<template>
    <div class="quantum-bg">
        <canvas ref="canvas" class="bg-canvas"></canvas>
        <div class="auth-container">
            <!-- 左侧介绍区 -->
            <div class="intro-section">
                <div class="intro-content">
                    <div style="display: flex;align-items: center;width: 50vw;">
                    <img class="logo" src="@/assets/logo.png" />
                    <h2>QUANTUM HEALTHCARE</h2>
                    </div>
                    <p>
                        量子科技赋能医疗，<br>
                        引领智能健康新纪元。
                    </p>
                </div>
            </div>
            <!-- 右侧登录卡片 -->
            <div class="form-wrapper">
                <div class="form-container">
                    <h1>登录</h1>
                    <form @submit.prevent="handleLogin">
                        <!-- 邮箱输入框 -->
                        <div class="input-group">
                            <span class="icon">
                                <!-- 邮箱图标 -->
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round">
                                    <rect x="2" y="4" width="20" height="16" rx="2"></rect>
                                    <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>
                                </svg>
                            </span>
                            <input v-model="form.mail" type="email" placeholder="邮箱" required>
                        </div>
                        <!-- 密码输入框 -->
                        <div class="input-group">
                            <span class="icon">
                                <!-- 密码图标 -->
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round">
                                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                                </svg>
                            </span>
                            <input v-model="form.password" :type="passwordVisible ? 'text' : 'password'"
                                placeholder="密码" required>
                            <!-- 切换密码可见性图标 -->
                            <span class="toggle-password" @click="passwordVisible = !passwordVisible">
                                <svg v-if="passwordVisible" xmlns="http://www.w3.org/2000/svg" width="20" height="20"
                                    viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"></path>
                                    <circle cx="12" cy="12" r="3"></circle>
                                </svg>
                                <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20"
                                    viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M9.88 9.88a3 3 0 1 0 4.24 4.24"></path>
                                    <path
                                        d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68">
                                    </path>
                                    <path d="M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61">
                                    </path>
                                    <line x1="2" x2="22" y1="2" y2="22"></line>
                                </svg>
                            </span>
                        </div>
                        <!-- 错误信息 -->
                        <div v-if="errorMsg" style="color:#ff6b81;text-align:center;margin-bottom:10px;">{{ errorMsg }}
                        </div>
                        <!-- 记住密码和忘记密码链接 -->
                        <div class="options">
                            <label class="checkbox-container">
                                <input type="checkbox" v-model="remember">
                                <span class="checkmark"></span>
                                记住密码
                            </label>
                            <router-link to="/forgot-password" class="forgot-password">忘记密码?</router-link>
                        </div>
                        <!-- 登录按钮 -->
                        <button type="submit" class="submit-btn" :disabled="loading">{{ loading ? '登录中...' : '登录'
                        }}</button>
                    </form>
                    <div class="separator"><span>或</span></div>
                    <p class="switch-form">没有账户? <router-link to="/register">注册</router-link></p>
                    <p class="footer-note">登录即表示您同意我们的<router-link to="/user-agreement">用户协议</router-link> 和
                        <router-link to="/privacy-policy">隐私政策</router-link>
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'

const form = ref({
    mail: '',
    password: ''
})
const passwordVisible = ref(false)
const errorMsg = ref('')
const loading = ref(false)
const remember = ref(false)
const router = useRouter()
const canvas = ref(null)
let animationId = null

function handleLogin() {
    errorMsg.value = ''
    loading.value = true
    setTimeout(() => {
        if (form.value.mail === 'admin@gmail.com' && form.value.password === '123456') {
            localStorage.setItem('isLogin', 'true')
            loading.value = false
            router.push('/home')
        } else {
            errorMsg.value = '邮箱或密码错误（账号：admin，密码：123456）'
            loading.value = false
        }
    }, 600)
}

// 粒子动画
function startQuantumParticles() {
    const ctx = canvas.value.getContext('2d')
    let w = canvas.value.width = window.innerWidth
    let h = canvas.value.height = window.innerHeight
    const particles = []
    const PARTICLE_NUM = 80
    const COLORS = ['#60a5fa', '#a78bfa', '#f472b6', '#38bdf8', '#facc15', '#fff']
    function randomBetween(a, b) { return a + Math.random() * (b - a) }
    for (let i = 0; i < PARTICLE_NUM; i++) {
        particles.push({
            x: Math.random() * w,
            y: Math.random() * h,
            r: randomBetween(1.5, 3.5),
            color: COLORS[Math.floor(Math.random() * COLORS.length)],
            vx: randomBetween(-0.7, 0.7),
            vy: randomBetween(-0.7, 0.7)
        })
    }
    function draw() {
        ctx.clearRect(0, 0, w, h)
        // 画粒子
        for (let p of particles) {
            ctx.beginPath()
            ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2)
            ctx.fillStyle = p.color
            ctx.shadowColor = p.color
            ctx.shadowBlur = 12
            ctx.globalAlpha = 0.85
            ctx.fill()
            ctx.globalAlpha = 1
            ctx.shadowBlur = 0
        }
        // 画连线
        for (let i = 0; i < PARTICLE_NUM; i++) {
            for (let j = i + 1; j < PARTICLE_NUM; j++) {
                const p1 = particles[i], p2 = particles[j]
                const dist = Math.hypot(p1.x - p2.x, p1.y - p2.y)
                if (dist < 110) {
                    ctx.beginPath()
                    ctx.moveTo(p1.x, p1.y)
                    ctx.lineTo(p2.x, p2.y)
                    ctx.strokeStyle = p1.color
                    ctx.globalAlpha = 0.12
                    ctx.lineWidth = 1
                    ctx.stroke()
                    ctx.globalAlpha = 1
                }
            }
        }
    }
    function update() {
        for (let p of particles) {
            p.x += p.vx
            p.y += p.vy
            if (p.x < 0 || p.x > w) p.vx *= -1
            if (p.y < 0 || p.y > h) p.vy *= -1
        }
    }
    function animate() {
        draw()
        update()
        animationId = requestAnimationFrame(animate)
    }
    animate()
    window.addEventListener('resize', resize)
    function resize() {
        w = canvas.value.width = window.innerWidth
        h = canvas.value.height = window.innerHeight
    }
    // 返回清理函数
    return () => {
        cancelAnimationFrame(animationId)
        window.removeEventListener('resize', resize)
    }
}

onMounted(() => {
    let cleanup = startQuantumParticles()
    onBeforeUnmount(() => {
        cleanup && cleanup()
    })
})
</script>

<style scoped>
.quantum-bg {
    position: fixed;
    inset: 0;
    width: 100vw;
    height: 100vh;
    z-index: 0;
    overflow: hidden;
    background: #181c24;
}

.bg-canvas {
    position: absolute;
    inset: 0;
    width: 100vw;
    height: 100vh;
    z-index: 1;
    pointer-events: none;
}

.auth-container {
    position: relative;
    z-index: 2;
    font-family: 'Noto Sans SC', sans-serif;
    display: flex;
    justify-content: center;
    align-items: stretch;
    min-height: 100vh;
    box-sizing: border-box;
    padding: 0;
    background: transparent;
}

.intro-section {
    flex: 1.2;
    background: rgba(24, 28, 36, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 48px 32px;
    min-width: 0;
    backdrop-filter: blur(2px);
    border-right: 1.5px solid rgba(80, 80, 120, 0.12);
}

.intro-content {
    max-width: 700px;
    color: #e0e7ef;
}

.intro-content h2 {
    font-size: 3.2rem;
    font-weight: 900;
    background: linear-gradient(90deg, #fff 60%, #bfc9d9 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-fill-color: transparent;
    margin-bottom: 30px;
    letter-spacing: 3px;
    text-shadow: 0 6px 32px #1e293b88;
}

.intro-content p {
    font-size: 2rem;
    color: #e5e7eb;
    font-weight: 700;
    margin-bottom: 24px;
    line-height: 1.5;
    letter-spacing: 1px;
    text-shadow: 0 2px 16px rgba(0, 0, 0, 0.3);
}

.intro-content ul {
    padding-left: 1.2em;
    color: #a5b4fc;
    font-size: 1.15rem;
    margin: 0;
    font-weight: 500;
}

.intro-content li {
    margin-bottom: 14px;
    list-style: disc;
}

.form-wrapper {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 340px;
    padding: 32px 16px;
    background: rgba(24, 28, 36, 0.7);
    backdrop-filter: blur(2px);
    border: 2.5px solid transparent;
    /* 设置为透明 */
}

.form-container {
    background-color: rgba(30, 41, 59, 0.98);
    padding: 40px;
    border-radius: 24px;
    box-shadow: 0 10px 32px 0 #0006;
    border: 2.5px solid #334155;
    width: 100%;
    max-width: 420px;
    box-sizing: border-box;
}

h1 {
    font-size: 28px;
    font-weight: 700;
    text-align: center;
    margin-top: 0;
    margin-bottom: 32px;
    color: #fff;
    letter-spacing: 2px;
}

.input-group {
    position: relative;
    margin-bottom: 20px;
}

.input-group .icon {
    position: absolute;
    left: 16px;
    top: 50%;
    transform: translateY(-50%);
    color: #64748b;
    pointer-events: none;
}

.input-group input {
    width: 100%;
    padding: 14px 14px 14px 48px;
    border: 1px solid #334155;
    border-radius: 12px;
    font-size: 15px;
    box-sizing: border-box;
    background-color: rgba(51, 65, 85, 0.7);
    color: #e0e7ef;
    transition: border-color 0.2s, box-shadow 0.2s;
}

.input-group input::placeholder {
    color: #94a3b8;
    opacity: 0.7;
}

.input-group input:focus {
    outline: none;
    border-color: #60a5fa;
    box-shadow: 0 0 0 3px #60a5fa33;
}

.toggle-password {
    position: absolute;
    right: 16px;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
    color: #64748b;
}

.options {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
    font-size: 14px;
    color: #94a3b8;
}

.checkbox-container {
    display: flex;
    align-items: center;
    cursor: pointer;
    position: relative;
    color: #94a3b8;
}

.checkbox-container input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
    height: 0;
    width: 0;
}

.checkmark {
    height: 20px;
    width: 20px;
    border: 2px solid #334155;
    border-radius: 50%;
    display: inline-block;
    margin-right: 10px;
    position: relative;
    background: #222b3a;
}

.checkbox-container input:checked~.checkmark {
    background-color: #60a5fa;
    border-color: #60a5fa;
}

.checkmark:after {
    content: "";
    position: absolute;
    display: none;
    left: 6px;
    top: 2px;
    width: 5px;
    height: 10px;
    border: solid white;
    border-width: 0 2px 2px 0;
    transform: rotate(45deg);
}

.checkbox-container input:checked~.checkmark:after {
    display: block;
}

.submit-btn {
    width: 100%;
    padding: 14px;
    background-color: #60a5fa;
    color: #fff;
    border: 1px solid #334155;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: background 0.2s;
}

.submit-btn:hover {
    background-color: #2563eb;
    color: #fff;
    transform: translateY(-1px);
}

.separator {
    display: flex;
    align-items: center;
    text-align: center;
    margin: 32px 0;
    color: #64748b;
}

.separator::before,
.separator::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid #334155;
}

.separator span {
    padding: 0 16px;
}

.switch-form {
    text-align: center;
    font-size: 15px;
    color: #64748b;
}

.switch-form a {
    color: #60a5fa;
}

.footer-note {
    text-align: center;
    font-size: 13px;
    color: #64748b;
    margin-top: 24px;
}

.footer-note a {
    color: #e0e7ef;
}
.logo {
    width: 64px;
    height: 64px;
    border-radius: 8px;
    margin-right: 20px;
    margin-top: 20px;
   }
@media (max-width: 900px) {
    .auth-container {
        flex-direction: column;
        align-items: stretch;
    }

    .intro-section {
        padding: 32px 12px;
        justify-content: flex-start;
        min-height: 180px;
        border-right: none;
        border-bottom: 1.5px solid rgba(80, 80, 120, 0.12);
    }

    .form-wrapper {
        padding: 24px 8px;
        min-width: 0;
    }
}
</style>