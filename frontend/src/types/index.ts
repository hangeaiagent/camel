// 通用类型定义

export interface User {
  user_id: string
  username: string
  email: string
  created_at: string
  preferences?: UserPreferences
}

export interface UserPreferences {
  preferred_languages: string[]
  travel_style: string
  budget_range: string
  favorite_destinations: string[]
}

export interface Message {
  id: string
  type: 'user' | 'assistant'
  content: string
  timestamp: Date
  metadata?: any
}

export interface ChatResponse {
  response_id: string
  content: string
  intent: string
  entities: Record<string, any>
  suggestions: string[]
  timestamp: string
}

export interface Conversation {
  conversation_id: string
  user_id: string
  title: string
  status: string
  created_at: string
  updated_at: string
  message_count: number
}

export interface TravelPlan {
  plan_id: string
  user_id: string
  title: string
  destination: string
  duration: string
  budget: string
  plan_data: Record<string, any>
  status: string
  created_at: string
}

export interface LoginCredentials {
  username: string
  password: string
}

export interface RegisterData {
  username: string
  email: string
  password: string
  confirm_password: string
}

export interface AuthToken {
  access_token: string
  token_type: string
  expires_in: number
  user_id: string
}

export interface ApiResponse<T = any> {
  data?: T
  message?: string
  error?: string
  status: number
}
