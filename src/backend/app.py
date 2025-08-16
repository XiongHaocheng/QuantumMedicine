import shutil
from flask import Flask, request, jsonify, send_from_directory
import paramiko
import os
import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有来源

UPLOAD_DIR = os.path.abspath("./uploads")  # 上传目录
RESULTS_DIR = os.path.abspath("../assets/Reconstruction")  # 下载图片存放目录（静态访问）

REMOTE_DATA_DIR = "/root/autodl-tmp/xhc/data/test"
REMOTE_RESULTS_DIR = "/root/autodl-tmp/xhc/test_results/best"

SSH_HOST = "connect.nmb2.seetacloud.com"
SSH_PORT = 46245
SSH_USER = "root"
SSH_PASSWORD = "yIGCqziSYpNw"

# 确保目录存在
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# PSNR 和 SSIM值计算
def calculate_metrics(lowdose_path, recon_path):
    img1 = cv2.imread(lowdose_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(recon_path, cv2.IMREAD_GRAYSCALE)
    psnr_val = cv2.PSNR(img1, img2)
    ssim_val = ssim(img1, img2)
    return round(psnr_val, 2), round(ssim_val, 3)

# 提供静态访问接口
@app.route("/results/<filename>")
def get_result(filename):
    return send_from_directory(RESULTS_DIR, filename)

# 上传并运行
@app.route("/upload-run", methods=["POST"])
def upload_and_run():
    file = request.files.get("file")
    if not file:
        return jsonify({"status": "error", "message": "未收到文件"})

    # 清空 uploads 文件夹
    for f in os.listdir(UPLOAD_DIR):
        path = os.path.join(UPLOAD_DIR, f)
        if os.path.isfile(path):
            os.unlink(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

    local_path = os.path.join(UPLOAD_DIR, file.filename)
    file.save(local_path)

    try:
        # SSH 上传
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(SSH_HOST, SSH_PORT, SSH_USER, SSH_PASSWORD)

        sftp = ssh.open_sftp()
        # 确保远程目录存在
        try:
            sftp.chdir(REMOTE_DATA_DIR)
        except IOError:
            sftp.mkdir(REMOTE_DATA_DIR)
            sftp.chdir(REMOTE_DATA_DIR)

        # 清空远程目录
        for f in sftp.listdir(REMOTE_DATA_DIR):
            try:
                sftp.remove(f"{REMOTE_DATA_DIR}/{f}")
            except IOError:
                pass

        # 上传新文件
        remote_path = f"{REMOTE_DATA_DIR}/{file.filename}"
        sftp.put(local_path, remote_path)
        sftp.close()

        # 执行远程命令
        commands = [
            f"cd /root/autodl-tmp/xhc",
            "source /root/miniconda3/etc/profile.d/conda.sh",
            "conda activate py39",
            f"python data_preparation.py --dataset_dir data/test --dataset_dst_path data/test.pickle",
            f"python main.py --phase test --dataset_dir ./data --data_test_name test.pickle --model_name GAN --generator_name UNet --batch_size 4 --gpu 0 --test_dir ./test_results --task_label best"
        ]
        full_command = " && ".join(commands)
        stdin, stdout, stderr = ssh.exec_command(full_command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        # 下载生成图片到 RESULTS_DIR
        sftp = ssh.open_sftp()
        try:
            lowdose_remote = f"{REMOTE_RESULTS_DIR}/batch0_sample0_lowdose.png"
            recon_remote = f"{REMOTE_RESULTS_DIR}/batch0_sample0_recon.png"
            stand_remote = f"{REMOTE_RESULTS_DIR}/batch0_sample0_standard.png"

            LOCAL_LOWDOSE_PATH = os.path.join(RESULTS_DIR, "lowdose.png")
            LOCAL_RECON_PATH = os.path.join(RESULTS_DIR, "recon.png")
            LOCAL_STAND_PATH = os.path.join(RESULTS_DIR, "stand.png")

            sftp.get(lowdose_remote, LOCAL_LOWDOSE_PATH)
            sftp.get(recon_remote, LOCAL_RECON_PATH)
            sftp.get(stand_remote, LOCAL_STAND_PATH)

        finally:
            sftp.close()
            ssh.close()

        # 计算指标
        psnr_val, ssim_val = calculate_metrics(LOCAL_STAND_PATH, LOCAL_RECON_PATH)

        # 返回可直接访问的 URL
        base_url = "http://localhost:8080/results"
        return jsonify({
            "status": "success",
            "output": output,
            "error": error,
            "lowdose_path": f"{base_url}/lowdose.png",
            "recon_path": f"{base_url}/recon.png",
            "stand_path": f"{base_url}/stand.png",
            "psnr": psnr_val,
            "ssim": ssim_val
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
