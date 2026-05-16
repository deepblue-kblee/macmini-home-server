# Next Actions: Automation & Maintenance Phase

## 🎯 Objective
- 호스트 프로세스 기반 인프라 안정화 및 시스템 자동화(Health Check/Logging).

## 🛠️ Execution Plan (High Priority)

### 1. 시스템 자동화 및 상태 감시 (Done)
- [x] **통합 헬스체크 스크립트 (Done)**: `health_check.py` 및 `health_check.sh`를 통한 서비스/포트 상태 감시 체계 구축.
- [x] **로그 순환 및 아카이빙 (Done)**: `newsyslog` 설정을 통한 자동 로테이션 구축 및 `log_manager.sh` 래퍼 스크립트 제공.

### 2. 백업 및 데이터 보호
- [ ] `~/services/` 하위의 중요 설정 및 데이터(AdGuard DB 등)를 오프사이트(S3 또는 클라우드 스토리지)로 자동 백업하는 워크플로우 수립.

### 3. Home Assistant (On Demand)
- [ ] 사용자 요청 시 HA용 Python venv 환경 구축 및 Docker 데이터 마이그레이션 착수.

## ✅ Past Achievements (2026-05-16)
- [x] **호스트 전략 전환 완료**: 모든 서비스(Nginx, AdGuard, DDNS, Fail2ban)의 Launchd 이관 및 검증.
- [x] **네트워크 설정 최적화**: Docker 브리지 대역 제거 및 로컬 보안 강화.
- [x] **DDNS 서비스 복구**: Python venv 도입으로 라이브러리 의존성 문제 해결.
- [x] **관리 문서 전수 최신화**: Docker 잔재 제거 및 호스트 프로세스 중심 설명 체계 구축.

---
*Next Session Start Point: 헬스체크 스크립트 설계 및 venv 환경 준비*
