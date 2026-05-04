# Mac Mini Home Server Project Context

## 📌 Project Overview
- **Root Directory:** `~/work/repo/macmini-home-server/`
- **Structure:** Monorepo (Docker services + System configs/scripts)
- **Primary Access Path:** `~/docker` (Symlinked to `./docker`)
- **Reference Docs:** `source-docs/` (Symlinked to Google Drive project folder)
  - *💡 Hint:* This folder contains documents created and updated by AI Agents (e.g., Gemini). Use these to understand previous collaboration history and design decisions.
- **Remote Repo:** [https://github.com/deepblue-kblee/macmini-home-server](https://github.com/deepblue-kblee/macmini-home-server)

## ✅ Completed Tasks
1.  **Repository Setup:** Root-based monorepo structure with Git & GitHub integration.
2.  **Service Migration:** All Docker services (AdGuard, Home Assistant, etc.) moved to `docker/apps/`.
3.  **Knowledge Integration:** Created `source-docs/` symlink to reference external Google Drive planning documents.

## 🚀 Execution Plan (Next Steps)
1.  **Security Hardening (Current Priority):**
    - Audit `nginx` and `docker-compose` configs for security vulnerabilities.
    - Reference `source-docs/` for original setup logic and agent work logs.
    - Implement security best practices (Headers, SSL, Fail2ban, etc.).
    - Leverage `npx skills find` to discover specialized hardening guides.
2.  **Documentation & Guide:**
    - Create a comprehensive root `README.md` based on `source-docs/` content.
    - Do not read `source-docs/`. This is only for human(User).
    - Refer to docs/*.
3.  **System Configuration (Non-Docker):**
    - Create a `scripts/` directory for automation.

## 💡 Notes for Next Session
- **Knowledge Base:** Use docs/references/*.md to understand the original intent and past implementation steps.
- **Skill-based Workflow:** Use `npx skills find` for complex/security tasks.
- **Environment:** Global settings in `~/.gemini/settings.json` now include `~/.agents/skills/`.

