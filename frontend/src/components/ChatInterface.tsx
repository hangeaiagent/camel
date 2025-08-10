import React, { useState, useEffect, useRef } from 'react'
import { Input, Button, Badge, Typography, Space } from 'antd'
import { SendOutlined, WifiOutlined } from '@ant-design/icons'
import { useAppStore } from '@/store/store'
import { useWebSocket } from '@/hooks/useWebSocket'
import MessageBubble from './MessageBubble'
import TypingIndicator from './TypingIndicator'
import type { Message } from '@/types'

const { Title } = Typography

const ChatInterface: React.FC = () => {
  const { user, messages, addMessage, setMessages } = useAppStore()
  const [inputValue, setInputValue] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const { sendMessage, connectionStatus } = useWebSocket(
    `ws://localhost:8000/ws/${user?.user_id}`,
    {
      onMessage: (data) => {
        if (data.type === 'response') {
          const assistantMessage: Message = {
            id: data.response_id || `msg_${Date.now()}`,
            type: 'assistant',
            content: data.content.text || data.content,
            timestamp: new Date(data.timestamp),
            metadata: data
          }
          addMessage(assistantMessage)
        }
        setIsLoading(false)
      },
      onError: (error) => {
        console.error('WebSocket error:', error)
        setIsLoading(false)
      }
    }
  )

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSend = () => {
    if (!inputValue.trim() || isLoading) return

    // 添加用户消息
    const userMessage: Message = {
      id: `user_${Date.now()}`,
      type: 'user',
      content: inputValue,
      timestamp: new Date()
    }

    addMessage(userMessage)
    setInputValue('')
    setIsLoading(true)

    // 发送到后端
    sendMessage(inputValue)
  }

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  const getStatusColor = () => {
    switch (connectionStatus) {
      case 'connected': return 'green'
      case 'connecting': return 'orange'
      case 'error': return 'red'
      default: return 'gray'
    }
  }

  const getStatusText = () => {
    switch (connectionStatus) {
      case 'connected': return '已连接'
      case 'connecting': return '连接中'
      case 'error': return '连接错误'
      default: return '未连接'
    }
  }

  return (
    <div className="chat-container">
      {/* 聊天头部 */}
      <div style={{ 
        padding: '16px 20px', 
        borderBottom: '1px solid #e8e8e8',
        background: 'white',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
      }}>
        <Space>
          <Title level={4} style={{ margin: 0 }}>
            Travel AI Assistant
          </Title>
          <span style={{ color: '#666', fontSize: '14px' }}>
            您的智能旅游规划助手
          </span>
        </Space>
        
        <Badge 
          color={getStatusColor()} 
          text={getStatusText()}
          style={{ fontSize: '12px' }}
        />
      </div>

      {/* 消息容器 */}
      <div className="messages-container">
        {messages.length === 0 && (
          <div style={{ 
            textAlign: 'center', 
            padding: '40px', 
            color: '#999' 
          }}>
            <div style={{ fontSize: '48px', marginBottom: '16px' }}>🧳</div>
            <h3>欢迎使用 Travel AI</h3>
            <p>我可以帮您规划完美的旅行路线，请告诉我您的需求！</p>
            <div style={{ marginTop: '20px' }}>
              <p style={{ fontSize: '14px', color: '#666' }}>试试这些问题：</p>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', justifyContent: 'center' }}>
                {[
                  '我想去日本旅游5天',
                  '推荐一个欧洲路线',
                  '制定预算1万元的计划'
                ].map((suggestion, index) => (
                  <Button 
                    key={index}
                    size="small" 
                    type="text"
                    onClick={() => setInputValue(suggestion)}
                    style={{ 
                      background: '#f5f5f5',
                      border: '1px solid #e8e8e8'
                    }}
                  >
                    {suggestion}
                  </Button>
                ))}
              </div>
            </div>
          </div>
        )}
        
        {messages.map(message => (
          <MessageBubble key={message.id} message={message} />
        ))}
        
        {isLoading && <TypingIndicator />}
        
        <div ref={messagesEndRef} />
      </div>

      {/* 输入区域 */}
      <div className="input-container">
        <Input.TextArea
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="输入您的旅行需求..."
          autoSize={{ minRows: 1, maxRows: 4 }}
          disabled={connectionStatus !== 'connected'}
          style={{ 
            borderRadius: '20px',
            padding: '12px 16px',
            resize: 'none'
          }}
        />
        <Button
          type="primary"
          icon={<SendOutlined />}
          onClick={handleSend}
          disabled={!inputValue.trim() || isLoading || connectionStatus !== 'connected'}
          style={{ 
            borderRadius: '20px',
            height: 'auto',
            padding: '12px 20px'
          }}
        >
          发送
        </Button>
      </div>
    </div>
  )
}

export default ChatInterface
