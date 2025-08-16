<template>
    <div class="quantum-overlay">
        <svg width="1000" height="250">
            <!-- 四条比特线和标签 -->
            <line v-for="(y, i) in [60, 110, 160, 210]" :key="'line' + i" x1="250" :y1="y" x2="750" :y2="y"
                stroke="#40a9ff" stroke-width="3" opacity="0">
                <animate attributeName="opacity" values="0;1" :begin="0.6 + i * 0.1 + 's'" dur="0.6s" fill="freeze" />
            </line>

            <text v-for="(y, i) in [60, 110, 160, 210]" :key="'text' + i" x="230" :y="y - 5" fill="white" font-size="14"
                opacity="0">
                {{ 'q' + i }}
                <animate attributeName="opacity" values="0;1" :begin="0.6 + i * 0.1 + 's'" dur="0.6s" fill="freeze" />
            </text>


            <!-- 预处理网络 -->
            <g opacity="0">
                <animate attributeName="opacity" values="0;1" dur="0.6s" begin="0s" fill="freeze" />
                <rect x="20" y="90" width="80" height="50" fill="#1890ff">
                    <animate attributeName="fill" values="#1890ff;#00ffff;#1890ff" dur="0.6s" begin="0s"
                        repeatCount="indefinite" />
                </rect>
                <text x="40" y="120" fill="white" font-size="12">3D池化</text>

                <rect x="120" y="90" width="80" height="50" fill="#1890ff">
                    <animate attributeName="fill" values="#1890ff;#00ffff;#1890ff" dur="0.6s" begin="0.6s"
                        repeatCount="indefinite" />
                </rect>
                <text x="135" y="120" fill="white" font-size="12">线性变化</text>
            </g>

            <!-- 门操作：RX, RY, RZ -->
            <g v-for="(gate, i) in gates" :key="i" :opacity="0">
                <rect :x="gate.x" :y="gate.y" width="60" height="30" fill="#1890ff" rx="5" ry="5" />
                <text :x="gate.x + 5" :y="gate.y + 20" fill="white" font-size="12">{{ gate.label }}</text>
                <animate attributeName="opacity" values="0;1" :begin="gate.begin" dur="0.6s" fill="freeze" />
            </g>

            <!-- CNOT门 -->
            <g v-for="(cnot, i) in cnots" :key="'cnot' + i" :opacity="0">
                <circle :cx="cnot.cx" :cy="cnot.cy1" r="8" fill="#40a9ff" />
                <line :x1="cnot.cx" :y1="cnot.cy1" :x2="cnot.cx" :y2="cnot.cy2" stroke="#40a9ff" stroke-width="2" />
                <circle :cx="cnot.cx" :cy="cnot.cy2" r="12" stroke="#40a9ff" stroke-width="2" fill="none" />
                <line :x1="cnot.cx - 12" :y1="cnot.cy2" :x2="cnot.cx + 12" :y2="cnot.cy2" stroke="#40a9ff"
                    stroke-width="2" />
                <line :x1="cnot.cx" :y1="cnot.cy2 - 12" :x2="cnot.cx" :y2="cnot.cy2 + 12" stroke="#40a9ff"
                    stroke-width="2" />
                <animate attributeName="opacity" values="0;1" :begin="cnot.begin" dur="0.6s" fill="freeze" />
            </g>

            <!-- 测量 M -->
            <g v-for="(y, i) in [60, 110, 160, 210]" :key="'m' + i" :opacity="0">
                <rect x="710" :y="y - 15" width="25" height="25" fill="#ff6347" rx="4" ry="4" />
                <text x="715" :y="y + 5" fill="white" font-size="12">M</text>
                <animate attributeName="opacity" values="0;1" :begin="2.2 + i * 0.2 + 's'" dur="0.6s" fill="freeze" />
            </g>

            <!-- 后处理网络 -->
            <g opacity="0">
                <animate attributeName="opacity" values="0;1" dur="0.6s" begin="2.8s" fill="freeze" />
                <rect x="800" y="100" width="80" height="50" fill="#52c41a">
                    <animate attributeName="fill" values="#52c41a;#a0ffa0;#52c41a" dur="0.6s" begin="2.8s"
                        repeatCount="indefinite" />
                </rect>
                <text x="815" y="130" fill="white" font-size="12">全连接层</text>

                <rect x="900" y="100" width="80" height="50" fill="#52c41a">
                    <animate attributeName="fill" values="#52c41a;#a0ffa0;#52c41a" dur="0.6s" begin="3.4s"
                        repeatCount="indefinite" />
                </rect>
                <text x="915" y="130" fill="white" font-size="12">全连接层</text>
            </g>
        </svg>
        <p class="loading-text">量子线路运算中...</p>
    </div>
</template>

<script setup>
const gates = [
    { x: 260, y: 40, label: 'RX(00)', begin: '0.6s' },
    { x: 260, y: 90, label: 'RX(03)', begin: '0.7s' },
    { x: 260, y: 140, label: 'RX(06)', begin: '0.8s' },
    { x: 260, y: 190, label: 'RX(09)', begin: '0.9s' },

    { x: 340, y: 40, label: 'RY(01)', begin: '1.0s' },
    { x: 340, y: 90, label: 'RY(04)', begin: '1.1s' },
    { x: 340, y: 140, label: 'RY(07)', begin: '1.2s' },
    { x: 340, y: 190, label: 'RY(10)', begin: '1.3s' },

    { x: 420, y: 40, label: 'RZ(02)', begin: '1.4s' },
    { x: 420, y: 90, label: 'RZ(05)', begin: '1.5s' },
    { x: 420, y: 140, label: 'RZ(08)', begin: '1.6s' },
    { x: 420, y: 190, label: 'RZ(11)', begin: '1.7s' },
];

const cnots = [
    { cx: 500, cy1: 60, cy2: 110, begin: '1.8s' },
    { cx: 580, cy1: 110, cy2: 160, begin: '1.9s' },
    { cx: 660, cy1: 160, cy2: 210, begin: '2.0s' },
];
</script>

<style scoped>
.quantum-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.85);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 9999;
}

.loading-text {
    margin-top: 16px;
    color: white;
    font-size: 18px;
}
</style>