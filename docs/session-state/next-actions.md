# Next Actions: Backup & Reliability Phase

## 🎯 Objective
- 호스트 프로세스 기반 데이터의 영속성 확보 및 오프사이트 백업 자동화.

## 🛠️ Execution Plan (Next Priority)

### 1. 알림 시스템 연동
- [ ] **헬스체크 알림**: `health_check.sh`의 결과를 텔레그램 또는 이메일로 전송하는 기능 추가.

### 2. 유지보수 및 확장 (우선순위 낮음)
- [ ] **오프사이트 백업 검토**: 설정 파일은 Git으로 관리하되, 향후 DB 등 동적 데이터의 클라우드 백업(S3 등) 필요성 재검토.
- [ ] **백업 주기 설정**: 필요 시 `launchd`를 이용한 자동 백업 스케줄링.

## ✅ Past Achievements (2026-05-16)
- [x] **헬스체크 스크립트 시스템 공용화**: 어느 계정에서나 `health-check` 명령어로 실행 가능하도록 `/usr/local/bin` 배포 완료.
- [x] **통합 헬스체크 시스템**: 서비스/포트 상태 감시 도구(`health_check.sh`) 구축 및 배포.
- [x] **로그 관리 자동화**: `newsyslog` 연동 및 상태 요약 도구(`log_manager.sh`) 구축.
- [x] **호스트 전략 전환**: Nginx, AdGuard, DDNS, Fail2ban 호스트 이관 완료.
- [x] **보안 및 라이브러리 최적화**: Docker 대역 제거 및 Python venv 환경 도입.

---
*Next Session Start Point: 클라우드 백업 스크립트 설계 및 API 연동*
