# Mac Mini Home Server

Mac Mini를 활용한 홈 서버 구축 및 관리 자동화 프로젝트입니다. Docker 기반 서비스와 macOS 호스트 기반 서비스를 결합하여 최적의 안정성과 성능을 제공합니다.

## 🚀 Quick Start (Health Check)

시스템의 모든 사용자는 터미널에서 다음 명령어로 서비스 상태를 즉시 확인할 수 있습니다:

```bash
health-check
```

## 📂 Project Structure

- `docker/apps/`: Docker 기반 서비스 (Home Assistant, n8n, Ollama 등)
- `host/`: macOS 호스트에서 직접 실행되는 서비스 및 설정
  - `nginx/`: 리버스 프록시 및 SSL 설정
  - `adguard/`: AdGuard Home (DNS 차단 및 관리)
  - `scripts/`: 자동화 및 관리 스크립트
- `docs/`: 프로젝트 문서 및 세션 관리 데이터

## 🛠️ Key Features

### 1. 통합 헬스체크 시스템
- `/usr/local/bin/health-check`를 통한 전역 상태 확인.
- 서비스 가동 여부, 포트 점유 상태, 프로세스 생존 여부를 시각적으로 표시.

### 2. 호스트 기반 서비스 최적화
- Nginx, AdGuard Home, Cloudflare DDNS, Fail2ban을 호스트 프로세스로 실행하여 네트워크 오버헤드 최소화 및 안정성 강화.
- `newsyslog`를 활용한 로그 관리 자동화.

### 3. 보안 강화
- 모든 서비스는 SSL/TLS(Let's Encrypt)를 통해 암호화된 연결을 제공.
- Fail2ban을 통한 무단 접근 차단.

## 📝 Maintenance

관련 설정 수정이나 추가 작업은 `docs/session-state/next-actions.md`의 우선순위에 따라 진행됩니다.
