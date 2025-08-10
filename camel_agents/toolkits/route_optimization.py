"""
路线优化工具包
"""
from typing import Dict, List, Any, Optional, Tuple
import asyncio
import math
from datetime import datetime, timedelta


class RouteOptimizationToolkit:
    """路线优化工具包"""
    
    def __init__(self):
        """初始化路线优化工具包"""
        self.city_coordinates = {
            # 中国主要城市
            "北京": (39.9042, 116.4074),
            "上海": (31.2304, 121.4737),
            "广州": (23.1291, 113.2644),
            "深圳": (22.5431, 114.0579),
            "成都": (30.5728, 104.0668),
            "西安": (34.3416, 108.9398),
            "杭州": (30.2741, 120.1551),
            
            # 国际城市
            "东京": (35.6762, 139.6503),
            "大阪": (34.6937, 135.5023),
            "首尔": (37.5665, 126.9780),
            "曼谷": (13.7563, 100.5018),
            "巴黎": (48.8566, 2.3522),
            "伦敦": (51.5074, -0.1278),
            "纽约": (40.7128, -74.0060),
            "洛杉矶": (34.0522, -118.2437),
            "悉尼": (-33.8688, 151.2093)
        }
        
        self.transportation_data = {
            "domestic": {  # 国内交通
                "flight": {
                    "speed": 800,  # km/h
                    "cost_per_km": 0.8,  # 元/km
                    "comfort": 4,
                    "min_time": 2,  # 最少2小时（含候机时间）
                    "pros": ["速度快", "长距离优选", "舒适度高"],
                    "cons": ["价格较高", "受天气影响", "候机时间长"]
                },
                "high_speed_rail": {
                    "speed": 300,  # km/h
                    "cost_per_km": 0.5,
                    "comfort": 5,
                    "min_time": 1,
                    "pros": ["准时可靠", "市中心到市中心", "环保舒适"],
                    "cons": ["线路限制", "需要提前订票"]
                },
                "car": {
                    "speed": 80,  # km/h (考虑休息和路况)
                    "cost_per_km": 0.3,
                    "comfort": 3,
                    "min_time": 0.5,
                    "pros": ["灵活自由", "风景沿途", "成本较低"],
                    "cons": ["耗时较长", "驾驶疲劳", "停车困难"]
                },
                "bus": {
                    "speed": 60,  # km/h
                    "cost_per_km": 0.15,
                    "comfort": 2,
                    "min_time": 1,
                    "pros": ["价格便宜", "班次较多", "覆盖面广"],
                    "cons": ["耗时很长", "舒适度低", "受路况影响"]
                }
            },
            "international": {  # 国际交通
                "flight": {
                    "speed": 850,  # km/h
                    "cost_per_km": 1.2,
                    "comfort": 4,
                    "min_time": 4,  # 最少4小时（含国际航班候机时间）
                    "pros": ["唯一选择", "速度最快", "服务较好"],
                    "cons": ["价格昂贵", "时差影响", "安检严格"]
                }
            }
        }
    
    async def calculate_distance(self, city1: str, city2: str) -> float:
        """计算两城市间距离（公里）"""
        if city1 not in self.city_coordinates or city2 not in self.city_coordinates:
            return 1000  # 默认距离
        
        lat1, lon1 = self.city_coordinates[city1]
        lat2, lon2 = self.city_coordinates[city2]
        
        # 使用球面距离公式
        R = 6371  # 地球半径（公里）
        
        lat1_rad = math.radians(lat1)
        lat2_rad = math.radians(lat2)
        delta_lat = math.radians(lat2 - lat1)
        delta_lon = math.radians(lon2 - lon1)
        
        a = (math.sin(delta_lat / 2) ** 2 + 
             math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return R * c
    
    async def get_route_options(self, origin: str, destination: str, 
                              preferences: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """获取路线选项"""
        if preferences is None:
            preferences = {}
        
        distance = await self.calculate_distance(origin, destination)
        is_international = self._is_international_route(origin, destination)
        
        transport_data = (self.transportation_data["international"] if is_international 
                         else self.transportation_data["domestic"])
        
        options = []
        
        for transport_type, data in transport_data.items():
            # 跳过不适用的交通方式
            if is_international and transport_type != "flight":
                continue
            
            if not is_international and distance < 100 and transport_type == "flight":
                continue  # 短距离不推荐飞机
            
            travel_time = max(distance / data["speed"], data["min_time"])
            cost = distance * data["cost_per_km"]
            
            # 根据偏好调整
            optimization_target = preferences.get("optimization_target", "balanced")
            if optimization_target == "cost" and transport_type in ["bus", "car"]:
                cost *= 0.8  # 成本优化折扣
            elif optimization_target == "time" and transport_type == "flight":
                travel_time *= 0.9  # 时间优化
            
            option = {
                "transport_type": self._get_transport_name(transport_type),
                "duration": self._format_duration(travel_time),
                "duration_hours": travel_time,
                "cost": f"{int(cost)}-{int(cost * 1.5)}元",
                "cost_value": cost,
                "comfort": data["comfort"],
                "distance": f"{int(distance)}公里",
                "pros": data["pros"],
                "cons": data["cons"],
                "departure_times": self._get_departure_times(transport_type),
                "booking_tips": self._get_booking_tips(transport_type),
                "score": self._calculate_score(travel_time, cost, data["comfort"], preferences)
            }
            
            options.append(option)
        
        # 按评分排序
        options.sort(key=lambda x: x["score"], reverse=True)
        
        return options
    
    async def optimize_multi_city_route(self, cities: List[str], 
                                      preferences: Dict[str, Any] = None) -> Dict[str, Any]:
        """优化多城市路线"""
        if len(cities) < 2:
            return {"error": "至少需要2个城市"}
        
        if preferences is None:
            preferences = {}
        
        optimization_target = preferences.get("optimization_target", "balanced")
        
        # 计算所有城市间的距离矩阵
        distance_matrix = {}
        cost_matrix = {}
        time_matrix = {}
        
        for i, city1 in enumerate(cities):
            distance_matrix[city1] = {}
            cost_matrix[city1] = {}
            time_matrix[city1] = {}
            
            for j, city2 in enumerate(cities):
                if i == j:
                    distance_matrix[city1][city2] = 0
                    cost_matrix[city1][city2] = 0
                    time_matrix[city1][city2] = 0
                else:
                    distance = await self.calculate_distance(city1, city2)
                    # 假设使用最快的交通方式
                    transport_data = self.transportation_data["domestic"]["high_speed_rail"]
                    
                    distance_matrix[city1][city2] = distance
                    cost_matrix[city1][city2] = distance * transport_data["cost_per_km"]
                    time_matrix[city1][city2] = max(distance / transport_data["speed"], 
                                                  transport_data["min_time"])
        
        # 使用简化的贪心算法找最优路线
        if optimization_target == "cost":
            optimal_route = await self._find_optimal_route(cities, cost_matrix)
        elif optimization_target == "time":
            optimal_route = await self._find_optimal_route(cities, time_matrix)
        else:
            # 平衡优化：时间和成本的加权组合
            balanced_matrix = {}
            for city1 in cities:
                balanced_matrix[city1] = {}
                for city2 in cities:
                    if city1 == city2:
                        balanced_matrix[city1][city2] = 0
                    else:
                        # 标准化时间和成本，然后加权
                        normalized_time = time_matrix[city1][city2] / 10  # 假设最大10小时
                        normalized_cost = cost_matrix[city1][city2] / 2000  # 假设最大2000元
                        balanced_matrix[city1][city2] = normalized_time * 0.6 + normalized_cost * 0.4
            
            optimal_route = await self._find_optimal_route(cities, balanced_matrix)
        
        # 计算总成本和时间
        total_distance = sum(distance_matrix[optimal_route[i]][optimal_route[i+1]] 
                           for i in range(len(optimal_route)-1))
        total_cost = sum(cost_matrix[optimal_route[i]][optimal_route[i+1]] 
                        for i in range(len(optimal_route)-1))
        total_time = sum(time_matrix[optimal_route[i]][optimal_route[i+1]] 
                        for i in range(len(optimal_route)-1))
        
        # 生成详细的路线规划
        route_details = []
        for i in range(len(optimal_route)-1):
            from_city = optimal_route[i]
            to_city = optimal_route[i+1]
            
            route_options = await self.get_route_options(from_city, to_city, preferences)
            recommended_option = route_options[0] if route_options else None
            
            route_details.append({
                "segment": i + 1,
                "from": from_city,
                "to": to_city,
                "distance": f"{int(distance_matrix[from_city][to_city])}公里",
                "recommended_transport": recommended_option,
                "all_options": route_options
            })
        
        return {
            "optimal_route": optimal_route,
            "total_distance": f"{int(total_distance)}公里",
            "total_cost": f"{int(total_cost)}元",
            "total_duration": self._format_duration(total_time),
            "optimization_target": optimization_target,
            "route_details": route_details,
            "travel_tips": self._get_multi_city_tips(optimal_route)
        }
    
    async def _find_optimal_route(self, cities: List[str], cost_matrix: Dict) -> List[str]:
        """使用贪心算法找最优路线"""
        if len(cities) <= 2:
            return cities
        
        # 从第一个城市开始
        current_city = cities[0]
        route = [current_city]
        remaining_cities = cities[1:]
        
        while remaining_cities:
            # 找到距离当前城市最近的城市
            next_city = min(remaining_cities, 
                          key=lambda city: cost_matrix[current_city][city])
            route.append(next_city)
            remaining_cities.remove(next_city)
            current_city = next_city
        
        return route
    
    def _is_international_route(self, origin: str, destination: str) -> bool:
        """判断是否为国际路线"""
        domestic_cities = ["北京", "上海", "广州", "深圳", "成都", "西安", "杭州", "南京", "武汉", "重庆"]
        
        origin_domestic = origin in domestic_cities
        dest_domestic = destination in domestic_cities
        
        return not (origin_domestic and dest_domestic)
    
    def _get_transport_name(self, transport_type: str) -> str:
        """获取交通方式中文名称"""
        names = {
            "flight": "飞机",
            "high_speed_rail": "高铁",
            "car": "汽车",
            "bus": "大巴"
        }
        return names.get(transport_type, transport_type)
    
    def _format_duration(self, hours: float) -> str:
        """格式化时长"""
        if hours < 1:
            return f"{int(hours * 60)}分钟"
        else:
            h = int(hours)
            m = int((hours - h) * 60)
            if m == 0:
                return f"{h}小时"
            else:
                return f"{h}小时{m}分钟"
    
    def _get_departure_times(self, transport_type: str) -> List[str]:
        """获取出发时间选项"""
        if transport_type == "flight":
            return ["06:00", "08:30", "10:00", "14:00", "16:30", "19:00", "21:30"]
        elif transport_type == "high_speed_rail":
            return ["07:00", "09:00", "11:00", "13:00", "15:00", "17:00", "19:00"]
        elif transport_type == "car":
            return ["任意时间"]
        else:
            return ["08:00", "10:00", "14:00", "16:00", "18:00"]
    
    def _get_booking_tips(self, transport_type: str) -> str:
        """获取预订建议"""
        tips = {
            "flight": "建议提前1-2周预订，关注航空公司促销",
            "high_speed_rail": "热门线路建议提前7-15天订票",
            "car": "提前预订租车，注意驾驶证和保险",
            "bus": "可当天购票，建议网上预订座位"
        }
        return tips.get(transport_type, "建议提前预订")
    
    def _calculate_score(self, time: float, cost: float, comfort: int, 
                        preferences: Dict[str, Any]) -> float:
        """计算选项评分"""
        optimization = preferences.get("optimization_target", "balanced")
        
        # 标准化指标 (假设最大值)
        time_score = max(0, 1 - time / 12)  # 12小时为最大
        cost_score = max(0, 1 - cost / 3000)  # 3000元为最大
        comfort_score = comfort / 5  # 5为最高舒适度
        
        if optimization == "time":
            return time_score * 0.7 + cost_score * 0.2 + comfort_score * 0.1
        elif optimization == "cost":
            return cost_score * 0.7 + time_score * 0.2 + comfort_score * 0.1
        else:  # balanced
            return time_score * 0.4 + cost_score * 0.4 + comfort_score * 0.2
    
    def _get_multi_city_tips(self, route: List[str]) -> List[str]:
        """获取多城市旅行建议"""
        tips = [
            f"推荐路线：{' → '.join(route)}",
            "建议每个城市停留2-3天，深度体验当地文化",
            "提前预订交通和住宿，特别是旺季期间",
            "随身携带身份证件，部分交通工具需要实名制"
        ]
        
        if len(route) > 3:
            tips.append("行程较长，注意合理安排休息时间")
        
        return tips
