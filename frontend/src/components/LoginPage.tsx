import React, { useState } from 'react'
import { Form, Input, Button, Card, message, Tabs, Space } from 'antd'
import { UserOutlined, LockOutlined, MailOutlined } from '@ant-design/icons'
import { useNavigate } from 'react-router-dom'
import { useAppStore } from '@/store/store'
import { authAPI } from '@/services/api'
import type { LoginCredentials, RegisterData } from '@/types'

const LoginPage: React.FC = () => {
  const navigate = useNavigate()
  const { setUser } = useAppStore()
  const [loading, setLoading] = useState(false)

  const handleLogin = async (values: LoginCredentials) => {
    setLoading(true)
    try {
      const tokenData = await authAPI.login(values)
      localStorage.setItem('access_token', tokenData.access_token)
      
      // 获取用户信息
      const userData = await authAPI.getCurrentUser()
      setUser(userData)
      
      message.success('登录成功！')
      navigate('/')
    } catch (error: any) {
      message.error(error.response?.data?.detail || '登录失败，请检查用户名和密码')
    } finally {
      setLoading(false)
    }
  }

  const handleRegister = async (values: RegisterData) => {
    if (values.password !== values.confirm_password) {
      message.error('两次输入的密码不一致')
      return
    }

    setLoading(true)
    try {
      await authAPI.register(values)
      message.success('注册成功！请登录')
      // 可以自动切换到登录标签页
    } catch (error: any) {
      message.error(error.response?.data?.detail || '注册失败')
    } finally {
      setLoading(false)
    }
  }

  const LoginForm = () => (
    <Form
      name="login"
      onFinish={handleLogin}
      autoComplete="off"
      layout="vertical"
    >
      <Form.Item
        label="用户名"
        name="username"
        rules={[{ required: true, message: '请输入用户名' }]}
      >
        <Input 
          prefix={<UserOutlined />} 
          placeholder="用户名" 
          size="large"
        />
      </Form.Item>

      <Form.Item
        label="密码"
        name="password"
        rules={[{ required: true, message: '请输入密码' }]}
      >
        <Input.Password 
          prefix={<LockOutlined />} 
          placeholder="密码" 
          size="large"
        />
      </Form.Item>

      <Form.Item>
        <Button 
          type="primary" 
          htmlType="submit" 
          loading={loading}
          size="large"
          block
        >
          登录
        </Button>
      </Form.Item>
    </Form>
  )

  const RegisterForm = () => (
    <Form
      name="register"
      onFinish={handleRegister}
      autoComplete="off"
      layout="vertical"
    >
      <Form.Item
        label="用户名"
        name="username"
        rules={[
          { required: true, message: '请输入用户名' },
          { min: 3, message: '用户名至少3个字符' }
        ]}
      >
        <Input 
          prefix={<UserOutlined />} 
          placeholder="用户名" 
          size="large"
        />
      </Form.Item>

      <Form.Item
        label="邮箱"
        name="email"
        rules={[
          { required: true, message: '请输入邮箱' },
          { type: 'email', message: '请输入有效的邮箱地址' }
        ]}
      >
        <Input 
          prefix={<MailOutlined />} 
          placeholder="邮箱" 
          size="large"
        />
      </Form.Item>

      <Form.Item
        label="密码"
        name="password"
        rules={[
          { required: true, message: '请输入密码' },
          { min: 6, message: '密码至少6个字符' }
        ]}
      >
        <Input.Password 
          prefix={<LockOutlined />} 
          placeholder="密码" 
          size="large"
        />
      </Form.Item>

      <Form.Item
        label="确认密码"
        name="confirm_password"
        rules={[{ required: true, message: '请确认密码' }]}
      >
        <Input.Password 
          prefix={<LockOutlined />} 
          placeholder="确认密码" 
          size="large"
        />
      </Form.Item>

      <Form.Item>
        <Button 
          type="primary" 
          htmlType="submit" 
          loading={loading}
          size="large"
          block
        >
          注册
        </Button>
      </Form.Item>
    </Form>
  )

  const items = [
    {
      key: 'login',
      label: '登录',
      children: <LoginForm />,
    },
    {
      key: 'register',
      label: '注册',
      children: <RegisterForm />,
    },
  ]

  return (
    <div className="login-container">
      <Card 
        style={{ width: 400, maxWidth: '90vw' }}
        title={
          <Space>
            <span style={{ fontSize: '24px' }}>🧳</span>
            <span>Travel AI</span>
          </Space>
        }
      >
        <Tabs defaultActiveKey="login" items={items} centered />
        
        <div style={{ marginTop: 16, textAlign: 'center', color: '#666' }}>
          <p>演示账号：demo / demo123</p>
        </div>
      </Card>
    </div>
  )
}

export default LoginPage
