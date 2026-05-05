# Server Setting Summary

이 문서는 맥미니 홈 서버의 현재 설정 상태를 요약한 참고 자료입니다. 설정 변경 시 이 파일을 최신 상태로 업데이트합니다.

## Domain & Cloudflare
- **도메인:** `deepblue.im`, `*.deepblue.im`
- **DNS 상태:** Cloudflare Proxy 활성화 (주황색 구름 ON)
- **SSL/TLS 모드:** `Full`
- **인증서 체계:** **Let's Encrypt (Certbot)** 기반 단일화
  - 외부(Cloudflare Edge)와 내부(Nginx) 인증서 일치.
  - Certbot 컨테이너가 12일 주기로 자동 갱신 수행.

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
  - **Internal DNS:** `*.deepblue.im` -> Mac Mini 내부 IP로 DNS Rewrite 설정 완료.
- **Home Assistant:** 가동 중. `hast.deepblue.im`으로 접속 가능.
- **Cloudflare-DDNS:** 가동 중. 공인 IP 동기화 수행.

## VPN & Internal Network
- **Tailscale:** 사용 중. 외부 접속과 충돌 없음.
- **Synology NAS:** `192.168.219.191`. DSM 포트(5001) 리버스 프록시 연동 완료.
- **Mac Mini Local IP:** `192.168.219.192` (DNS 설정은 안정성을 위해 외부 DNS 8.8.8.8 사용).

## Infrastructure Notes
- **공유기 (GAPM-7500):**
  - 포트 포워딩: 외부 443 -> 192.168.219.192:443
  - **DHCP 설정:** 주 DNS를 맥미니 IP(`192.168.219.192`)로 설정하여 내부망 전체 광고 차단 및 도메인 체계 적용.

---
*마지막 업데이트: 2026-05-05*
