#!/bin/bash

# Configuration
SERVICES=("adguard" "nginx" "scripts" "fail2ban")
BASE_DIR="$HOME/services"
CONF_FILE="$BASE_DIR/scripts/newsyslog.conf"

# Colors for output
GREEN='\033[0;32m'
NC='\033[0m' # No Color

function show_status() {
    echo -e "${GREEN}=== Service Log Status ===${NC}"
    for SVC in "${SERVICES[@]}"; do
        LOG_DIR="$BASE_DIR/$SVC/logs"
        if [ -d "$LOG_DIR" ]; then
            # Get total size of the log directory
            SIZE=$(du -sh "$LOG_DIR" 2>/dev/null | cut -f1)
            # Count log files (including rotated ones)
            COUNT=$(ls "$LOG_DIR" 2>/dev/null | wc -l | xargs)
            
            # Simple one-line output
            printf "%-12s : %-8s (%s files)\n" "[$SVC]" "$SIZE" "$COUNT"
        else
            printf "%-12s : %-8s\n" "[$SVC]" "N/A"
        fi
    done
}

function rotate_logs() {
    if [ "$EUID" -ne 0 ]; then
        echo -e "${GREEN}=== Log Rotation (Dry Run / Permission Check) ===${NC}"
        echo "Error: 'newsyslog' requires root privileges to execute rotation."
        echo "Please run: sudo $0 rotate"
        return 1
    fi

    echo -e "${GREEN}=== Rotating Logs using newsyslog ===${NC}"
    if [ -f "$CONF_FILE" ]; then
        # -F: force rotation, -f: specify config file, -v: verbose
        newsyslog -F -f "$CONF_FILE"
        echo "Rotation completed successfully."
        show_status
    else
        echo "Error: Configuration file not found at $CONF_FILE"
    fi
}

# Main logic
case "$1" in
    rotate)
        rotate_logs
        ;;
    *)
        show_status
        echo -e "\nTip: Run '$0 rotate' to force log rotation."
        ;;
esac
