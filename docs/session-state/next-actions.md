# Next Actions: Security Hardening & System Integration

## 🎯 Objective
- 서비스 안정화 및 DNS 최적화 완료 후, 시스템 보안을 더욱 강화하고 비-도커(Non-Docker) 시스템과의 연동을 확장함.

## 🛠️ Step-by-Step Execution Plan

### 1. 보안 및 로그 관리 (Completed)
- [x] **Fail2ban 도입:** 실시간 침입 차단 체계 구축.
- [x] **보안 헤더 최적화:** 브라우저 보안 강화.
- [x] **로그 순환 정책:** Docker 로그 드라이버 설정을 통한 용량 관리 자동화.
- [x] **네트워크 3대 원칙 구현:** geo 모듈 기반 내부/외부 접속 분기 처리.

### 2. 내부 시스템 고도화 (Next Session)
- [ ] **Synology NAS:** WOL 연동 스크립트 작성 및 Home Assistant 대시보드 등록.
- [ ] **백업 자동화:** 주요 서비스 설정 데이터의 정기적 백업 체계 구축.
- [ ] **Uptime Kuma:** 서비스 가동 상태 모니터링 및 알림 설정.

### 3. 모니터링 및 유지보수
- [ ] **Uptime Kuma:** 각 서비스의 가동 상태 모니터링 및 알림 설정.
- [ ] **Log Rotation:** Nginx 및 서비스 로그 파일 용량 관리 설정.

---
*Updated on: 2026-05-05 (DNS 최적화 완료 반영)*
