# FastAPI CI/CD Starter (GitHub Actions)

Mẫu repo nhỏ để học CI/CD với GitHub cho ứng dụng **FastAPI**.

## Tính năng
- API mẫu với FastAPI: `GET /` và `GET /health`
- Kiểm thử tự động (pytest)
- Lint & type-check (ruff, mypy)
- Dockerfile + docker-compose
- CI: chạy lint/test/build image trên mỗi push/PR
- CD (tùy chọn): build & push image lên **GHCR** khi push vào `main`

## Chạy local
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
uvicorn app.main:app --reload
```
Truy cập: http://127.0.0.1:8000 và docs: http://127.0.0.1:8000/docs

## Chạy bằng Docker
```bash
docker build -t fastapi-cicd:dev .
docker run -p 8000:8000 --env APP_NAME="FastAPI CI/CD" fastapi-cicd:dev
```
hoặc
```bash
docker compose up --build
```

## Cấu trúc thư mục
```
.
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_health.py
├── .github/workflows/
│   ├── ci.yml
│   └── release.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
└── README.md
```

## CI (tự động chạy trên GitHub Actions)
- `ci.yml`: Lint (ruff), type-check (mypy), test (pytest, coverage), build Docker image (không push)

## CD: Push image lên GHCR (tùy chọn)
- `release.yml`: Khi push vào `main`, workflow sẽ build và **push** image lên **GitHub Container Registry (GHCR)**
- Không cần tạo PAT — dùng luôn `GITHUB_TOKEN` mặc định.
- Image name: `ghcr.io/<owner>/<repo>:<sha>` và `:latest` (với nhánh main)

### Bật GHCR cho repo
1. Vào **Settings → Actions → General**: cho phép read/write package (mặc định OK)
2. Vào **Settings → Packages** (nếu có), kiểm tra quyền mặc định
3. Merge/push vào `main` để kích hoạt `release.yml`

## Nâng cấp (gợi ý)
- Thêm pre-commit (ruff, end-of-file-fixer)
- Triển khai lên: Azure Web App / Azure Container Apps / Fly.io / Railway / Render
- Thêm Helm chart & GitHub Actions deploy vào K8s

---
> Tác giả: bạn 😉. Dự án chỉ là skeleton để học CI/CD, hãy tùy chỉnh theo môi trường thật của bạn.
