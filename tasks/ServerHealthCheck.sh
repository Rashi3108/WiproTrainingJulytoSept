#!/bin/bash
# server_health_check.sh - Complete server monitoring script

LOG_FILE="/var/log/health_check.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting server health check..." | tee -a $LOG_FILE

# Check CPU usage
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | sed 's/%us,//')
echo "CPU Usage: $CPU_USAGE%" | tee -a $LOG_FILE

# Check memory usage
MEMORY_USAGE=$(free | grep Mem | awk '{printf("%.2f%%", $3/$2 * 100.0)}')
echo "Memory Usage: $MEMORY_USAGE" | tee -a $LOG_FILE

# Check disk space
DISK_USAGE=$(df -h / | tail -1 | awk '{print $5}')
echo "Disk Usage: $DISK_USAGE" | tee -a $LOG_FILE

# Check running services
SERVICES=("nginx" "mysql" "redis")
for service in "${SERVICES[@]}"; do
    if systemctl is-active --quiet $service; then
        echo "✅ $service is running" | tee -a $LOG_FILE
    else
        echo "❌ $service is not running" | tee -a $LOG_FILE
    fi
done

echo "[$DATE] Health check completed!" | tee -a $LOG_FILE
