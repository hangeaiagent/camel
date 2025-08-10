"""
旅行规划工具包
"""
from typing import Dict, List, Any, Optional
import asyncio
import random
from datetime import datetime, timedelta


class TravelPlanningToolkit:
    """旅行规划工具包"""
    
    def __init__(self):
        """初始化规划工具包"""
        self.destination_data = {
            "日本": {
                "cities": ["东京", "大阪", "京都", "名古屋", "福冈"],
                "attractions": {
                    "东京": ["浅草寺", "银座", "新宿", "涩谷", "东京塔", "迪士尼乐园"],
                    "大阪": ["大阪城", "道顿堀", "环球影城", "奈良公园", "心斋桥"],
                    "京都": ["清水寺", "金阁寺", "伏见稻荷大社", "岚山", "二条城"]
                },
                "best_season": ["春季(3-5月)", "秋季(9-11月)"],
                "avg_budget": {"budget": 8000, "luxury": 15000, "economy": 4000},
                "culture_tips": ["脱鞋进屋", "不要大声说话", "准时很重要"],
                "food": ["寿司", "拉面", "天妇罗", "和牛", "抹茶"]
            },
            "泰国": {
                "cities": ["曼谷", "清迈", "普吉岛", "芭提雅", "苏梅岛"],
                "attractions": {
                    "曼谷": ["大皇宫", "卧佛寺", "湄南河", "考山路", "暹罗广场"],
                    "清迈": ["素贴山", "古城", "周末市场", "大象营", "丛林飞跃"],
                    "普吉岛": ["芭东海滩", "皮皮岛", "卡伦海滩", "幻多奇乐园"]
                },
                "best_season": ["凉季(11-2月)", "热季(3-6月)"],
                "avg_budget": {"budget": 5000, "luxury": 10000, "economy": 2500},
                "culture_tips": ["尊重佛教文化", "不要摸头", "进寺庙要穿长裤"],
                "food": ["冬阴功汤", "青木瓜沙拉", "芒果糯米饭", "泰式炒面"]
            },
            "法国": {
                "cities": ["巴黎", "尼斯", "里昂", "马赛", "波尔多"],
                "attractions": {
                    "巴黎": ["埃菲尔铁塔", "卢浮宫", "凯旋门", "巴黎圣母院", "香榭丽舍大街"],
                    "尼斯": ["蔚蓝海岸", "老城区", "城堡山", "马塞纳广场"],
                    "里昂": ["里昂老城", "白莱果广场", "富维耶圣母院"]
                },
                "best_season": ["春季(4-6月)", "秋季(9-10月)"],
                "avg_budget": {"budget": 12000, "luxury": 25000, "economy": 6000},
                "culture_tips": ["学几句法语", "用餐礼仪", "小费文化"],
                "food": ["法式面包", "奶酪", "红酒", "鹅肝", "马卡龙"]
            }
        }
        
        self.activity_types = {
            "文化探索": ["博物馆", "历史遗迹", "传统文化体验", "艺术展览"],
            "自然风光": ["国家公园", "海滩", "山景", "湖泊", "森林"],
            "美食体验": ["当地餐厅", "街头小吃", "烹饪课程", "酒庄参观"],
            "购物娱乐": ["购物中心", "当地市场", "娱乐场所", "夜生活"],
            "冒险运动": ["徒步", "潜水", "滑雪", "攀岩", "极限运动"],
            "休闲度假": ["spa", "海滩度假", "温泉", "度假村", "休闲漫步"]
        }
    
    async def generate_itinerary(self, requirements: Dict[str, Any]) -> Dict[str, Any]:
        """生成旅行行程"""
        destination = requirements.get("destination", "日本")
        duration = self._parse_duration(requirements.get("duration", "5天"))
        budget_range = requirements.get("budget_range", "budget")
        travel_style = requirements.get("travel_style", "文化探索")
        travelers = requirements.get("travelers", 2)
        
        dest_data = self.destination_data.get(destination, self.destination_data["日本"])
        
        # 生成日程安排
        daily_plans = []
        cities = dest_data["cities"][:min(duration, len(dest_data["cities"]))]
        
        for day in range(1, duration + 1):
            city_index = min(day - 1, len(cities) - 1)
            city = cities[city_index]
            
            # 为每一天安排活动
            attractions = dest_data["attractions"].get(city, ["当地景点"])
            activities = self._select_activities(attractions, travel_style, day)
            
            daily_plans.append({
                "day": day,
                "location": city,
                "activities": activities,
                "meals": self._suggest_meals(dest_data["food"], day),
                "accommodation": f"{city}推荐酒店",
                "tips": f"第{day}天建议早起，避开人群高峰"
            })
        
        # 预算估算
        base_budget = dest_data["avg_budget"].get(budget_range, 8000)
        budget_breakdown = self._calculate_budget(base_budget, duration, travelers)
        
        return {
            "title": f"{destination}{duration}日精彩之旅",
            "destination": destination,
            "duration": f"{duration}天",
            "budget_range": budget_range,
            "daily_plans": daily_plans,
            "budget_breakdown": budget_breakdown,
            "best_travel_time": dest_data["best_season"],
            "culture_tips": dest_data["culture_tips"],
            "recommended_items": self._get_packing_list(destination, duration),
            "emergency_info": self._get_emergency_info(destination)
        }
    
    async def suggest_destinations(self, preferences: Dict[str, Any]) -> List[Dict[str, Any]]:
        """推荐目的地"""
        budget = preferences.get("budget", 10000)
        style = preferences.get("style", "文化探索")
        season = preferences.get("season", "春季")
        
        suggestions = []
        
        for dest, data in self.destination_data.items():
            score = 0
            
            # 预算匹配
            if budget >= data["avg_budget"]["economy"]:
                score += 3
            if budget >= data["avg_budget"]["budget"]:
                score += 2
            if budget >= data["avg_budget"]["luxury"]:
                score += 1
            
            # 季节匹配
            if any(season in s for s in data["best_season"]):
                score += 2
            
            # 活动类型匹配
            if style in self.activity_types:
                score += 1
            
            suggestions.append({
                "destination": dest,
                "score": score,
                "budget_fit": self._get_budget_fit(budget, data["avg_budget"]),
                "highlights": list(data["attractions"].values())[0][:3],
                "best_time": data["best_season"][0]
            })
        
        # 按评分排序
        suggestions.sort(key=lambda x: x["score"], reverse=True)
        return suggestions[:5]
    
    async def optimize_budget(self, plan: Dict[str, Any], target_budget: float) -> Dict[str, Any]:
        """优化预算"""
        current_budget = plan["budget_breakdown"]["total"]
        
        if current_budget <= target_budget:
            return plan
        
        # 需要削减预算
        reduction_needed = current_budget - target_budget
        reduction_strategies = []
        
        # 住宿优化
        accommodation_savings = current_budget * 0.3 * 0.3  # 住宿占30%，可节省30%
        if reduction_needed > 0:
            reduction_strategies.append({
                "category": "住宿",
                "savings": min(accommodation_savings, reduction_needed),
                "suggestion": "选择经济型酒店或民宿"
            })
            reduction_needed -= accommodation_savings
        
        # 餐饮优化
        if reduction_needed > 0:
            food_savings = current_budget * 0.25 * 0.4  # 餐饮占25%，可节省40%
            reduction_strategies.append({
                "category": "餐饮",
                "savings": min(food_savings, reduction_needed),
                "suggestion": "多尝试当地小吃，减少高档餐厅"
            })
            reduction_needed -= food_savings
        
        # 活动优化
        if reduction_needed > 0:
            activity_savings = current_budget * 0.2 * 0.5  # 活动占20%，可节省50%
            reduction_strategies.append({
                "category": "活动",
                "savings": min(activity_savings, reduction_needed),
                "suggestion": "选择免费或低价景点，如公园、海滩"
            })
        
        optimized_budget = current_budget - sum(s["savings"] for s in reduction_strategies)
        
        return {
            **plan,
            "budget_breakdown": {
                **plan["budget_breakdown"],
                "total": optimized_budget,
                "optimized": True
            },
            "optimization_strategies": reduction_strategies
        }
    
    def _parse_duration(self, duration_str: str) -> int:
        """解析持续时间"""
        if isinstance(duration_str, int):
            return duration_str
        
        # 提取数字
        import re
        numbers = re.findall(r'\d+', str(duration_str))
        if numbers:
            return int(numbers[0])
        return 5  # 默认5天
    
    def _select_activities(self, attractions: List[str], style: str, day: int) -> List[str]:
        """选择活动"""
        # 根据旅行风格和天数选择活动
        available_activities = self.activity_types.get(style, attractions)
        
        if day == 1:
            # 第一天：轻松适应
            return ["抵达酒店", "附近漫步", attractions[0] if attractions else "当地景点"]
        elif day <= 3:
            # 前几天：主要景点
            selected = random.sample(attractions, min(3, len(attractions)))
            return selected
        else:
            # 后几天：深度体验
            return [attractions[0] if attractions else "当地体验", "自由活动", "纪念品购物"]
    
    def _suggest_meals(self, local_food: List[str], day: int) -> List[str]:
        """推荐餐饮"""
        if day == 1:
            return ["酒店早餐", "当地简餐", "欢迎晚宴"]
        else:
            breakfast = "当地早餐" if day > 2 else "酒店早餐"
            lunch = random.choice(local_food) if local_food else "当地午餐"
            dinner = random.choice(local_food) if local_food else "特色晚餐"
            return [breakfast, lunch, dinner]
    
    def _calculate_budget(self, base_budget: int, duration: int, travelers: int) -> Dict[str, Any]:
        """计算预算分解"""
        total_budget = base_budget * duration * travelers / 5  # 基于5天的基准
        
        return {
            "total": int(total_budget),
            "transportation": int(total_budget * 0.3),
            "accommodation": int(total_budget * 0.35),
            "food": int(total_budget * 0.25),
            "activities": int(total_budget * 0.10),
            "breakdown_percentage": {
                "transportation": "30%",
                "accommodation": "35%",
                "food": "25%",
                "activities": "10%"
            }
        }
    
    def _get_budget_fit(self, budget: float, dest_budgets: Dict[str, int]) -> str:
        """获取预算匹配度"""
        if budget >= dest_budgets["luxury"]:
            return "豪华游"
        elif budget >= dest_budgets["budget"]:
            return "标准游"
        elif budget >= dest_budgets["economy"]:
            return "经济游"
        else:
            return "预算不足"
    
    def _get_packing_list(self, destination: str, duration: int) -> List[str]:
        """获取打包清单"""
        basic_items = ["护照", "身份证", "手机充电器", "换洗衣物", "洗漱用品"]
        
        if destination in ["日本", "韩国"]:
            basic_items.extend(["转换插头", "口罩", "现金"])
        elif destination in ["泰国", "马来西亚"]:
            basic_items.extend(["防晒霜", "驱蚊液", "夏季衣物"])
        elif destination in ["法国", "德国"]:
            basic_items.extend(["保暖衣物", "雨具", "欧式插头转换器"])
        
        if duration > 7:
            basic_items.extend(["备用药品", "额外行李箱"])
            
        return basic_items
    
    def _get_emergency_info(self, destination: str) -> Dict[str, str]:
        """获取紧急信息"""
        emergency_info = {
            "日本": {
                "emergency_number": "110 (警察), 119 (消防/急救)",
                "embassy": "中国驻日本大使馆: +81-3-3403-3388",
                "hospital": "国际医疗中心",
                "tips": "日本医疗费用较高，建议购买旅行保险"
            },
            "泰国": {
                "emergency_number": "191 (警察), 1669 (急救)",
                "embassy": "中国驻泰国大使馆: +66-2-245-7044",
                "hospital": "曼谷医院",
                "tips": "注意食物卫生，防范登革热"
            },
            "法国": {
                "emergency_number": "112 (通用急救)",
                "embassy": "中国驻法国大使馆: +33-1-4439-0000",
                "hospital": "巴黎公立医院",
                "tips": "注意个人财物安全，小心扒手"
            }
        }
        
        return emergency_info.get(destination, {
            "emergency_number": "当地急救电话",
            "embassy": "中国大使馆",
            "hospital": "当地医院",
            "tips": "注意安全，保持通讯畅通"
        })
