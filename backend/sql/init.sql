-- Travel AI 数据库初始化脚本
-- 创建时间: 2025-08-10

-- 创建扩展
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 用户表
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    preferences JSONB DEFAULT '{}',
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 对话会话表
CREATE TABLE IF NOT EXISTS conversations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(200),
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 消息表
CREATE TABLE IF NOT EXISTS messages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    conversation_id UUID REFERENCES conversations(id) ON DELETE CASCADE,
    role VARCHAR(20) NOT NULL, -- 'user' or 'assistant'
    content TEXT NOT NULL,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 旅行计划表
CREATE TABLE IF NOT EXISTS travel_plans (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    conversation_id UUID REFERENCES conversations(id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    destination TEXT,
    start_date DATE,
    end_date DATE,
    budget_min DECIMAL(10,2),
    budget_max DECIMAL(10,2),
    plan_data JSONB NOT NULL,
    status VARCHAR(20) DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 目的地数据表 (预置数据)
CREATE TABLE IF NOT EXISTS destinations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    region VARCHAR(50),
    description TEXT,
    attractions JSONB DEFAULT '[]',
    avg_daily_budget DECIMAL(8,2),
    best_season VARCHAR(50),
    tags TEXT[],
    coordinates POINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建索引
CREATE INDEX IF NOT EXISTS idx_conversations_user_id ON conversations(user_id);
CREATE INDEX IF NOT EXISTS idx_messages_conversation_id ON messages(conversation_id);
CREATE INDEX IF NOT EXISTS idx_travel_plans_user_id ON travel_plans(user_id);
CREATE INDEX IF NOT EXISTS idx_destinations_country ON destinations(country);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);

-- 创建更新时间触发器函数
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- 为需要的表创建更新时间触发器
CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_conversations_updated_at BEFORE UPDATE ON conversations
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_travel_plans_updated_at BEFORE UPDATE ON travel_plans
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- 插入示例目的地数据
INSERT INTO destinations (name, country, region, description, attractions, avg_daily_budget, best_season, tags) VALUES
('东京', '日本', '关东地区', '日本的首都，现代化大都市', '["浅草寺", "银座", "新宿", "涩谷", "东京塔"]', 800.00, '春季,秋季', ARRAY['城市', '文化', '购物', '美食']),
('大阪', '日本', '关西地区', '日本的厨房，美食之都', '["大阪城", "道顿堀", "环球影城", "心斋桥"]', 600.00, '春季,秋季', ARRAY['城市', '美食', '娱乐']),
('巴黎', '法国', '法兰西岛', '浪漫之都，艺术之城', '["埃菲尔铁塔", "卢浮宫", "凯旋门", "香榭丽舍大街"]', 1000.00, '春季,秋季', ARRAY['城市', '文化', '艺术', '浪漫']),
('曼谷', '泰国', '中部地区', '微笑之国的首都', '["大皇宫", "卧佛寺", "湄南河", "考山路"]', 300.00, '凉季', ARRAY['城市', '文化', '美食', '便宜']);

-- 创建演示用户 (密码: demo123)
INSERT INTO users (username, email, password_hash, preferences) VALUES
('demo', 'demo@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/lewdBDYVdJZJc8Lx6', 
 '{"preferred_languages": ["zh-CN", "en-US"], "travel_style": "文化探索", "budget_range": "中等"}')
ON CONFLICT (username) DO NOTHING;

-- 完成初始化
SELECT 'Travel AI 数据库初始化完成!' AS message;
