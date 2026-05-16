# ☁️ Cloudflare DDNS Management

## 📂 Directory Structure
```text
~/services/scripts/
├── cloudflare_ddns.py (link) # Python script
└── README_DDNS.md (link)     # This file
```

## ⚙️ Configuration
- **Script Source**: `~/work/repo/macmini-home-server/host/scripts/cloudflare_ddns.py`
- **Interval**: 5 minutes (via launchd)
- **Domains**: `deepblue.im`, `*.deepblue.im`

## 🛠 Commands
- **Manual Execution**: `python3 ~/services/scripts/cloudflare_ddns.py`
- **Restart Agent**:
  ```bash
  launchctl unload ~/Library/LaunchAgents/im.deepblue.cloudflare-ddns.plist
  launchctl load -w ~/Library/LaunchAgents/im.deepblue.cloudflare-ddns.plist
  ```
- **View Logs**: `tail -f ~/services/scripts/logs/ddns_out.log`
