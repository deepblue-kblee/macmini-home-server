# Current State: DNS Optimization & AdGuard Recovery (2026-05-06)

## 📡 Connectivity & Domain
- **Domain:** `deepblue.im`, `*.deepblue.im` (Cloudflare Proxied)
- **Internal DNS:**
  - AdGuard Home을 통한 `deepblue.im` 및 `*.deepblue.im` Rewrite 적용 (`192.168.219.192`).
  - **AdGuard Home 복구 완료:** 이미지 버전(`v0.107.73`)과 설정 파일(`schema_version: 34`) 간의 불일치로 인한 무한 재시작 장애 해결. 최신 이미지로 업데이트 및 정상화.

## 🔒 Security & Access Control
- **네트워크 3대 원칙 확립:** 내부 전면 허용, 외부망 선별 차단 정책 운영 중.
- **Fail2ban 도입:** 실시간 침입 차단 체계 가동 중.
- **geo 모듈 기반 접근 제어:** 내부망/VPN 접속 허용 및 외부 우회 접속 차단 정책 적용.

## ✅ Service Status
- **adg.deepblue.im:** AdGuard Home (정상 가동 중, `v0.107.74+`).
- **hast.deepblue.im / n8n.deepblue.im / nas.deepblue.im:** 리버스 프록시 연동 정상.
- **Ollama:** 구성 완료 및 모델 서빙 중.

## 🏠 Infrastructure
- **Docker Desktop:** 현재 사용 중. Colima 전환 대기 상태.
- **Router:** DHCP DNS가 맥미니로 설정되어 네트워크 전체 광고 차단 적용 중.
