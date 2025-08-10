import axios from 'axios'
import type { LoginCredentials, RegisterData, AuthToken, User, ChatResponse } from '@/types'

// 创建axios实例
const api = axios.create({
  baseURL: '/api/v1',
  timeout: 10000,
})

// 请求拦截器 - 添加认证token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// 响应拦截器 - 处理错误
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // 清除过期token
      localStorage.removeItem('access_token')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

// 认证API
export const authAPI = {
  login: async (credentials: LoginCredentials): Promise<AuthToken> => {
    const response = await api.post('/auth/login', credentials)
    return response.data
  },
  
  register: async (data: RegisterData) => {
    const response = await api.post('/auth/register', data)
    return response.data
  },
  
  getCurrentUser: async (): Promise<User> => {
    const response = await api.get('/auth/me')
    return response.data
  },
}

// 对话API
export const chatAPI = {
  sendMessage: async (message: string, userId: string): Promise<ChatResponse> => {
    const response = await api.post('/chat/send', {
      content: message,
      user_id: userId,
    })
    return response.data
  },
  
  getChatHistory: async (userId: string, limit = 20) => {
    const response = await api.get(`/chat/history/${userId}`, {
      params: { limit }
    })
    return response.data
  },
}

// 用户API
export const userAPI = {
  getProfile: async (): Promise<User> => {
    const response = await api.get('/users/profile')
    return response.data
  },
  
  updatePreferences: async (preferences: any) => {
    const response = await api.put('/users/preferences', preferences)
    return response.data
  },
  
  getTravelPlans: async () => {
    const response = await api.get('/users/travel-plans')
    return response.data
  },
}

export default api
