#!/usr/bin/env python3
"""
Exercise 2: System Information Script
Cross-platform system monitoring tool
"""

import os
import platform
import shutil
from datetime import datetime
from pathlib import Path

def get_system_info():
    """Get basic system information"""
    system = platform.system()
    if system == "Darwin":
        os_name = "macOS"
    elif system == "Windows":
        os_name = "Windows"
    elif system == "Linux":
        os_name = "Linux"
    else:
        os_name = system
    
    return {
        'os': os_name,
        'version': platform.release(),
        'architecture': platform.architecture()[0],
        'hostname': platform.node(),
        'python_version': platform.python_version()
    }

def get_disk_usage():
    """Get disk usage information"""
    try:
        if platform.system() == "Windows":
            # Windows - check C: drive
            total, used, free = shutil.disk_usage("C:\\")
        else:
            # Unix-like systems - check root
            total, used, free = shutil.disk_usage("/")
        
        # Convert to GB
        total_gb = round(total / (1024**3), 2)
        used_gb = round(used / (1024**3), 2)
        free_gb = round(free / (1024**3), 2)
        usage_percent = round((used / total) * 100, 1)
        
        return {
            'total': total_gb,
            'used': used_gb,
            'free': free_gb,
            'percentage': usage_percent
        }
    except Exception as e:
        return {'error': str(e)}

def main():
    """Main function"""
    print("🖥️  SYSTEM INFORMATION DASHBOARD")
    print("=" * 50)
    
    # System info
    sys_info = get_system_info()
    print(f"🏷️  Hostname: {sys_info['hostname']}")
    print(f"🖥️  Operating System: {sys_info['os']} {sys_info['version']}")
    print(f"🏗️  Architecture: {sys_info['architecture']}")
    print(f"🐍 Python Version: {sys_info['python_version']}")
    print(f"⏰ Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Disk usage
    print(f"\n💿 DISK USAGE:")
    disk_info = get_disk_usage()
    if 'error' not in disk_info:
        print(f"📊 Total Space: {disk_info['total']} GB")
        print(f"💿 Used Space: {disk_info['used']} GB ({disk_info['percentage']}%)")
        print(f"📀 Free Space: {disk_info['free']} GB")
        
        if disk_info['percentage'] > 80:
            print("🚨 WARNING: Disk usage is high!")
    else:
        print(f"❌ Error getting disk info: {disk_info['error']}")
    
    print(f"\n✅ System check completed!")

if __name__ == "__main__":
    main()
