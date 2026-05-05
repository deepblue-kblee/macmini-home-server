# Current State: DNS Optimization & Tailscale Integration (2026-05-05)

## 📡 Connectivity & Domain
- **Domain:** `deepblue.im`, `*.deepblue.im` (Cloudflare Proxied)
- **SSL:** Let's Encrypt (Certbot) 기반 단일화 완료.
- **Internal DNS:**
  - AdGuard Home을 통한 `deepblue.im` 및 `*.deepblue.im` Rewrite 적용 (`192.168.219.192`).
  - 맥미니 본체 전용 `/etc/resolver` 설정으로 로컬 호출 성능 최적화 완료.

## 🔒 Security & Access Control (Updated 2026-05-05)
- **네트워크 3대 원칙 확립:** 내부 전면 허용, 외부망 선별 차단 정책 수립.
- **Fail2ban 도입:** Nginx 로그 감시를 통한 침입 IP 자동 차단 시스템 가동.
- **HTTP 보안 헤더:** HSTS, X-Frame-Options 등 주요 보안 헤더 적용 완료.
- **geo 모듈 기반 접근 제어:** `$is_internal` 변수를 이용해 내부망/VPN 접속은 허용하고 외부 우회 접속은 Nginx 수준에서 원천 차단.
- **로그 관리 정책:** 모든 주요 서비스(Nginx, AdGuard, Fail2ban)에 10MB x 3개 로그 순환 정책 적용.

## ✅ Service Status
- **adg.deepblue.im:** AdGuard Home (도메인 단축 및 내부 전용 설정 완료).
- **hast.deepblue.im:** Home Assistant (내부 전용 설정 완료).
- **n8n.deepblue.im:** 전역 허용 상태 유지.
- **nas.deepblue.im:** Synology NAS 리버스 프록시 및 내부 전용 설정 완료.
- **n8n / Home Assistant / NAS:** 내부망 IP로 직접 연결 및 리버스 프록시 연동 정상.
- **Ollama:** 구성 완료 및 모델 서빙 준비 상태.
- **Custom Commands:** `/kb:update-summary` 등 커스텀 커맨드 스키마 오류 수정 완료.

## 🏠 Infrastructure
- **Router:** DHCP DNS를 맥미니로 설정하여 네트워크 전체 광고 차단 및 도메인 체계 적용.
