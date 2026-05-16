#!/bin/bash

# Configuration
BASE_DIR="$HOME/services/scripts"
PYTHON_BIN="$BASE_DIR/venv/bin/python3"
SCRIPT_PATH="$BASE_DIR/health_check.py"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}=== System Health Check ===${NC}"

if [ ! -f "$PYTHON_BIN" ]; then
    # Fallback to system python if venv is not ready
    PYTHON_BIN="python3"
fi

if [ -f "$SCRIPT_PATH" ]; then
    $PYTHON_BIN "$SCRIPT_PATH" | while read -r line; do
        if [[ $line == *"FAILED"* ]]; then
            echo -e "${RED}$line${NC}"
        else
            echo -e "$line"
        fi
    done
else
    echo -e "${RED}Error: Health check script not found at $SCRIPT_PATH${NC}"
    exit 1
fi
