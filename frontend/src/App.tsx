import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import { Layout } from 'antd'

import { useAppStore } from '@/store/store'
import Header from '@/components/Header'
import ChatInterface from '@/components/ChatInterface'
import LoginPage from '@/components/LoginPage'
import ProfilePage from '@/components/ProfilePage'

const { Content } = Layout

function App() {
  const { isAuthenticated } = useAppStore()

  return (
    <Layout className="app-layout" style={{ minHeight: '100vh' }}>
      <Header />
      <Content style={{ padding: '0' }}>
        <Routes>
          <Route 
            path="/login" 
            element={isAuthenticated ? <Navigate to="/" replace /> : <LoginPage />} 
          />
          <Route 
            path="/profile" 
            element={isAuthenticated ? <ProfilePage /> : <Navigate to="/login" replace />} 
          />
          <Route 
            path="/" 
            element={isAuthenticated ? <ChatInterface /> : <Navigate to="/login" replace />} 
          />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Content>
    </Layout>
  )
}

export default App
