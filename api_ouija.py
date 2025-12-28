#!/usr/bin/env python3
"""
API Version Ouija Board - When documentation is just a suggestion.
"""

import requests
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# The mystical versions to test - because who knows what actually works?
VERSIONS = ['v1', 'v2', 'v2.1', 'v3', 'v3.1', 'beta', 'latest', '']

# The sacred HTTP methods - pick your poison
METHODS = ['GET', 'POST', 'PUT', 'DELETE']

# The forbidden status codes - if you see these, run away!
BAD_CODES = {404, 500, 501, 502, 503}

def test_endpoint(base_url, endpoint, headers=None):
    """Ask the API spirits which version they prefer today."""
    results = []
    
    for version in VERSIONS:
        url = f"{base_url.rstrip('/')}/{version}/{endpoint.lstrip('/')}" if version else f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        for method in METHODS:
            try:
                # Politely knock on the API's door
                if method == 'GET':
                    resp = requests.get(url, headers=headers, timeout=5)
                elif method == 'POST':
                    resp = requests.post(url, headers=headers, timeout=5)
                elif method == 'PUT':
                    resp = requests.put(url, headers=headers, timeout=5)
                else:  # DELETE
                    resp = requests.delete(url, headers=headers, timeout=5)
                
                # Interpret the API's mystical response
                if resp.status_code not in BAD_CODES:
                    results.append({
                        'version': version or '(no version)',
                        'method': method,
                        'status': resp.status_code,
                        'url': url,
                        'success': True
                    })
                
                # Don't anger the API gods with too many requests
                time.sleep(0.1)
                
            except requests.RequestException:
                # API said "talk to the hand"
                continue
    
    return results

def main():
    """Summon the API spirits and ask them what they want."""
    if len(sys.argv) < 3:
        print("Usage: python api_ouija.py <base_url> <endpoint>")
        print("Example: python api_ouija.py https://api.example.com /users")
        sys.exit(1)
    
    base_url = sys.argv[1]
    endpoint = sys.argv[2]
    
    print(f"🔮 Consulting the API Ouija Board for {base_url}{endpoint}...")
    print("The spirits are communicating...")
    
    results = test_endpoint(base_url, endpoint)
    
    if not results:
        print("\n💀 The API is dead to us. Try sacrificing a goat.")
        return
    
    print(f"\n✨ The spirits suggest {len(results)} working combination(s):\n")
    
    for i, result in enumerate(results, 1):
        print(f"{i}. Version: {result['version']}")
        print(f"   Method: {result['method']}")
        print(f"   Status: {result['status']}")
        print(f"   URL: {result['url']}")
        print()
    
    # The final revelation
    best = min(results, key=lambda x: x['status'])
    print(f"🎯 Recommended: {best['method']} {best['url']}")
    print("May the API odds be ever in your favor!")

if __name__ == "__main__":
    main()
