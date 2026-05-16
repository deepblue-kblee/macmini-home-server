# Next Actions: Maintenance & Automation

## 🎯 Objective
- 호스트 프로세스 기반 인프라 안정화 및 시스템 자동화(Health Check).

## 🛠️ Execution Plan

### 1. 시스템 안정화 및 자동화 (Current Priority)
- [ ] **통합 헬스체크**: 모든 호스트 서비스 상태, 포트 응답, 심볼릭 링크 무결성을 점검하고 알림을 보내는 Python 스크립트(venv 기반) 구축.
- [ ] **로그 순환**: `newsyslog`를 설정하여 `~/services/*/logs/` 파일 용량 관리.

### 2. 백업 전략 수립
- [ ] `~/services/` 하위의 중요 데이터(DB, 설정)에 대한 오프사이트 백업 자동화.

### 3. Home Assistant 전환 (Postponed)
- [ ] HA 전용 Python venv 환경 구축 (사용자 별도 요청 시 진행).
- [ ] 기존 Docker 볼륨 데이터 마이그레이션 및 서비스 가동.
- [ ] HACS 및 스마트홈 기기 연동성 최종 검증.

### 4. 완료된 항목 (2026-05-16)
- [x] **문서 전수 최신화**: Server Setting Summary, Current State 등 주요 문서의 Docker 잔재 제거 및 호스트 전략 반영 완료.
- [x] **네트워크 설정 정리**: Nginx 및 Fail2ban에서 불필요한 Docker 브리지 대역(172.16.0.0/12) 제거 완료.
- [x] **서비스 복구**: Cloudflare DDNS 라이브러리 문제 해결 및 `venv` 환경 도입 완료.
- [x] **심볼릭 링크 점검**: `~/services/` 하위 주요 링크의 무결성 전수 확인 완료.

---
*Updated on: 2026-05-16 (Transition to Automation Phase)*
