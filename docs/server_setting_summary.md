# Server Setting Summary

이 문서는 맥미니 홈 서버의 현재 설정 상태를 요약한 참고 자료입니다. 설정 변경 시 이 파일을 최신 상태로 업데이트합니다.

## 🌐 네트워크 3대 원칙 (사용자 의도 반영)
모든 네트워크 및 서비스 설정 변경 시 다음 원칙을 반드시 준수해야 합니다.

1.  **내부 우선 및 전면 허용 (Internal First & Full Access)**
    - **의도:** 집 안(내부망)에서는 어떤 서비스든 불편함 없이 접속 가능해야 함.
    - **라우팅:** `/etc/hosts` 및 AdGuard Home DNS Rewrite를 통해 `*.deepblue.im` 접속 시 맥미니 내부 IP(`192.168.219.192`)로 직접 연결.
    - **권한:** 내부망(192.168.x.x) 및 VPN(100.64.x.x) 접속은 모든 서비스에 대해 **전면 허용**.

2.  **외부망 선별 허용 및 보안 (External Selective Access)**
    - **의도:** 외부에서는 꼭 필요한 서비스만 열고, 보안이 중요한 서비스는 원천 봉쇄함.
    - **라우팅:** 외부망 접속 시 Cloudflare Proxy를 거쳐 보안 계층을 유지.
    - **권한:**
        - **공개 서비스 (n8n 등):** 외부에서도 자유롭게 접속 가능.
        - **내부 전용 서비스 (adg, hast, nas 등):** 외부망을 통한 접속 시도는 Nginx 수준에서 즉시 **403 Forbidden 차단**.

3.  **정확한 신원 식별 (Accurate IP Identification)**
    - Nginx는 Cloudflare를 통해 들어오는 외부 요청에 대해서만 Real IP 변환을 수행함.
    - 내부망 직접 접속은 `/etc/hosts`를 통해 순수 로컬 IP(`192.168.x.x`)로 인식하여 접근 제어 오작동을 방지함.

---

## Nginx (Gateway)
- **공통 설정 (`conf.d/common/ssl_params.conf`):**
    - Cloudflare Real IP 식별 정상화 및 보안 헤더 적용 완료.
- **서브도메인 접근 정책:**
    - `n8n.deepblue.im`: 전역 허용.
    - `adg.deepblue.im`: **내부망 전용** (AdGuard Home).
    - `hast.deepblue.im`: **내부망 전용** (Home Assistant).
    - `nas.deepblue.im`: **내부망 전용** (Synology NAS).

## 활성화된 서비스 (ON)
- **n8n / AdGuard Home(adg) / Home Assistant(hast) / Fail2ban / Ollama / Cloudflare-DDNS**

## VPN & Internal Network
- **Tailscale:** 상시 가동 중 (`100.99.21.73`).
- **Mac Mini Local IP:** `192.168.219.192`.

---
*마지막 업데이트: 2026-05-05 (AdGuard 도메인 단축 및 로컬 접속 최적화 완료)*
