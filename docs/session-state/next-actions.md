# Next Actions: Automation & Maintenance Phase

## 🎯 Objective
- 호스트 프로세스 기반 인프라 안정화 및 시스템 자동화(Health Check/Logging).

## 🛠️ Execution Plan (High Priority)

### 1. 시스템 자동화 및 상태 감시 (Next Task)
- [ ] **통합 헬스체크 스크립트**: 모든 호스트 서비스 상태, 포트 응답, 심볼릭 링크 무결성을 점검하고 텔레그램/이메일 알림을 보내는 Python 스크립트(`~/services/scripts/health_check.py`) 구축.
- [ ] **로그 순환 및 아카이빙**: `newsyslog` 설정을 통해 `~/services/*/logs/` 파일 용량 관리 및 주기적 압축 보관.

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
