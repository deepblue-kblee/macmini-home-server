# Server Setting Summary

이 문서는 맥미니 홈 서버의 현재 설정 상태를 요약한 참고 자료입니다. 설정 변경 시 이 파일을 최신 상태로 업데이트합니다.

## 🌐 네트워크 3대 원칙 (사용자 의도 반영)
모든 네트워크 및 서비스 설정 변경 시 다음 원칙을 반드시 준수해야 합니다.

1.  **내부 우선 및 전면 허용 (Internal First & Full Access)**
    - **의도:** 집 안(내부망)에서는 어떤 서비스든 불편함 없이 접속 가능해야 함.
    - **라우팅:** `/etc/hosts` 및 AdGuard Home DNS Rewrite를 통해 `*.deepblue.im` 접속 시 맥미니 내부 IP(`192.168.219.192`)로 직접 연결.
    - **권한:** 내부망(192.168.x.x), VPN(100.64.x.x) 접속은 모든 서비스에 대해 **전면 허용**.

2.  **외부망 선별 허용 및 보안 (External Selective Access)**
    - **의도:** 외부에서는 꼭 필요한 서비스만 열고, 보안이 중요한 서비스는 원천 봉쇄함.
    - **라우팅:** 외부망 접속 시 Cloudflare Proxy를 거쳐 보안 계층을 유지.
    - **권한:**
        - **공개 서비스 (n8n, oclw 등):** 외부에서도 자유롭게 접속 가능.
        - **내부 전용 서비스 (adg, hast, nas 등):** 외부망을 통한 접속 시도는 Nginx 수준에서 즉시 **403 Forbidden 차단**.

3.  **정확한 신원 식별 (Accurate IP Identification)**
    - Nginx는 Cloudflare를 통해 들어오는 외부 요청에 대해서만 Real IP 변환을 수행함.
    - 내부망 직접 접속은 `/etc/hosts`를 통해 순수 로컬 IP(`192.168.x.x`)로 인식하여 접근 제어 오작동을 방지함.

---

## 🏗️ 시스템 구성 요약

### 1. Nginx 리버스 프록시 및 도메인 설정
| 도메인 | 서비스 대상 (Internal Target) | 접근 정책 (Access Policy) | 특이 사항 |
| :--- | :--- | :--- | :--- |
| `n8n.deepblue.im` | `localhost:5678` | 전역 허용 | 워크플로우 자동화 (호스트 프로세스) |
| `oclw.deepblue.im` | `localhost:18789` | 전역 허용 | **OpenClaw**, WebSocket |
| `adg.deepblue.im` | `localhost:13080` | **내부망 전용** | AdGuard 관리 UI, `allow/deny` |
| `hast.deepblue.im` | `localhost:8123` | **내부망 전용** | Home Assistant (이전 예정) |
| `nas.deepblue.im` | `192.168.219.100:5000` | **내부망 전용** | Synology NAS, `$is_internal` 체크 |
| `deepblue.im` | `Nginx Static` | 전역 허용 | 기본 루트 도메인 |

**접근 제어 메커니즘:**
- **신원 식별:** `nginx.conf`의 `geo` 모듈을 통해 `$is_internal` 변수 정의 (127.0.0.1, 192.168.0.0/16, 100.64.0.0/10).
- **SSL:** Certbot (Cloudflare DNS Challenge) 기반 와일드카드 인증서 사용. 관리 경로: `/etc/letsencrypt/`

### 2. 활성화된 호스트 서비스 (launchd 관리)
| 서비스명 | 관리 도구 | 설정 경로 | 로그 경로 | 주요 역할 |
| :--- | :--- | :--- | :--- | :--- |
| `Nginx` | `launchd` (root) | `~/services/nginx/` | `~/services/nginx/logs/` | 게이트웨이 및 보안 |
| `AdGuard Home` | `launchd` (root) | `~/services/adguard/` | `~/services/adguard/logs/` | DNS 서버 및 광고 차단 |
| `Cloudflare DDNS`| `launchd` (user) | `~/services/scripts/` | `~/services/scripts/logs/` | DNS IP 자동 갱신 |
| `Fail2Ban` | `launchd` (root) | `/opt/homebrew/etc/fail2ban/` | `/opt/homebrew/var/log/fail2ban.log` | 실시간 침입 차단 |

---

## 💡 주요 참고 사항 및 이슈
- **인프라 구조:** Docker 기반 운영에서 macOS 네이티브 호스트 프로세스 기반 운영으로 전환 완료.
- **서비스 관리:** 모든 핵심 서비스는 `launchd`를 통해 데몬/에이전트로 실행되며, `~/services/` 하위의 심볼릭 링크를 통해 설정 관리.
- **Home Assistant:** 현재 호스트 프로세스(Python venv)로의 이식 대기 중 (최종 단계 진행 예정).
- **Ollama:** 호스트 프로세스로 별도 관리 중.

---
*마지막 업데이트: 2026-05-16 (Docker -> Host Process 기반 구조 전환 반영)*
