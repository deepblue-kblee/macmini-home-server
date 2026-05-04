# Server Setting Summary

이 문서는 맥미니 홈 서버의 현재 설정 상태를 요약한 참고 자료입니다. 설정 변경 시 이 파일을 최신 상태로 업데이트합니다.

## 🌐 Domain & Cloudflare
- **도메인:** `deepblue.im`, `*.deepblue.im`
- **DNS 상태:** Cloudflare Proxy 활성화 (주황색 구름 ON)
- **SSL/TLS 모드:** `Full (Strict)`
- **Cloudflare 설정 특징:**
  - `Browser Integrity Check`: OFF (523 에러 해결을 위해 비활성화)
  - `IPv6 Compatibility`: ON (필요 시 OFF 검토 가능)
- **DDNS:** `favonia/cloudflare-ddns` 컨테이너 사용 중
  - 5분 간격으로 공인 IP(`182.209.125.58`) 동기화

## 🛡️ Nginx (Gateway)
- **인증서:** Cloudflare Origin CA 인증서 (15년 만기)
  - 파일 위치: `docker/apps/nginx/certs/cert.pem`, `key.pem`
- **Port 구성:** `80` (HTTP), `443` (HTTPS)
- **주요 설정 (conf.d/default.conf):**
  - 모든 443 요청을 `deepblue.im` 블록으로 수용 (`default_server`)
  - IPv6 리스닝 활성화 (`listen [::]:443`)
  - Cloudflare Real IP 설정 적용 (`set_real_ip_from` 대역 등록 및 `CF-Connecting-IP` 헤더 사용)
  - HTTP -> HTTPS 강제 리다이렉트 활성화
- **컨테이너 상태:** 실행 중 (`Up`)

## 🚫 비활성화된 서비스 (OFF)
- **AdGuard Home:** 현재 중지 상태 (`docker stop adguard`)
  - 특별한 지침이 있을 때까지 OFF 유지.
- **n8n:** 현재 중지 상태 (`n8n.conf`는 복구되었으나 컨테이너 미가동)
  - 특별한 지침이 있을 때까지 OFF 유지.

## 🔗 VPN & Internal Network
- **Tailscale:** 사용 중
  - VPN ON 상태에서도 외부 접속(Cloudflare Proxy)과 충돌 없음 확인.
- **Synology NAS:**
  - 고정 IP: `192.168.219.191`
  - 상태: WOL(Wake on LAN) 대기 중. 향후 HomeAssistant 등과 연동 예정.
- **Mac Mini Local IP:** `192.168.219.192`

## 🛠️ Infrastructure Notes
- **공유기 (GAPM-7500):**
  - 포트 포워딩: 외부 443 -> 192.168.219.192:443
  - 특이사항: 단순한 UI로 방화벽 세부 설정 제약이 있음.

---
*마지막 업데이트: 2026-05-04*
