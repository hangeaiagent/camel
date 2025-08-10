import React from 'react'
import { Avatar } from 'antd'
import { RobotOutlined } from '@ant-design/icons'

const TypingIndicator: React.FC = () => {
  return (
    <div className="message assistant">
      <Avatar 
        size={32} 
        icon={<RobotOutlined />} 
        style={{ 
          background: '#1677ff',
          flexShrink: 0
        }} 
      />
      
      <div className="typing-indicator">
        <span style={{ marginRight: '8px', color: '#666' }}>AI正在思考</span>
        <div className="typing-dots">
          <div className="typing-dot"></div>
          <div className="typing-dot"></div>
          <div className="typing-dot"></div>
        </div>
      </div>
    </div>
  )
}

export default TypingIndicator
