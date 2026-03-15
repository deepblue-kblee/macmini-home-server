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
1.  **Security Hardening (Current Priority):**
    - Audit existing `nginx` and `docker-compose` configurations for security vulnerabilities.
    - Implement security best practices (Headers, SSL, Fail2ban, etc.).
    - Leverage `npx skills find` to discover specialized hardening guides.
2.  **Documentation & Guide:**
    - Create a comprehensive root `README.md` with setup instructions and architecture diagram.
3.  **System Configuration (Non-Docker):**
    - Create a `scripts/` directory for automation (e.g., backup, health check).
4.  **Automation & Maintenance:**
    - Implement a backup strategy for the `data/` and `config/` folders.

## 💡 Notes for Next Session
- **Skill-based Workflow:** Always check for existing skills using `npx skills find` before implementing complex features or security measures.
- **Environment:** Global settings in `~/.gemini/settings.json` now include `~/.agents/skills/` directory.
- **Git Operations:** Perform all git commands from the project root.
- **Security:** Focus on hardening the Mac Mini home server setup.
