# Next Actions: Infrastructure Migration & Monitoring

## 🎯 Objective
- Docker Desktop을 Colima로 대체하여 리소스 효율을 높이고, 서비스 모니터링 및 백업 체계를 강화함.

## 🛠️ Step-by-Step Execution Plan

### 1. 인프라 고도화 (Next Priority)
- [ ] **Docker Desktop -> Colima 전환:**
    - [ ] Colima 설치 및 Rosetta/VirtioFS 최적화 설정.
    - [ ] `launchd`를 이용한 맥 부팅 시 Colima 자동 실행 스크립트 등록.
- [ ] **관리 도구 구축:**
    - [ ] Portainer 설치 및 `portainer.deepblue.im` (내부망 전용) 도메인 연결.
    - [ ] Uptime Kuma 도입: 서비스 가동 상태 모니터링 및 알림 설정.

### 2. 네트워크 및 서비스 디버깅
- [!] **Nginx 내부망 접근 이슈:** 일부 환경에서 `allow/deny` 정책으로 인해 발생하는 접근 차단 현상 디버깅 및 수정.
- [ ] **Synology NAS 연동:** WOL 스크립트 작성 및 Home Assistant 대시보드 통합.

### 3. 유지보수 및 백업
- [ ] **백업 자동화:** 서비스 설정 및 중요 데이터 정기 백업 스크립트 작성.
- [ ] **로그 순환 점검:** Nginx 및 서비스 로그 용량 관리 정책 실효성 확인.

---
*Updated on: 2026-05-06 (AdGuard 복구 완료 및 Colima 전환 과업 재확인)*
