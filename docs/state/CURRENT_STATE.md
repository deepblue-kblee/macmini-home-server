# Current State: DNS Optimization & Tailscale Integration (2026-05-05)

## 📡 Connectivity & Domain
- **Domain:** `deepblue.im`, `*.deepblue.im` (Cloudflare Proxied)
- **SSL:** Let's Encrypt (Certbot) 기반 단일화 완료.
- **Internal DNS:**
  - AdGuard Home을 통한 `deepblue.im` 및 `*.deepblue.im` Rewrite 적용 (`192.168.219.192`).
  - 맥미니 본체 전용 `/etc/resolver` 설정으로 로컬 호출 성능 최적화 완료.

## 🛡️ VPN & Network
- **Tailscale:** 상시 가동 중 (비상 접근성 확보).
  - **MagicDNS:** `macmini.story-pierce.ts.net` 사용 가능.
  - **Split DNS:** `deepblue.im` 질의를 맥미니 AdGuard(`100.99.21.73`)로 라우팅하여 외부에서도 내부 IP로 즉시 접속 가능.

## ✅ Service Status
- **n8n / Home Assistant / NAS:** 내부망 IP로 직접 연결 및 리버스 프록시 연동 정상.
- **Ollama:** 구성 완료 및 모델 서빙 준비 상태.
- **Custom Commands:** `/kb:update-summary` 등 커스텀 커맨드 스키마 오류 수정 완료.

## 🏠 Infrastructure
- **Router:** DHCP DNS를 맥미니로 설정하여 네트워크 전체 광고 차단 및 도메인 체계 적용.
