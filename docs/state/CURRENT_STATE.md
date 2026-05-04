# Current State: Domain & Gateway Setup (2026-05-04)

## 📡 Connectivity & Domain
- **Domain:** `deepblue.im` (Cloudflare Proxied)
- **SSL:** `Full (Strict)` 모드 활성화 및 Cloudflare Origin CA 적용 완료.
- **External Access:** 성공 (HTTP/2 200 OK). Cloudflare 'Browser Integrity Check' OFF로 523 에러 해결.

## 🛡️ Nginx Configuration
- **Certificates:** Cloudflare Origin CA (15년) 설치 (`/etc/nginx/certs/`).
- **IPv6:** 활성화 (`listen [::]:443`).
- **Real IP:** Cloudflare IP 대역 등록 및 `CF-Connecting-IP` 헤더 연동 완료.
- **Static Content:** 기본 `index.html` 서비스 중.

## 🚫 Service Status
- **AdGuard Home:** 중지 (OFF).
- **n8n:** 중지 (OFF), Nginx 설정파일(`n8n.conf.bak`) 비활성화.
- **DDNS:** 정상 작동 중.
