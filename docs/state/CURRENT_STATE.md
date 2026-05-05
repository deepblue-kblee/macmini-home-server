# Current State: Service Restoration & Subdomain Architecture (2026-05-05)

## 📡 Connectivity & Domain
- **Domain:** `deepblue.im`, `*.deepblue.im` (Cloudflare Proxied)
- **SSL:** Let's Encrypt (Certbot) 기반으로 단일화 완료.
- **External Access:** 모든 서브도메인(`n8n`, `hast`, `nas`, `adguard`)에 대해 SSL 적용 및 접속 가능.

## 🛡️ Nginx Configuration
- **Certificates:** Let's Encrypt 와일드카드 인증서 사용 (자동 갱신 활성).
- **Architecture:** `ssl_params.conf`를 통한 공통 설정 모듈화 완료.
- **Subdomains:**
  - `n8n.deepblue.im`: n8n 서비스 연동.
  - `hast.deepblue.im`: Home Assistant 연동 (Trusted Proxies 설정 포함).
  - `nas.deepblue.im`: Synology NAS 연동.
  - `adguard.deepblue.im`: AdGuard Home 관리 UI (내부망 전용 접근 제어).
- **Security:** Cloudflare 및 사설 IP 대역에 대한 Real IP 설정 및 신뢰 프록시 설정 최적화.

## ✅ Service Status
- **n8n:** 가동 중 (ON).
- **AdGuard Home:** 가동 중 (ON). 내부 DNS Rewrite(`*.deepblue.im`) 적용 완료.
- **Home Assistant:** 가동 중 (ON).
- **DDNS:** 정상 가동 중.

## 🏠 Internal Network
- **DNS:** 공유기 DHCP 설정을 통해 맥미니(AdGuard Home)를 주 DNS로 사용.
- **Internal Domain:** 내부망에서도 `*.deepblue.im` 도메인 체계 사용 가능.
