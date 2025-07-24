# BOJ Tier SVG Generator

solved.ac 사용자의 상위 100개 문제 티어를 아름다운 SVG로 시각화하는 FastAPI 기반 서비스입니다.

## 🎨 미리보기


<img src="https://topsolved.mayonedev.com/api/boj?handle=mayone6063&row=25&base_color=default">
<img src="https://topsolved.mayonedev.com/api/boj?handle=mayone6063&row=25&base_color=bronze">
<img src="https://topsolved.mayonedev.com/api/boj?handle=mayone6063&row=25&base_color=silver">
<img src="https://topsolved.mayonedev.com/api/boj?handle=mayone6063&row=25&base_color=gold">
<img src="https://topsolved.mayonedev.com/api/boj?handle=mayone6063&row=25&base_color=platinum">
<img src="https://topsolved.mayonedev.com/api/boj?handle=mayone6063&row=25&base_color=diamond">
<img src="https://topsolved.mayonedev.com/api/boj?handle=mayone6063&row=25&base_color=ruby">

## 🚀 빠른 시작

### 설치

```bash
# 저장소 클론
git clone https://github.com/MayoneJY/top-solved.git
cd topsolved

# 의존성 설치
pip install -r requirements.txt
```

### 실행

```bash
uvicorn main:app --reload
```

서버가 `http://localhost:8000`에서 실행됩니다.

## 📋 API 사용법

### 기본 사용

```
GET /api/boj?handle={사용자핸들}&row={한줄에표시할개수}
```
```
![top solved](https://topsolved.mayonedev.com/api/boj?handle={boj_id}&row=25)
```
```
<img src="https://topsolved.mayonedev.com/api/boj?handle={boj_id}&row=25">
```


### 매개변수

| 매개변수 | 타입 | 필수 | 기본값 | 설명 |
|---------|------|------|--------|------|
| `handle` | string | ✅ | - | BOJ/solved.ac 사용자 핸들 |
| `row` | int | ✅ | - | 한 줄에 표시할 아이콘 개수 |
| `base_color` | string | ❌ | `` | 배경 그라데이션 기본 색상 |

### 예시

```bash
# 기본 사용법
GET /api/boj?handle=mayone6063&row=20

# 색상 적용
GET /api/boj?handle=mayone6063&row=25&base_color=default
```

## 🎭 커스터마이징

### 색상 테마 변경

`base_color` 매개변수를 통해 배경 그라데이션 색상을 변경할 수 있습니다:

- `auto` (기본값)
- `default`
- `silver`
- `gold`
- `bronze`
- `platinum`
- `diamond`
- `ruby`

### 레이아웃 조정

- `row`: 한 줄에 표시할 아이콘 개수 (권장: 10-25)

[![Hits](https://hitmeup-backend-593087166771.asia-northeast1.run.app/api/count/increment?url=https%3A%2F%2Fgithub.com%2FMayoneJY%2Ftop-solved&title=hits&title_bg=555555&count_bg=79c83d&edge_flat=false)](https://hitmeup-backend-593087166771.asia-northeast1.run.app)
