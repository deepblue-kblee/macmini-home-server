# 🛡️ AdGuard Home Host Process Management

## 📂 Directory Structure
```text
~/services/adguard/
├── AdGuardHome              # Execution Binary
├── AdGuardHome.yaml (link)  # Main configuration
├── data/                    # Stats, Filters, and Sessions (DB)
└── logs/                    # Service logs
```

## ⚙️ Configuration
- **Central Config**: `~/work/repo/macmini-home-server/host/adguard/AdGuardHome.yaml`
- **Live Path**: `~/services/adguard/`
- **Admin UI**: `http://localhost:13080` (or your server IP)

## 🛠 Commands
- **Restart Service**: 
  ```bash
  sudo launchctl unload /Library/LaunchDaemons/im.deepblue.adguardhome.plist
  sudo launchctl load -w /Library/LaunchDaemons/im.deepblue.adguardhome.plist
  ```
- **View Logs**: `tail -f ~/services/adguard/logs/adguard_out.log`
