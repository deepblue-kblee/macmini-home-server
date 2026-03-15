# Mac Mini Home Server Project Context

## 📌 Project Overview
- **Root Directory:** `~/work/repo/macmini-home-server/`
- **Structure:** Monorepo (Docker services + System configs/scripts)
- **Primary Access Path:** `~/docker` (Symlinked to `./docker`)
- **Remote Repo:** [https://github.com/deepblue-kblee/macmini-home-server](https://github.com/deepblue-kblee/macmini-home-server)

## ✅ Completed Tasks
1.  **Repository Refactoring:**
    - Moved `.git` and `.gitignore` from `docker/` to the project root.
    - Successfully pushed the initial structure to GitHub.
    - Verified all files and paths are intact after the move.
2.  **Service Configuration:**
    - `docker/apps/`: AdGuard, Cloudflare-DDNS, Home Assistant, n8n, nginx, ollama.
    - `.gitignore`: Configured to exclude sensitive data (certs, secrets, db, logs).
3.  **Environment Setup:**
    - Created a symbolic link: `ln -s ~/work/repo/macmini-home-server/docker ~/docker`.
    - Verified running containers are stable and paths are correctly resolved.

## 🚀 Execution Plan (Next Steps)
1.  **Documentation & Guide:**
    - Create a comprehensive root `README.md` with setup instructions and architecture diagram.
    - Add service-specific documentation where needed.
2.  **System Configuration (Non-Docker):**
    - Create a `scripts/` directory for automation (e.g., backup, update, health check).
    - Create a `configs/` directory for Mac Mini system-level settings (macOS tweaks, cron jobs).
3.  **Automation & Maintenance:**
    - Develop a master script to manage all Docker services (`up`, `down`, `pull`, `logs`).
    - Implement a backup strategy for the `data/` and `config/` folders.
4.  **Monitoring & Alerts:**
    - (Future) Consider adding monitoring tools (e.g., Prometheus/Grafana or simpler dashboard).

## 💡 Notes for Next Session
- Work can be done directly in `~/docker`.
- Git operations should be performed from the root (`~/work/repo/macmini-home-server/`).
- Ensure `secrets.yaml` and other sensitive files are not accidentally committed.
