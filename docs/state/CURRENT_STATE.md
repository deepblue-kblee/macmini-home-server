# Current System State (as of 2026-05-16)

## 🏗️ Architecture: Host Process Based (Native)
- **Primary OS**: macOS (Darwin arm64)
- **Service Management**: `launchd` (System Daemons & User Agents)
- **Base Directory**: `~/services/` (Symlinked to `host/` configs)
- **Config Management**: Centralized in Git repo (`host/` directory)
- **Web Root**: `/opt/homebrew/var/www` (Standard Homebrew path for security)

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
