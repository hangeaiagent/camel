import React, { useEffect, useState } from 'react'
import { Card, Descriptions, Button, Tag, List, message } from 'antd'
import { EditOutlined, HistoryOutlined } from '@ant-design/icons'
import { useQuery } from '@tanstack/react-query'
import { userAPI } from '@/services/api'
import type { User, TravelPlan } from '@/types'

const ProfilePage: React.FC = () => {
  const [user, setUser] = useState<User | null>(null)
  const [travelPlans, setTravelPlans] = useState<TravelPlan[]>([])

  // 获取用户信息
  const { data: profileData, isLoading: profileLoading } = useQuery({
    queryKey: ['userProfile'],
    queryFn: userAPI.getProfile,
    onSuccess: (data) => setUser(data),
    onError: (error: any) => {
      message.error('获取用户信息失败')
    }
  })

  // 获取旅行计划
  const { data: plansData, isLoading: plansLoading } = useQuery({
    queryKey: ['travelPlans'],
    queryFn: userAPI.getTravelPlans,
    onSuccess: (data) => setTravelPlans(data.travel_plans || []),
    onError: (error: any) => {
      message.error('获取旅行计划失败')
    }
  })

  if (profileLoading) {
    return <div style={{ padding: '20px', textAlign: 'center' }}>加载中...</div>
  }

  return (
    <div style={{ 
      padding: '20px', 
      maxWidth: '1200px', 
      margin: '0 auto',
      background: '#f5f5f5',
      minHeight: 'calc(100vh - 64px)'
    }}>
      {/* 用户基本信息 */}
      <Card 
        title="个人信息" 
        extra={
          <Button icon={<EditOutlined />} type="text">
            编辑
          </Button>
        }
        style={{ marginBottom: '20px' }}
      >
        <Descriptions column={2}>
          <Descriptions.Item label="用户名">
            {user?.username}
          </Descriptions.Item>
          <Descriptions.Item label="邮箱">
            {user?.email}
          </Descriptions.Item>
          <Descriptions.Item label="注册时间">
            {user?.created_at ? new Date(user.created_at).toLocaleDateString('zh-CN') : '-'}
          </Descriptions.Item>
          <Descriptions.Item label="账户状态">
            <Tag color="green">正常</Tag>
          </Descriptions.Item>
        </Descriptions>
      </Card>

      {/* 用户偏好 */}
      <Card 
        title="旅行偏好" 
        extra={
          <Button icon={<EditOutlined />} type="text">
            编辑偏好
          </Button>
        }
        style={{ marginBottom: '20px' }}
      >
        <Descriptions column={2}>
          <Descriptions.Item label="偏好语言">
            {user?.preferences?.preferred_languages?.map(lang => (
              <Tag key={lang} color="blue">
                {lang === 'zh-CN' ? '中文' : lang === 'en-US' ? '英文' : lang}
              </Tag>
            ))}
          </Descriptions.Item>
          <Descriptions.Item label="旅行风格">
            <Tag color="purple">{user?.preferences?.travel_style || '未设置'}</Tag>
          </Descriptions.Item>
          <Descriptions.Item label="预算偏好">
            <Tag color="orange">{user?.preferences?.budget_range || '未设置'}</Tag>
          </Descriptions.Item>
          <Descriptions.Item label="喜爱目的地">
            {user?.preferences?.favorite_destinations?.map(dest => (
              <Tag key={dest} color="green">{dest}</Tag>
            ))}
          </Descriptions.Item>
        </Descriptions>
      </Card>

      {/* 旅行计划历史 */}
      <Card 
        title={
          <span>
            <HistoryOutlined style={{ marginRight: '8px' }} />
            旅行计划历史
          </span>
        }
        loading={plansLoading}
      >
        <List
          dataSource={travelPlans}
          locale={{ emptyText: '暂无旅行计划' }}
          renderItem={(plan) => (
            <List.Item
              actions={[
                <Button type="text" key="view">查看</Button>,
                <Button type="text" key="edit">编辑</Button>
              ]}
            >
              <List.Item.Meta
                title={
                  <span>
                    {plan.title}
                    <Tag 
                      color={plan.status === '已完成' ? 'green' : 'blue'} 
                      style={{ marginLeft: '8px' }}
                    >
                      {plan.status}
                    </Tag>
                  </span>
                }
                description={
                  <div>
                    <div>{plan.summary}</div>
                    <div style={{ marginTop: '4px', fontSize: '12px', color: '#999' }}>
                      目的地: {plan.destination} | 时长: {plan.duration} | 预算: {plan.budget}
                    </div>
                    <div style={{ marginTop: '4px', fontSize: '12px', color: '#999' }}>
                      创建时间: {new Date(plan.created_at).toLocaleDateString('zh-CN')}
                    </div>
                  </div>
                }
              />
            </List.Item>
          )}
        />
      </Card>
    </div>
  )
}

export default ProfilePage
