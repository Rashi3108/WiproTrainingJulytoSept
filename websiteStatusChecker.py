#!/usr/bin/env python3
"""
Exercise 1: Website Status Checker
Cross-platform website monitoring tool
"""

import requests
import time
import platform
from datetime import datetime

# List of websites to monitor
websites = [
    {"name": "Google", "url": "https://www.google.com"},
    {"name": "GitHub", "url": "https://github.com"},
    {"name": "Stack Overflow", "url": "https://stackoverflow.com"},
    {"name": "Python.org", "url": "https://www.python.org"},
    {"name": "AWS", "url": "https://aws.amazon.com"}
]

def check_website(site_info, timeout=10):
    """Check website accessibility and measure response time"""
    try:
        print(f"🔍 Checking {site_info['name']}...")
        
        start_time = time.time()
        response = requests.get(site_info['url'], timeout=timeout)
        response_time = round((time.time() - start_time) * 1000, 2)
        
        if response.status_code == 200:
            print(f"✅ {site_info['name']} - OK ({response_time}ms)")
            return {
                'status': 'UP',
                'response_time': response_time,
                'status_code': response.status_code
            }
        else:
            print(f"⚠️  {site_info['name']} - Status: {response.status_code}")
            return {
                'status': 'WARNING',
                'response_time': response_time,
                'status_code': response.status_code
            }
            
    except requests.exceptions.Timeout:
        print(f"⏰ {site_info['name']} - Request timeout")
        return {'status': 'TIMEOUT', 'response_time': timeout * 1000}
        
    except requests.exceptions.ConnectionError:
        print(f"🔌 {site_info['name']} - Connection failed")
        return {'status': 'DOWN', 'response_time': 0}
        
    except Exception as e:
        print(f"❌ {site_info['name']} - Error: {str(e)}")
        return {'status': 'ERROR', 'response_time': 0}

def main():
    """Main monitoring function"""
    print("🌐 WEBSITE STATUS CHECKER")
    print("=" * 40)
    print(f"🖥️  Platform: {platform.system()}")
    print(f"⏰ Check time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    results = []
    for site in websites:
        result = check_website(site)
        results.append({'name': site['name'], 'result': result})
        print()
        time.sleep(0.5)
    
    # Summary
    up_sites = len([r for r in results if r['result']['status'] == 'UP'])
    print(f"📊 Summary: {up_sites}/{len(results)} sites are UP")

if __name__ == "__main__":
    main()
