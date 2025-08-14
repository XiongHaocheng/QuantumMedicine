// HttpRequest.js
import axios from "axios";
import { ElMessage } from 'element-plus'; 

const httpRequest = axios.create({
  baseURL: "http://127.0.0.1:8080", // Flask 后端地址
  timeout: 100000,
});

// 请求拦截器
httpRequest.interceptors.request.use(
  config => {
    return config;
  },
  error => Promise.reject(error)
);

// 响应拦截器
httpRequest.interceptors.response.use(
  response => {
    if (response.data.status === "success") {
      return response.data; // 返回整个数据对象
    } else {
      ElMessage.error(response.data.message || "请求错误");
      return Promise.reject(response.data.message);
    }
  },
  error => {
    ElMessage.error(error.message || "请求失败");
    return Promise.reject(error);
  }
);

export default httpRequest;
