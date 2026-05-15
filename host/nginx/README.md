# 🌐 Nginx Host Process Management

## 📂 Directory Structure
```text
~/services/nginx/
├── nginx.conf (symlink)     # Main configuration
├── servers/ (symlink)       # Virtual Host configs (*.conf)
├── common/ (symlink)        # Shared SSL/Security params
├── html (symlink)           # Web root -> /opt/homebrew/var/www
├── certs/                   # SSL Certificates (Let's Encrypt)
├── logs/                    # Access and Error logs
└── temp/                    # PID and temporary files
```

## ⚙️ Configuration
- **Central Config**: `~/work/repo/macmini-home-server/host/nginx/`
- **Live Path**: `~/services/nginx/`
- **Web Root**: `/opt/homebrew/var/www` (Nginx `nobody` worker access enabled)

## 🛠 Commands
- **Check Config**: `sudo nginx -t -c ~/services/nginx/nginx.conf`
- **Reload Config**: `sudo nginx -s reload -c ~/services/nginx/nginx.conf`
- **Restart Service**: 
  ```bash
  sudo launchctl unload /Library/LaunchDaemons/im.deepblue.nginx.plist
  sudo launchctl load -w /Library/LaunchDaemons/im.deepblue.nginx.plist
  ```
- **View Logs**: `tail -f ~/services/nginx/logs/access.log`
