# 🔒 Fail2Ban Host Process Management

## 📂 Directory Structure
```text
/opt/homebrew/etc/fail2ban/
├── jail.local (symlink)     # Custom jail configurations
└── filter.d/ (symlink)      # Custom filters
```

## ⚙️ Configuration
- **Central Config**: `~/work/repo/macmini-home-server/host/fail2ban/`
- **Native Path**: `/opt/homebrew/etc/fail2ban/`
- **Log Monitor**: Watching `~/services/nginx/logs/*.log`

## 🛠 Commands
- **Check Status**: `sudo fail2ban-client status`
- **Check Specific Jail**: `sudo fail2ban-client status nginx-http-auth`
- **Restart Service**: `sudo brew services restart fail2ban`
- **View Logs**: `tail -f /opt/homebrew/var/log/fail2ban.log`
