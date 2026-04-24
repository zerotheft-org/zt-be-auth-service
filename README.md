# zt-be-auth-service

Auth Service for the ZeroTheft platform.

## Local Development

```bash
pip install -r requirements.txt
python app/main.py
```

## Docker

```bash
docker build -t zt-be-auth-service .
docker run -p 8000:8000 zt-be-auth-service
```

- **Port:** 8000
- **Health Check:** `GET /health`
- **Root Endpoint:** `GET /`
# Test commit to verify CI → ECR pipeline
# Pipeline test v2
# Pipeline test v3 - hardened image
# Pipeline test v4 - verbose scan output
# Pipeline test v5 - alpine image
# Pipeline test v6 - correct ECR repo name
# Pipeline test v7 - sanitized artifact name

