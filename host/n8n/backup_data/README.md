# n8n 데이터 백업 정보 (Docker -> Host 이전용)

이 폴더는 Docker 컨테이너에서 실행되던 n8n의 핵심 데이터를 호스트 프로세스 이전을 위해 백업해둔 폴더입니다.

## 📂 백업 정보
- **백업 일시**: 2026년 5월 16일
- **백업 원본**: `docker/apps/n8n/data/` (Container path: `/home/node/.n8n`)
- **백업 내용**:
    - `database.sqlite`: 모든 워크플로우, 자격 증명(Credentials), 실행 기록이 포함된 메인 DB
    - `config`: n8n 사용자 설정 파일
    - `nodes/`, `storage/`: 추가 설치된 노드 및 바이너리 저장 데이터

## 🚀 추후 활용 방법 (호스트 프로세스 설치 시)
1. **n8n 설치**: 호스트 머신에 Node.js 설치 후 `npm install n8n -g` 명령어로 n8n을 설치합니다.
2. **데이터 복원**:
    - 백업된 `data/` 내부의 모든 파일들을 호스트의 n8n 기본 데이터 경로인 `$HOME/.n8n/` 위치로 복사합니다.
    - 예: `cp -R host/n8n/backup_data/data/* ~/.n8n/`
3. **서비스 실행**: `n8n start` 명령어로 실행하면 기존 워크플로우와 설정을 그대로 사용할 수 있습니다.

---
*주의: 보안을 위해 복원 후 자격 증명(Credentials)이 정상적으로 작동하는지 확인하십시오.*
