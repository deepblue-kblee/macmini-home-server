# Next Actions: Backup & Reliability Phase

## 🎯 Objective
- 호스트 프로세스 기반 데이터의 영속성 확보 및 오프사이트 백업 자동화.

## 🛠️ Execution Plan (Next Priority)

### 1. 백업 및 데이터 보호
- [ ] **오프사이트 백업 구축**: `~/services/` 하위의 중요 설정 및 데이터(AdGuard DB 등)를 클라우드 스토리지(S3, Google Drive 등)로 자동 백업하는 스크립트 작성.
- [ ] **백업 주기 설정**: `launchd`를 이용한 일일/주간 자동 백업 스케줄링.

### 2. 알림 시스템 연동
- [ ] **헬스체크 알림**: `health_check.sh`의 결과를 텔레그램 또는 이메일로 전송하는 기능 추가.

## ✅ Past Achievements (2026-05-16)
- [x] **통합 헬스체크 시스템**: 서비스/포트 상태 감시 도구(`health_check.sh`) 구축 및 배포.
- [x] **로그 관리 자동화**: `newsyslog` 연동 및 상태 요약 도구(`log_manager.sh`) 구축.
- [x] **호스트 전략 전환**: Nginx, AdGuard, DDNS, Fail2ban 호스트 이관 완료.
- [x] **보안 및 라이브러리 최적화**: Docker 대역 제거 및 Python venv 환경 도입.

---
*Next Session Start Point: 클라우드 백업 스크립트 설계 및 API 연동*
