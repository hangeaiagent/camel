import React from 'react'
import { Layout, Button, Avatar, Dropdown, Space } from 'antd'
import { UserOutlined, LogoutOutlined, SettingOutlined } from '@ant-design/icons'
import { useNavigate } from 'react-router-dom'
import { useAppStore } from '@/store/store'

const { Header: AntHeader } = Layout

const Header: React.FC = () => {
  const navigate = useNavigate()
  const { user, logout, isAuthenticated } = useAppStore()

  const handleLogout = () => {
    logout()
    localStorage.removeItem('access_token')
    navigate('/login')
  }

  const userMenuItems = [
    {
      key: 'profile',
      icon: <UserOutlined />,
      label: '个人资料',
      onClick: () => navigate('/profile'),
    },
    {
      key: 'settings',
      icon: <SettingOutlined />,
      label: '设置',
      onClick: () => navigate('/settings'),
    },
    {
      type: 'divider' as const,
    },
    {
      key: 'logout',
      icon: <LogoutOutlined />,
      label: '退出登录',
      onClick: handleLogout,
    },
  ]

  return (
    <AntHeader 
      style={{ 
        background: '#fff', 
        padding: '0 24px',
        borderBottom: '1px solid #f0f0f0',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
      }}
    >
      <div 
        style={{ 
          fontSize: '20px', 
          fontWeight: 'bold', 
          color: '#1677ff',
          cursor: 'pointer'
        }}
        onClick={() => navigate('/')}
      >
        🧳 Travel AI
      </div>
      
      {isAuthenticated && user ? (
        <Dropdown menu={{ items: userMenuItems }} placement="bottomRight">
          <Space style={{ cursor: 'pointer' }}>
            <Avatar size={32} icon={<UserOutlined />} />
            <span>{user.username}</span>
          </Space>
        </Dropdown>
      ) : (
        <Button type="primary" onClick={() => navigate('/login')}>
          登录
        </Button>
      )}
    </AntHeader>
  )
}

export default Header
