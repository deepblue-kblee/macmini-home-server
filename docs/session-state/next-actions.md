# Next Actions: Service Restoration & Hardening

## 🎯 Objective
- 외부 접속 안정화 이후, 중지된 서비스들을 단계적으로 복구하고 보안을 강화함.

## 🛠️ Step-by-Step Execution Plan

### 1. 보안 강화 (Security Hardening)
- [ ] Cloudflare IP를 통해서만 443 포트 접속을 허용하도록 Nginx `allow/deny` 설정 검토.
- [ ] Fail2ban 또는 Nginx 보안 헤더 (HSTS, CSP 등) 적용.

### 2. 서비스 복구 및 연동
- [ ] **n8n:** 컨테이너 실행 및 Nginx 업스트림 연결 복구 (`n8n.conf` 활성화).
- [ ] **AdGuard Home:** DNS 루프 방지 및 업스트림 최적화 후 재가동.

### 3. 내부 시스템 연동
- [ ] **Synology NAS:** WOL 연동 및 Nginx 리버스 프록시를 통한 외부 접근 경로 설정.
- [ ] **HomeAssistant:** 현재 구성 확인 및 Nginx 연동 준비.

---
*Updated on: 2026-05-04*
