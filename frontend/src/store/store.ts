import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import type { User, Conversation, Message } from '@/types'

interface AppState {
  // 用户状态
  user: User | null
  isAuthenticated: boolean
  
  // 对话状态
  conversations: Conversation[]
  currentConversationId: string | null
  messages: Message[]
  
  // UI状态
  isLoading: boolean
  error: string | null
  
  // 动作
  setUser: (user: User | null) => void
  setConversations: (conversations: Conversation[]) => void
  addConversation: (conversation: Conversation) => void
  setCurrentConversation: (id: string) => void
  addMessage: (message: Message) => void
  setMessages: (messages: Message[]) => void
  setLoading: (loading: boolean) => void
  setError: (error: string | null) => void
  logout: () => void
}

export const useAppStore = create<AppState>()(
  persist(
    (set, get) => ({
      // 初始状态
      user: null,
      isAuthenticated: false,
      conversations: [],
      currentConversationId: null,
      messages: [],
      isLoading: false,
      error: null,
      
      // 动作实现
      setUser: (user) => set({ 
        user, 
        isAuthenticated: !!user 
      }),
      
      setConversations: (conversations) => set({ conversations }),
      
      addConversation: (conversation) => set((state) => ({
        conversations: [conversation, ...state.conversations]
      })),
      
      setCurrentConversation: (id) => set({ 
        currentConversationId: id 
      }),
      
      addMessage: (message) => set((state) => ({
        messages: [...state.messages, message]
      })),
      
      setMessages: (messages) => set({ messages }),
      
      setLoading: (isLoading) => set({ isLoading }),
      
      setError: (error) => set({ error }),
      
      logout: () => set({
        user: null,
        isAuthenticated: false,
        conversations: [],
        currentConversationId: null,
        messages: [],
        error: null
      }),
    }),
    {
      name: 'travel-ai-store',
      partialize: (state) => ({
        user: state.user,
        isAuthenticated: state.isAuthenticated,
      }),
    }
  )
)
