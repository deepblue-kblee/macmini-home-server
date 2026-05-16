# Current System State (as of 2026-05-16)

## 🏗️ Architecture: Host Process Based (Native)
- **Primary OS**: macOS (Darwin arm64)
- **Service Management**: `launchd` (System Daemons & User Agents)
- **Base Directory**: `~/services/` (Symlinked to `host/` configs)
- **Config Management**: Centralized in Git repo (`host/` directory)
- **Web Root**: `/opt/homebrew/var/www` (Standard Homebrew path for security)
- **Python Env**: Dedicated `venv` for system scripts (~/services/scripts/venv)

## 🚀 Running Services (Host)

| Service | Type | Path | Management | Manual |
| :--- | :--- | :--- | :--- | :--- |
| **Nginx** | Reverse Proxy | `~/services/nginx/` | `launchd` (root) | [README.md](~/services/nginx/README.md) |
| **AdGuard Home** | DNS & Filter | `~/services/adguard/` | `launchd` (root) | [README.md](~/services/adguard/README.md) |
| **Cloudflare DDNS** | IP Sync | `~/services/scripts/` | `launchd` (user) | [README_DDNS.md](~/services/scripts/README_DDNS.md) |
| **Fail2Ban** | Security | `/opt/homebrew/etc/fail2ban/` | `launchd` (root) | [README.md](~/services/fail2ban/README.md) |

## 📦 Pending / Managed Externally
- **Home Assistant**: Deployment on host process (Python venv) postponed - *To be requested later*
- **n8n / Ollama**: Managed as host processes.

## 🔗 Sync Mechanism
- **Config**: `host/` (Git) ↔ `~/services/` (Symlink)
- **Data/Logs**: `~/services/[service]/` (Persistent)

## 🕒 Recent Updates (2026-05-16)
- **헬스체크 스크립트 시스템 공용화**: 어느 계정에서나 `health-check` 명령어로 서비스 상태를 확인할 수 있도록 `/usr/local/share/macmini-server`에 배포 및 `/usr/local/bin` 심볼릭 링크 생성 완료.
- **프로젝트 문서화(README.md)**: Monorepo 구조 및 핵심 관리 기능을 요약한 프로젝트 루트 README.md 생성.
- **헬스체크 출력 시스템 개선**: `health_check.sh`의 출력을 가독성이 높은 테이블 형식으로 개편.
- **백업 전략 재설정**: 설정 파일 중심의 Git 백업을 우선하고, 동적 데이터의 클라우드 백업은 후순위로 조정하여 관리 효율성을 높임.
- **통합 헬스체크 및 로그 관리 도구 배포**: 서비스 생존 여부와 포트 응답을 확인하는 `health_check.sh` 및 로그 로테이션 상태를 요약 출력하는 `log_manager.sh` 구현 완료.
- **로그 관리 자동화 시스템 구축**: macOS `newsyslog`를 활용한 서비스별 로그 로테이션 설정을 완료함.
- **호스트 기반 전략 전면 도입**: Docker 의존성을 제거하고 모든 서비스를 macOS 호스트 프로세스(Launchd)로 이관 완료.
- **네트워크 보안 최신화**: Nginx 및 Fail2ban 설정에서 Docker 전용 대역(172.16.x.x)을 제거하고 로컬 호스트 통신 최적화.
- **서비스 복구 및 격리**: Cloudflare DDNS 라이브러리 충돌 문제를 Python `venv` 도입을 통해 해결하고 안정화.
- **문서 무결성 확보**: 모든 관리 문서에서 Docker 관련 설명을 제거하고 호스트 프로세스 중심 설명으로 동기화.
