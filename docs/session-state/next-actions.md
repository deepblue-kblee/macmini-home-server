# Next Actions: Security Hardening & System Integration

## 🎯 Objective
- 서비스 안정화 및 DNS 최적화 완료 후, 시스템 보안을 더욱 강화하고 비-도커(Non-Docker) 시스템과의 연동을 확장함.

## 🛠️ Step-by-Step Execution Plan

### 1. 보안 강화 (Security Hardening)
- [ ] **Fail2ban 도입:** Nginx 로그를 모니터링하여 반복적인 악의적 접근 차단.
- [ ] **보안 헤더 최적화:** `Content-Security-Policy`, `X-Frame-Options` 등 세부 조정.
- [ ] **접근 제어 확장:** 중요 서비스(n8n 등)에 대해 추가적인 인증 레이어(Authelia 등) 또는 IP 제한 검토.

### 2. 내부 시스템 고도화
- [ ] **Synology NAS:** WOL(Wake on LAN) 연동 스크립트 작성 및 Home Assistant 대시보드 등록.
- [ ] **백업 자동화:** 주요 서비스(`letsencrypt`, `n8n`, `HA`) 설정 데이터의 정기적 백업 체계 구축.

### 3. 모니터링 및 유지보수
- [ ] **Uptime Kuma:** 각 서비스의 가동 상태 모니터링 및 알림 설정.
- [ ] **Log Rotation:** Nginx 및 서비스 로그 파일 용량 관리 설정.

---
*Updated on: 2026-05-05 (DNS 최적화 완료 반영)*
