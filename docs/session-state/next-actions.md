# Next Actions: Maintenance & HA Migration

## 🎯 Objective
- 호스트 프로세스 기반 인프라 안정화 및 Home Assistant 이식.

## 🛠️ Execution Plan

### 1. 시스템 안정화 및 자동화
- [ ] **통합 헬스체크**: 모든 호스트 서비스 상태를 주기적으로 감시하고 알림을 보내는 Python 스크립트 구축.
- [ ] **로그 순환**: `newsyslog`를 설정하여 `~/services/*/logs/` 파일 용량 관리.
- [ ] **문서 전수 조사**: Repo 내 기존 문서들이 변경된 전략(Docker -> Host)을 정확히 반영하고 있는지 체크하고 수정.

### 2. Home Assistant 전환 (Priority)
- [ ] HA 전용 Python venv 환경 구축.
- [ ] 기존 Docker 볼륨 데이터 마이그레이션 및 서비스 가동.
- [ ] HACS 및 스마트홈 기기 연동성 최종 검증.

### 3. 백업 전략 수립
- [ ] `~/services/` 하위의 중요 데이터(DB, 설정)에 대한 오프사이트 백업 자동화.

---
*Updated on: 2026-05-16 (Docker -> Host Process Migration Complete)*
