# Server Setting Summary

이 문서는 맥미니 홈 서버의 현재 설정 상태를 요약한 참고 자료입니다. 설정 변경 시 이 파일을 최신 상태로 업데이트합니다.

## 🌐 네트워크 3대 원칙 (사용자 의도 반영)
모든 네트워크 및 서비스 설정 변경 시 다음 원칙을 반드시 준수해야 합니다.

1.  **내부 우선 및 전면 허용 (Internal First & Full Access)**
    - **의도:** 집 안(내부망)에서는 어떤 서비스든 불편함 없이 접속 가능해야 함.
    - **라우팅:** `/etc/hosts` 및 AdGuard Home DNS Rewrite를 통해 `*.deepblue.im` 접속 시 맥미니 내부 IP(`192.168.219.192`)로 직접 연결.
    - **권한:** 내부망(192.168.x.x), VPN(100.64.x.x), Docker 내부 대역(172.16.x.x) 접속은 모든 서비스에 대해 **전면 허용**.

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
| `n8n.deepblue.im` | `n8n:5678` (Docker) | 전역 허용 | 워크플로우 자동화 |
| `oclw.deepblue.im` | `host.docker.internal:18789` | 전역 허용 | **호스트(OpenClaw)**, WebSocket |
| `adg.deepblue.im` | `adguard:13080` (Docker) | **내부망 전용** | AdGuard 관리 UI, `allow/deny` |
| `hast.deepblue.im` | `homeassistant:8123` (Docker) | **내부망 전용** | Home Assistant, `allow/deny` |
| `nas.deepblue.im` | `192.168.219.100:5000` | **내부망 전용** | Synology NAS, `$is_internal` 체크 |
| `deepblue.im` | `nginx:html` (Static) | 전역 허용 | 기본 루트 도메인 |

**접근 제어 메커니즘:**
- **신원 식별:** `nginx.conf`의 `geo` 모듈을 통해 `$is_internal` 변수 정의 (127.0.0.1, 192.168.0.0/16, 100.64.0.0/10, 172.16.0.0/12).
- **SSL:** Certbot (Cloudflare DNS Challenge) 기반 와일드카드 인증서 사용.

### 2. 활성화된 Docker 서비스
| 서비스명 | 이미지 | 네트워크 모드 | 포트 맵핑 (호스트:컨테이너) | 주요 역할 |
| :--- | :--- | :--- | :--- | :--- |
| `nginx` | `nginx:latest` | `web` (bridge) | 80:80, 443:443 | 게이트웨이 및 보안 |
| `adguard` | `adguard/adguardhome` | `web` (bridge) | 53, 3000, 13080 | DNS 서버 및 광고 차단 |
| `n8n` | `n8nio/n8n:latest` | `web` (bridge) | 5678:5678 | 워크플로우 자동화 |
| `homeassistant`| `home-assistant:stable`| **host** | N/A | 홈 오토메이션 |
| `fail2ban` | (Custom) | **host** | N/A | 실시간 침입 차단 (L3/L4) |
| `cloudflare-ddns`| `favonia/cloudflare-ddns`| **host** | N/A | DNS IP 자동 갱신 |
| `certbot` | `certbot/dns-cloudflare`| `web` (bridge) | N/A | SSL 인증서 관리 |
| `ollama` | (관리 필요) | (추후 확인) | (11434:11434) | 로컬 LLM 서버 |

---

## 💡 주요 참고 사항 및 이슈
- **호스트 서비스 연동:** `oclw.deepblue.im`은 Docker 외부(맥미니 호스트)에서 실행되는 OpenClaw 서비스를 프록시함. `host.docker.internal` 게이트웨이 사용.
- **네트워크 모드:** Home Assistant 및 보안 서비스(Fail2ban)는 브로드캐스트 인식 및 로그 분석을 위해 `host` 네트워크를 사용함.
- **Ollama:** `docker/apps/ollama/` 디렉토리는 존재하나 현재 설정 파일 보완이 필요한 상태임.

---
*마지막 업데이트: 2026-05-05 (OpenClaw 호스트 서비스 및 Nginx 전수 조사 결과 반영)*
