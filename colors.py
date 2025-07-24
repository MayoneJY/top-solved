"""
등급별 테마 시스템
각 등급(1-30)에 따른 색상과 테마를 관리하는 Python 클래스
"""

class TierSystem:
    def __init__(self):
        # 등급별 테마 정의
        self.tiers = {
            'bronze': {
                'range': (1, 5),
                'color': '#ad5600',
                'name': 'Bronze',
                'description': '구리의 따뜻함, 시작의 단계',
                'effects': ['기본 반짝임', '구리 광택']
            },
            'silver': {
                'range': (6, 10),
                'color': '#435f7a',
                'name': 'Silver',
                'description': '은빛 우아함, 성장의 증거',
                'effects': ['은빛 반사', '차분한 광택', '미세한 파동']
            },
            'gold': {
                'range': (11, 15),
                'color': '#ec9a00',
                'name': 'Gold',
                'description': '황금의 찬란함, 실력의 증명',
                'effects': ['황금 빛줄기', '강렬한 광채', '파티클 효과']
            },
            'platinum': {
                'range': (16, 20),
                'color': '#27e2a4',
                'name': 'Platinum',
                'description': '플래티넘의 고귀함, 엘리트의 영역',
                'effects': ['에메랄드 빛', '펄스 효과', '오로라 반짝임']
            },
            'diamond': {
                'range': (21, 25),
                'color': '#00b4fc',
                'name': 'Diamond',
                'description': '다이아몬드의 순수함, 최고의 경지',
                'effects': ['다이아몬드 프리즘', '무지개 스펙트럼', '크리스탈 효과']
            },
            'ruby': {
                'range': (26, 30),
                'color': '#ff0062',
                'name': 'Ruby',
                'description': '루비의 열정, 전설의 영역',
                'effects': ['루비 화염', '마그마 효과', '레이저 빛', '신화적 오라']
            }
        }
    def get_color_by_level(self, level):
        tier_info = self.get_tier_by_level(level)
        if not tier_info:
            return None
        
        return tier_info['color']
    
    def get_tier_by_name(self, tier_name):
        """등급 이름에 따른 등급 정보 반환"""
        tier_name = tier_name.lower()
        if tier_name not in self.tiers:
            return None
            
        tier_info = self.tiers[tier_name]
        return {
            'tier': tier_name,
            **tier_info
        }
    
    def get_tier_by_level(self, level):
        """레벨에 따른 등급 정보 반환 (기존 호환성 유지)"""
        if not 0 <= level <= 30:
            return None
            
        for tier_name, tier_info in self.tiers.items():
            min_level, max_level = tier_info['range']
            if min_level <= level <= max_level:
                return {
                    'tier': tier_name,
                    'level': level,
                    **tier_info
                }
        return None
    
    def generate_svg_gradient(self, tier_name):
        """등급 이름에 맞는 SVG 그라데이션 생성"""
        if tier_name and tier_name != "default":
            tier_info = self.get_tier_by_name(tier_name)
            if not tier_info:
                return None
            
            color = tier_info['color']
            tier = tier_info['tier']
        else:
            tier = None
        result = '''<defs>
        <radialGradient id="sparkle" cx="50%" cy="50%" r="50%"> 
            <stop offset="0%" style="stop-color:rgba(255,255,255,0.8);stop-opacity:1" /> 
            <stop offset="100%" style="stop-color:rgba(255,255,255,0);stop-opacity:0" /> 
        </radialGradient> 
        <!-- 아이콘 테두리 효과 --> 
        <filter id="iconGlow" x="-50%" y="-50%" width="200%" height="200%"> 
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/> 
            <feMerge> 
            <feMergeNode in="coloredBlur"/> 
            <feMergeNode in="SourceGraphic"/> 
        </feMerge> 
        </filter> 
        <!-- 부드러운 그림자 --> 
        <filter id="softShadow" x="-50%" y="-50%" width="200%" height="200%"> 
            <feDropShadow dx="3" dy="3" stdDeviation="2" flood-opacity="0.3"/> 
        </filter> '''
        # 등급별 특별한 그라데이션 패턴
        if tier == 'bronze':
            result += f'''
            <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:{color};stop-opacity:1" />
                <stop offset="50%" style="stop-color:#d4691a;stop-opacity:1" />
                <stop offset="100%" style="stop-color:{color};stop-opacity:1" />
            </linearGradient>'''
            
        elif tier == 'silver':
            result +=  f'''
            <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#5a7a9a;stop-opacity:1" />
                <stop offset="50%" style="stop-color:{color};stop-opacity:1" />
                <stop offset="100%" style="stop-color:#6b8db5;stop-opacity:1" />
            </linearGradient>'''
            
        elif tier == 'gold':
            result +=  f'''
            <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#ffb000;stop-opacity:1" />
                <stop offset="25%" style="stop-color:{color};stop-opacity:1" />
                <stop offset="75%" style="stop-color:#ffd700;stop-opacity:1" />
                <stop offset="100%" style="stop-color:{color};stop-opacity:1" />
            </linearGradient>'''
            
        elif tier == 'platinum':
            result +=  f'''
            <radialGradient id="bgGradient" cx="50%" cy="50%" r="70%">
                <stop offset="0%" style="stop-color:#40e8b0;stop-opacity:1" />
                <stop offset="50%" style="stop-color:{color};stop-opacity:1" />
                <stop offset="100%" style="stop-color:#1ad4a0;stop-opacity:1" />
            </radialGradient>'''
            
        elif tier == 'diamond':
            result +=  f'''
            <radialGradient id="bgGradient" cx="50%" cy="50%" r="80%">
                <stop offset="0%" style="stop-color:#66c2ff;stop-opacity:1" />
                <stop offset="30%" style="stop-color:{color};stop-opacity:1" />
                <stop offset="70%" style="stop-color:#0099e6;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#004d80;stop-opacity:1" />
            </radialGradient>'''
            
        elif tier == 'ruby':
            result +=  f'''
            <radialGradient id="bgGradient" cx="50%" cy="50%" r="60%">
                <stop offset="0%" style="stop-color:#ff3380;stop-opacity:1" />
                <stop offset="25%" style="stop-color:{color};stop-opacity:1" />
                <stop offset="50%" style="stop-color:#ff0040;stop-opacity:1" />
                <stop offset="75%" style="stop-color:#cc0050;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#990040;stop-opacity:1" />
            </radialGradient>'''
        else:
            result +=  f'''
            <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%"> 
                <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" /> 
                <stop offset="50%" style="stop-color:#764ba2;stop-opacity:1" /> 
                <stop offset="100%" style="stop-color:#f093fb;stop-opacity:1" /> 
            </linearGradient>'''
        result += "</defs>"
        return result
    