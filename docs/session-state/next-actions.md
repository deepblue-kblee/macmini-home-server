# Next Actions: Maintenance & HA Migration

## 🎯 Objective
- 호스트 프로세스 기반 인프라 안정화 및 문서 최신화.

## 🛠️ Execution Plan

### 1. 문서 전수 조사 및 최신화 (Priority)
- [x] **Server Setting Summary 최신화**: Docker 기반 설정을 호스트 네이티브 설정으로 변경 완료.
- [x] **Current State 최신화**: Home Assistant 작업 보류 상태 반영 완료.
- [ ] **기타 문서 검토**: `host/` 및 `docker/` 하위 README 등 잔여 문서들의 전략 일치 여부 확인.

### 2. 시스템 안정화 및 자동화
- [ ] **통합 헬스체크**: 모든 호스트 서비스 상태를 주기적으로 감시하고 알림을 보내는 Python 스크립트 구축.
- [ ] **로그 순환**: `newsyslog`를 설정하여 `~/services/*/logs/` 파일 용량 관리.

### 3. 백업 전략 수립
- [ ] `~/services/` 하위의 중요 데이터(DB, 설정)에 대한 오프사이트 백업 자동화.

### 4. Home Assistant 전환 (Postponed)
- [ ] HA 전용 Python venv 환경 구축 (사용자 별도 요청 시 진행).
- [ ] 기존 Docker 볼륨 데이터 마이그레이션 및 서비스 가동.
- [ ] HACS 및 스마트홈 기기 연동성 최종 검증.

---
*Updated on: 2026-05-16 (Prioritizing documentation and system stabilization)*
