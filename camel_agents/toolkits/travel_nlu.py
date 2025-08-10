"""
旅行自然语言理解工具包
"""
from typing import Dict, List, Any, Optional
import re
import asyncio
from datetime import datetime


class TravelNLUToolkit:
    """旅行自然语言理解工具包"""
    
    def __init__(self):
        """初始化NLU工具包"""
        self.intent_patterns = {
            "travel_planning": [
                r"想去.*旅游", r"计划.*旅行", r"安排.*行程", r"规划.*旅游",
                r"去.*玩", r"旅行.*天", r".*游.*天", r"plan.*trip"
            ],
            "route_planning": [
                r"怎么去", r"路线", r"交通", r"航班", r"火车", r"汽车",
                r"从.*到.*", r"route", r"transportation", r"flight"
            ],
            "attraction_query": [
                r"推荐.*景点", r"什么好玩", r"有什么.*的", r"必去.*地方",
                r"景点推荐", r"attractions", r"recommend", r"sightseeing"
            ],
            "hotel_booking": [
                r"酒店", r"住宿", r"预订.*房间", r"hotel", r"accommodation", r"booking"
            ],
            "budget_planning": [
                r"预算", r"费用", r"花费", r"价格", r"多少钱", r"budget", r"cost", r"price"
            ],
            "weather_inquiry": [
                r"天气", r"气候", r"温度", r"weather", r"climate", r"temperature"
            ],
            "food_recommendation": [
                r"美食", r"餐厅", r"小吃", r"特色菜", r"food", r"restaurant", r"cuisine"
            ]
        }
        
        self.entity_patterns = {
            "destination": {
                "国家": [
                    "中国", "日本", "韩国", "泰国", "新加坡", "马来西亚", "印度尼西亚",
                    "美国", "加拿大", "英国", "法国", "德国", "意大利", "西班牙",
                    "澳大利亚", "新西兰", "印度", "俄罗斯", "巴西", "阿根廷"
                ],
                "城市": [
                    "北京", "上海", "广州", "深圳", "成都", "西安", "杭州", "南京",
                    "东京", "大阪", "京都", "首尔", "釜山", "曼谷", "清迈", "普吉岛",
                    "纽约", "洛杉矶", "旧金山", "华盛顿", "芝加哥", "拉斯维加斯",
                    "伦敦", "巴黎", "罗马", "米兰", "巴塞罗那", "马德里", "柏林",
                    "悉尼", "墨尔本", "多伦多", "温哥华", "莫斯科", "圣彼得堡"
                ],
                "景点": [
                    "长城", "故宫", "天安门", "兵马俑", "九寨沟", "张家界",
                    "富士山", "清水寺", "金阁寺", "东京塔", "迪士尼乐园",
                    "埃菲尔铁塔", "卢浮宫", "凯旋门", "罗马斗兽场", "比萨斜塔",
                    "自由女神像", "时代广场", "金门大桥", "好莱坞标志"
                ]
            },
            "duration": [
                r"(\d+)天", r"(\d+)日", r"(\d+)周", r"(\d+)个月",
                r"(\d+)\s*days?", r"(\d+)\s*weeks?", r"(\d+)\s*months?"
            ],
            "budget": [
                r"(\d+)元", r"(\d+)块", r"(\d+)万", r"(\d+)千",
                r"\$(\d+)", r"(\d+)\s*dollars?", r"(\d+)\s*rmb", r"(\d+)\s*yuan"
            ],
            "date": [
                r"(\d{1,2})月(\d{1,2})日", r"(\d{4})年(\d{1,2})月", 
                r"(\d{1,2})/(\d{1,2})", r"明天", r"后天", r"下周", r"下个月"
            ],
            "travelers": [
                r"(\d+)人", r"(\d+)个人", r"一个人", r"两个人", r"一家人",
                r"夫妻", r"情侣", r"朋友", r"同事", r"家庭"
            ]
        }
    
    async def intent_recognition(self, user_input: str) -> Dict[str, Any]:
        """意图识别"""
        user_input_lower = user_input.lower()
        intent_scores = {}
        
        for intent, patterns in self.intent_patterns.items():
            score = 0
            for pattern in patterns:
                if re.search(pattern, user_input, re.IGNORECASE):
                    score += 1
            intent_scores[intent] = score
        
        # 找到得分最高的意图
        if intent_scores:
            primary_intent = max(intent_scores, key=intent_scores.get)
            confidence = intent_scores[primary_intent] / len(self.intent_patterns[primary_intent])
        else:
            primary_intent = "general_query"
            confidence = 0.5
        
        # 获取次要意图
        secondary_intents = [
            intent for intent, score in intent_scores.items() 
            if score > 0 and intent != primary_intent
        ]
        
        return {
            "primary_intent": primary_intent,
            "secondary_intents": secondary_intents[:3],  # 最多3个次要意图
            "confidence": min(confidence, 1.0),
            "intent_scores": intent_scores
        }
    
    async def entity_extraction(self, user_input: str) -> Dict[str, List[str]]:
        """实体提取"""
        entities = {}
        
        # 提取目的地实体
        destinations = []
        for category, locations in self.entity_patterns["destination"].items():
            for location in locations:
                if location in user_input:
                    destinations.append(location)
        
        if destinations:
            entities["destination"] = destinations
        
        # 提取时长实体
        duration_matches = []
        for pattern in self.entity_patterns["duration"]:
            matches = re.findall(pattern, user_input, re.IGNORECASE)
            duration_matches.extend(matches)
        
        if duration_matches:
            entities["duration"] = [match if isinstance(match, str) else str(match) for match in duration_matches]
        
        # 提取预算实体
        budget_matches = []
        for pattern in self.entity_patterns["budget"]:
            matches = re.findall(pattern, user_input, re.IGNORECASE)
            budget_matches.extend(matches)
        
        if budget_matches:
            entities["budget"] = [match if isinstance(match, str) else str(match) for match in budget_matches]
        
        # 提取日期实体
        date_matches = []
        for pattern in self.entity_patterns["date"]:
            matches = re.findall(pattern, user_input, re.IGNORECASE)
            date_matches.extend(matches)
        
        if date_matches:
            entities["date"] = [match if isinstance(match, str) else str(match) for match in date_matches]
        
        # 提取旅行者信息
        travelers_matches = []
        for pattern in self.entity_patterns["travelers"]:
            matches = re.findall(pattern, user_input, re.IGNORECASE)
            travelers_matches.extend(matches)
        
        if travelers_matches:
            entities["travelers"] = [match if isinstance(match, str) else str(match) for match in travelers_matches]
        
        return entities
    
    async def detect_language(self, text: str) -> str:
        """检测文本语言"""
        # 简单的语言检测逻辑
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
        english_chars = len(re.findall(r'[a-zA-Z]', text))
        japanese_chars = len(re.findall(r'[\u3040-\u309f\u30a0-\u30ff]', text))
        korean_chars = len(re.findall(r'[\uac00-\ud7af]', text))
        
        total_chars = len(text)
        
        if chinese_chars / total_chars > 0.3:
            return "zh-CN"
        elif japanese_chars / total_chars > 0.2:
            return "ja-JP"
        elif korean_chars / total_chars > 0.2:
            return "ko-KR"
        elif english_chars / total_chars > 0.5:
            return "en-US"
        else:
            return "zh-CN"  # 默认中文
    
    async def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """情感分析"""
        # 简单的情感分析
        positive_words = ["喜欢", "想要", "期待", "兴奋", "高兴", "棒", "好", "love", "want", "excited", "great", "amazing"]
        negative_words = ["不喜欢", "讨厌", "担心", "害怕", "不想", "糟糕", "hate", "worry", "afraid", "terrible", "bad"]
        
        positive_count = sum(1 for word in positive_words if word in text.lower())
        negative_count = sum(1 for word in negative_words if word in text.lower())
        
        if positive_count > negative_count:
            sentiment = "positive"
            score = 0.6 + (positive_count - negative_count) * 0.1
        elif negative_count > positive_count:
            sentiment = "negative"
            score = 0.4 - (negative_count - positive_count) * 0.1
        else:
            sentiment = "neutral"
            score = 0.5
        
        return {
            "sentiment": sentiment,
            "score": max(0.0, min(1.0, score)),
            "positive_indicators": positive_count,
            "negative_indicators": negative_count
        }
    
    async def process(self, user_input: str) -> Dict[str, Any]:
        """综合处理用户输入"""
        results = await asyncio.gather(
            self.intent_recognition(user_input),
            self.entity_extraction(user_input),
            self.detect_language(user_input),
            self.analyze_sentiment(user_input)
        )
        
        intent_result, entities_result, language, sentiment_result = results
        
        return {
            "intent": intent_result["primary_intent"],
            "intent_details": intent_result,
            "entities": entities_result,
            "language": language,
            "sentiment": sentiment_result,
            "processed_at": datetime.now().isoformat(),
            "input_text": user_input
        }
