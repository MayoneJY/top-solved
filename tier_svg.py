# tier_svg.py
def generate_svg(tier, x=0, y=0, delay=0.0, width=40, height=40):
    # 1~5 bronze #ad5600
    # 6~10 silver #435f7a
    # 11~15 gold #ec9a00
    # 16~20 platinum #27e2a4
    # 21~25 diamond #00b4fc
    # 26~30 ruby #ff0062
    if tier < 0 or tier > 30:
        raise ValueError("Tier must be between 1 and 30")
    if tier == 0:
        color = "#2d2d2d"
    elif tier <= 5:
        color = "#ad5600"
    elif tier <= 10:
        color = "#435f7a"
    elif tier <= 15:
        color = "#ec9a00"
    elif tier <= 20:
        color = "#27e2a4"
    elif tier <= 25:
        color = "#00b4fc"
    else:
        color = "#ff0062"

    # Generate SVG content
    svg = f"""<g style="animation-delay: {delay}s" class="tier-icon"><svg xmlns="http://www.w3.org/2000/svg" x="{x}" y="{y-2}" width="{width}" height="{height}" viewBox="0 0 100 100">
        <style>
            .g-text {{ font-family: NotoSansKR-Black, Noto Sans KR, Arial, sans-serif; font-size: 60px; font-weight: 800; fill: white; }}
        </style>
        <polygon 
            points="12,0 88,0 88,80 50,100 12,80"
            fill="{color}"
        />
        <polygon 
            points="12,62 50,82 88,62 88,70 50,90 12,70"
            fill="white"
        />
        <text class="g-text" x="49%" y="42%" dominant-baseline="middle" text-anchor="middle">{"?" if tier==0 else 6 - ((tier - 1) % 5 + 1)}</text>
        </svg></g>
    """

    return svg