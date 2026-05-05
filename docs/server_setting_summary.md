# Server Setting Summary

이 문서는 맥미니 홈 서버의 현재 설정 상태를 요약한 참고 자료입니다. 설정 변경 시 이 파일을 최신 상태로 업데이트합니다.

## Domain & Cloudflare
- **도메인:** `deepblue.im`, `*.deepblue.im`
- **DNS 상태:** Cloudflare Proxy 활성화 (주황색 구름 ON)
- **SSL/TLS 모드:** `Full`
- **인증서 체계:** **Let's Encrypt (Certbot)** 기반 단일화
  - 외부(Cloudflare Edge)와 내부(Nginx) 인증서 일치.
  - Certbot 컨테이너가 자동 갱신 수행.

## Nginx (Gateway)
- **Port 구성:** `80` (HTTP), `443` (HTTPS)
- **공통 설정 (`conf.d/common/ssl_params.conf`):**
  - SSL 프로토콜 (TLS 1.2, 1.3), 최적화된 사이퍼 스위트 적용.
  - Cloudflare 및 내부 사설 IP 대역에 대한 Real IP 설정 통합.
- **서브도메인 리버스 프록시 구성:**
  - `n8n.deepblue.im`: n8n 서비스 연결.
  - `hast.deepblue.im`: Home Assistant 연결 (WebSocket 및 Trusted Proxies 설정 완료).
  - `nas.deepblue.im`: Synology NAS (192.168.219.191) 연결.
  - `adguard.deepblue.im`: AdGuard Home 관리 UI (내부망 전용 접속 제한).
- **컨테이너 상태:** 실행 중 (`Up`)

## 활성화된 서비스 (ON)
- **n8n:** 가동 중. 서브도메인을 통해 외부 접속 가능.
- **AdGuard Home:** 가동 중.
  - **Internal DNS Rewrite:** `deepblue.im` 및 `*.deepblue.im` -> Mac Mini 내부 IP(`192.168.219.192`)로 연결되도록 설정 완료.
- **Home Assistant:** 가동 중. `hast.deepblue.im`으로 접속 가능.
- **Cloudflare-DDNS:** 가동 중. 공인 IP 동기화 수행.
- **Ollama:** 구성됨. LLM 모델 서빙 준비 상태.

## VPN & Internal Network
- **Tailscale:** **상시 가동 중.**
  - **기기 정보:**
    - **Mac Mini (본체):** `100.99.21.73`
      - **MagicDNS:** `macmini.story-pierce.ts.net` (또는 간단히 `macmini`)
    - **Tailscale 도메인:** `story-pierce.ts.net`
    - **연결 기기:** iPhone 16 Pro (`100.106.50.94`) 등 개인 기기망 구성.
  - **MagicDNS & Split DNS:**
    - **Split DNS:** `deepblue.im` 도메인 질의를 Mac Mini의 AdGuard Home(`100.99.21.73`)으로 라우팅.
    - **Global Nameservers:** 시스템 기본값(1.1.1.1 등)과 혼용하여 안정성 확보.
- **Mac Mini 로컬 최적화 (Loopback):**
  - **`/etc/resolver` 설정:** 맥미니 본체에서 `deepblue.im` 호출 시 Tailscale 인터페이스(`utun`)나 외부망을 거치지 않고 로컬 루프백(`127.0.0.1`) AdGuard를 통해 즉시 내부 IP로 연결 (응답 속도 최적화).
- **Synology NAS:** `192.168.219.191`. DSM 포트(5001) 리버스 프록시 연동 완료.
- **Mac Mini Local IP:** `192.168.219.192`.

## Infrastructure Notes
- **공유기 (GAPM-7500):**
  - 포트 포워딩: 외부 443 -> 192.168.219.192:443
  - **DHCP 설정:** 주 DNS를 맥미니 IP(`192.168.219.192`)로 설정하여 내부망 전체 광고 차단 및 도메인 체계 적용.

---
*마지막 업데이트: 2026-05-05 (DNS 최적화 및 Tailscale 가동 정책 반영)*
