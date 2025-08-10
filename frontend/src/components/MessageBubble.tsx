import React from 'react'
import { Avatar, Card, Tag } from 'antd'
import { UserOutlined, RobotOutlined } from '@ant-design/icons'
import ReactMarkdown from 'react-markdown'
import type { Message } from '@/types'

interface MessageBubbleProps {
  message: Message
}

const MessageBubble: React.FC<MessageBubbleProps> = ({ message }) => {
  const isUser = message.type === 'user'
  
  const formatTime = (timestamp: Date) => {
    return timestamp.toLocaleTimeString('zh-CN', { 
      hour: '2-digit', 
      minute: '2-digit' 
    })
  }

  const renderTravelPlan = (planData: any) => {
    if (!planData || !planData.itinerary) return null

    return (
      <Card 
        size="small" 
        title="🗺️ 旅行计划"
        style={{ marginTop: '12px', background: '#f8f9fa' }}
      >
        <div>
          <p><strong>目的地:</strong> {planData.destination}</p>
          <p><strong>时长:</strong> {planData.duration}</p>
          <p><strong>预算:</strong> {planData.budget}</p>
          
          {planData.daily_plans && (
            <div style={{ marginTop: '12px' }}>
              <h4>行程安排:</h4>
              {planData.daily_plans.map((day: any, index: number) => (
                <div key={index} style={{ marginBottom: '8px' }}>
                  <Tag color="blue">第{index + 1}天</Tag>
                  <span>{day.location}: {day.activities?.join(', ')}</span>
                </div>
              ))}
            </div>
          )}
          
          {planData.suggestions && planData.suggestions.length > 0 && (
            <div style={{ marginTop: '12px' }}>
              <h4>建议:</h4>
              {planData.suggestions.map((suggestion: string, index: number) => (
                <Tag key={index} style={{ margin: '2px' }}>
                  {suggestion}
                </Tag>
              ))}
            </div>
          )}
        </div>
      </Card>
    )
  }

  return (
    <div className={`message ${message.type}`}>
      {!isUser && (
        <Avatar 
          size={32} 
          icon={<RobotOutlined />} 
          style={{ 
            background: '#1677ff',
            flexShrink: 0
          }} 
        />
      )}
      
      <div className="message-content">
        <div style={{ wordWrap: 'break-word' }}>
          {isUser ? (
            message.content
          ) : (
            <ReactMarkdown>{message.content}</ReactMarkdown>
          )}
        </div>
        
        {/* 渲染旅行计划（如果有） */}
        {!isUser && message.metadata?.type === 'travel_plan' && 
          renderTravelPlan(message.metadata.plan)
        }
        
        {/* 显示意图和实体（开发调试用） */}
        {!isUser && message.metadata && process.env.NODE_ENV === 'development' && (
          <div style={{ 
            marginTop: '8px', 
            fontSize: '12px', 
            color: '#666',
            padding: '4px 8px',
            background: '#f0f0f0',
            borderRadius: '4px'
          }}>
            <div>意图: {message.metadata.intent}</div>
            {Object.keys(message.metadata.entities || {}).length > 0 && (
              <div>实体: {JSON.stringify(message.metadata.entities)}</div>
            )}
          </div>
        )}
        
        <div className="message-time">
          {formatTime(message.timestamp)}
        </div>
      </div>
      
      {isUser && (
        <Avatar 
          size={32} 
          icon={<UserOutlined />} 
          style={{ 
            background: '#52c41a',
            flexShrink: 0
          }} 
        />
      )}
    </div>
  )
}

export default MessageBubble
