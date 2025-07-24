# main.py

from fastapi import FastAPI, Response
import requests
from colors import TierSystem

from tier_svg import generate_svg

app = FastAPI()

@app.get("/api/boj")
def generate_tier_svg(handle: str, row: int, base_color: str|None = None):
    if row > 25:
        row = 25
    elif row < 1:
        row = 1
    if base_color == "auto":
        base_color = None
    solved_url = f"https://solved.ac/api/v3/user/top_100?handle={handle}"
    solved_url2 = f"https://solved.ac/api/v3/user/show?handle={handle}"
    res = requests.get(solved_url)
    res2 = requests.get(solved_url2)

    if res.status_code != 200 or res2.status_code != 200:
        # print(res.status_code, res2.status_code)
        levels = []
        svg = build_svg_from_tiers(levels, "Unknown", cell_size=20, gap=12, row_count=row, base_color=base_color)
        response = Response(content=svg, media_type="image/svg+xml")
        response.headers["Cache-Control"] = "no-cache"
        return response

    data = res.json()["items"]
    data2 = res2.json()
    levels = [item["level"] for item in data]
    tier = data2["tier"]

    svg = build_svg_from_tiers(levels, handle, boj_tier=tier, cell_size=20, gap=12, row_count=row, base_color=base_color)
    
    response = Response(content=svg, media_type="image/svg+xml")
    response.headers["Cache-Control"] = "no-cache"
    return response


# svg_builder.py

def build_svg_from_tiers(levels, boj_id, boj_tier=0, cell_size=45, gap=12, row_count=25, base_color="default"):
    """
    아름답게 꾸민 가로 100%, 세로 400px 고정 SVG
    """
    total_icons = len(levels)
    padding = 10
    fixed_height = 170
    
    # 한 줄에 고정 20개
    icons_per_row = row_count
    actual_rows = (total_icons + icons_per_row - 1) // icons_per_row
    
    # viewBox 크기를 20개 기준으로 고정 계산
    viewbox_width = icons_per_row * cell_size + (icons_per_row - 1) * gap + (padding * 2) + 40
    viewbox_height = max(fixed_height, actual_rows * cell_size + (actual_rows - 1) * gap + (padding * 2))
    
    svg_header = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
        viewBox="0 0 {viewbox_width} 170" 
        width="{viewbox_width}px" 
        height="170px"
        preserveAspectRatio="xMidYTop meet"
        style="border-radius: 14px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
        <style type="text/css">
        <![CDATA[
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@600&display=swap');
            text {{
            font-family: 'Inter', sans-serif;
            font-size: 24px;
            font-weight: 600;
            fill: white;
            text-rendering: geometricPrecision;
            }}
        ]]>
        </style>
        '''
    tierSystem = TierSystem()
    if base_color:
        svg_header += tierSystem.generate_svg_gradient(base_color)
    else:
        svg_header += tierSystem.generate_svg_gradient(tierSystem.get_tier_by_level(boj_tier)["tier"])
    svg_header += f'''
        
        <!-- 배경 -->
        <rect width="100%" height="100%" fill="url(#bgGradient)"/>
        
        <!-- 장식용 패턴 -->
        <circle cx="50" cy="50" r="80" fill="rgba(255,255,255,0.05)" opacity="0.6"/>
        <circle cx="{viewbox_width-50}" cy="{viewbox_height-50}" r="60" fill="rgba(255,255,255,0.05)" opacity="0.4"/>
        <style type="text/css">
            .tier-icon {{
                opacity: 0;
                transform-origin: center;
                animation: magicalAppear 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55) forwards;
                filter: url(#softShadow);
                cursor: pointer;
            }}
            
            .tier-icon:hover {{
                transform: scale(1.15);
                filter: url(#iconGlow) url(#softShadow);
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            }}

            .tier_level {{
                opacity: 0.4;
            }}
            
            .sparkle {{
                opacity: 0;
                animation: sparkleAnim 2s ease-in-out infinite;
            }}
            
            @keyframes magicalAppear {{
                0% {{ 
                    opacity: 0; 
                    transform: scale(0.5) translateY(20px);
                }}
                60% {{
                    transform: scale(1.05) translateY(-5px);
                }}
                100% {{ 
                    opacity: 1; 
                    transform: scale(1) translateY(0);
                }}
            }}
            
            @keyframes bounce {{
                0%, 20%, 50%, 80%, 100% {{
                    transform: scale(1.2) translateY(0);
                }}
                40% {{
                    transform: scale(1.25) translateY(-8px);
                }}
                60% {{
                    transform: scale(1.25) translateY(-4px);
                }}
            }}
            
            @keyframes sparkleAnim {{
                0%, 100% {{ opacity: 0; transform: scale(0.8); }}
                50% {{ opacity: 0.8; transform: scale(1.2); }}
            }}
            
            @keyframes float {{
                0%, 100% {{ transform: translateY(0px); }}
                50% {{ transform: translateY(-10px); }}
            }}
        </style>'''
    svg_body = ""
    
    svg_body += f"""
            <text transform="translate(30 14)" style="font-family: 'Inter'; font-size: 14px;" fill="#fff" dominant-baseline="Hanging" text-anchor="start">{boj_id}</text>
            """
    
    svg_body += f"""
            <text transform="translate({viewbox_width - 30} 14)" style="font-family: 'Inter'; font-size: 14px;" fill="#fff" dominant-baseline="Hanging" text-anchor="end">{get_tier_name(boj_tier)}</text>
            """
    
    # 반짝이는 장식 요소들 추가
    for i in range(5):
        x = (i * viewbox_width / 5) + (viewbox_width / 10)
        y = 30 + (i % 2) * 340
        delay = i * 0.5
        svg_body += f'''

            <circle cx="{x}" cy="{y}" r="3" fill="url(#sparkle)" 
                    class="sparkle" style="animation-delay: {delay}s"/>'''
    
    # 아이콘들 배치
    for idx, level in enumerate(levels):
        if idx >= row_count * 4:
            break
        col = idx % icons_per_row
        row = idx // icons_per_row
        
        x = padding + col * (cell_size + gap) + 20
        y = padding + row * (cell_size + gap) + 30
        delay = round(0.1 + idx * 0.05, 2)
        
        # 각 아이콘마다 다른 색상의 배경 원 추가
        bg_colors = ["rgba(255,255,255,0.1)", "rgba(255,255,255,0.15)", "rgba(255,255,255,0.08)"]
        bg_color = bg_colors[idx % 3]
        
        svg_body += f'''
            <!-- 아이콘 배경 원 -->
            <circle cx="{x + cell_size/2}" cy="{y + cell_size/2 - 2}" r="{cell_size/2 + 3}" 
                    fill="{bg_color}" opacity="0" 
                    style="animation: magicalAppear 0.6s ease-out {delay}s forwards;"/>'''
        svg_body += generate_svg(level, x=x, y=y, delay=delay, width=cell_size, height=cell_size)
    # 빈 공간 채우기
    for i in range(len(levels), 4 * row_count):
        if i >= row_count * 4:
            break
        col = i % icons_per_row
        row = i // icons_per_row

        x = padding + col * (cell_size + gap) + 20
        y = padding + row * (cell_size + gap) + 30
        delay = round(0.1 + i * 0.05, 2)
        
        # 각 아이콘마다 다른 색상의 배경 원 추가
        bg_colors = ["rgba(255,255,255,0.1)", "rgba(255,255,255,0.15)", "rgba(255,255,255,0.08)"]
        bg_color = bg_colors[i % 3]

        svg_body += f'''
            <!-- 아이콘 배경 원 -->
            <circle cx="{x + cell_size/2}" cy="{y + cell_size/2 - 2}" r="{cell_size/2 + 3}" 
                    fill="{bg_color}" opacity="0" 
                    style="animation: magicalAppear 0.6s ease-out {delay}s forwards;"/>'''

    # 마지막에 떠다니는 장식 요소들
    svg_body += f'''
        <!-- 떠다니는 장식 -->
        <circle cx="30" cy="200" r="4" fill="rgba(255,255,255,0.3)" 
                style="animation: float 3s ease-in-out infinite;"/>
        <circle cx="{viewbox_width-30}" cy="150" r="3" fill="rgba(255,255,255,0.4)" 
                style="animation: float 4s ease-in-out infinite 1s;"/>
        <circle cx="{viewbox_width/2}" cy="380" r="2" fill="rgba(255,255,255,0.5)" 
                style="animation: float 2.5s ease-in-out infinite 0.5s;"/>'''

    svg_footer = "</svg>"
    return svg_header + svg_body + svg_footer


def get_tier_name(level: int) -> str:
    tiers = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Ruby"]
    
    if not 0 <= level <= 30:
        raise ValueError("레벨은 0부터 30 사이여야 합니다.")
    if level == 0:
        return "unrank"
    # 티어 그룹: 5단계씩 나눔
    group_index = (level - 1) // 5
    tier_name = tiers[group_index]

    # 각 그룹에서 1~5 역순: 1은 5등급, 5는 1등급
    rank_in_group = 6 - ((level - 1) % 5 + 1)

    return f"{tier_name} {rank_in_group}"
