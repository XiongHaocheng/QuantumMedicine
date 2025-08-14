import httpRequest from "@/apis/HttpRequest.js";

// 上传文件并运行远程脚本
export const uploadAndRun = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return httpRequest.post("/upload-run", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  })
  .then(res => res)
  .catch(err => {
    console.error("请求失败:", err);
    throw err;
  });
};
