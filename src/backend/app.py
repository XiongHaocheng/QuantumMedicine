from flask import Flask, request, jsonify
import paramiko
import os
import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np

from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # 允许所有来源


UPLOAD_DIR = os.path.abspath("./uploads")  # 本地根目录下的 uploads 文件夹
REMOTE_DATA_DIR = "/root/autodl-tmp/xhc/data/test"
REMOTE_RESULTS_DIR = "/root/autodl-tmp/xhc/test_results/best"

SSH_HOST = "connect.nmb2.seetacloud.com"
SSH_PORT = 46245
SSH_USER = "root"
SSH_PASSWORD = "yIGCqziSYpNw"

LOCAL_LOWDOSE_PATH = os.path.abspath("../assets/Reconstruction/lowdose.png")
LOCAL_RECON_PATH = os.path.abspath("../assets/Reconstruction/recon.png")
LOCAL_STAND_PATH = os.path.abspath("../assets/Reconstruction/stand.png")

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)
# PSNR 和 SSIM值计算
def calculate_metrics(lowdose_path, recon_path):
    # 读取灰度图
    img1 = cv2.imread(lowdose_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(recon_path, cv2.IMREAD_GRAYSCALE)
    # PSNR
    psnr_val = cv2.PSNR(img1, img2)
    # SSIM
    ssim_val = ssim(img1, img2)
    return round(psnr_val, 2), round(ssim_val, 3)

# 上传pet文件到服务器并测试获取结果
@app.route("/upload-run", methods=["POST"])
def upload_and_run():
    file = request.files.get("file")
    if not file:
        return jsonify({"status": "error", "message": "未收到文件"})
    
    local_path = os.path.join(UPLOAD_DIR, file.filename)
    file.save(local_path)  # 保存到 Flask 根目录 ./uploads/文件名

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

        # 清空远程目录下的所有文件
        for filename in sftp.listdir(REMOTE_DATA_DIR):
            file_path = REMOTE_DATA_DIR + '/' + filename
            try:
                sftp.remove(file_path)
            except IOError:
                pass  # 忽略文件删除错误

        # 上传新文件
        remote_path = REMOTE_DATA_DIR + '/' + file.filename
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
        print(output)
        error = stderr.read().decode()

        # 下载生成图片
        sftp = ssh.open_sftp()
        try:
            lowdose_remote = REMOTE_RESULTS_DIR + '/' + "batch0_sample0_lowdose.png"
            recon_remote = REMOTE_RESULTS_DIR + '/' + "batch0_sample0_recon.png"
            stand_remote = REMOTE_RESULTS_DIR + '/' + "batch0_sample0_standard.png"
            # print("尝试下载低剂量图片，远程路径:", lowdose_remote)
            # print("尝试下载重建图片，远程路径:", recon_remote)

            sftp.get(lowdose_remote, LOCAL_LOWDOSE_PATH)
            sftp.get(recon_remote, LOCAL_RECON_PATH)
            sftp.get(stand_remote, LOCAL_STAND_PATH)

            print("图片下载成功，本地路径:", LOCAL_LOWDOSE_PATH, LOCAL_RECON_PATH, LOCAL_STAND_PATH)
        except IOError as e:
            print("下载图片失败:", e)
        finally:
            sftp.close()
            ssh.close()

        # 计算指标
        psnr_val, ssim_val = calculate_metrics(LOCAL_STAND_PATH, LOCAL_RECON_PATH)

        return jsonify({"status": "success", "output": output, "error": error,
                        "lowdose_path": LOCAL_LOWDOSE_PATH,
                        "recon_path": LOCAL_RECON_PATH,
                        "stand_path": LOCAL_STAND_PATH,
                        "psnr": psnr_val,
                        "ssim": ssim_val
                        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
