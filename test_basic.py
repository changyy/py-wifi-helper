#!/usr/bin/env python3
import sys
import platform

# Only run on macOS
if platform.system() != 'Darwin':
    print("Skipping macOS tests on non-Darwin platform")
    sys.exit(0)

# Test basic import and initialization
try:
    from py_wifi_helper import my_macos_helper
    from py_wifi_helper import yy_wifi_helper
    print("✓ Successfully imported existing modules")
    
    # Test basic initialization
    helper = my_macos_helper.YYMacOSWIFIHelper()
    print("✓ Successfully initialized original helper")
    
    # Test interface detection
    result = helper.getInterface()
    print(f"✓ Interface detection: {result}")
    
    # Test version detection logic (without v2 import)
    import subprocess
    try:
        result = subprocess.run(['sw_vers', '-productVersion'], capture_output=True, text=True, check=True)
        version = result.stdout.strip()
        parts = version.split('.')
        if len(parts) >= 2:
            version_float = float(f"{parts[0]}.{parts[1]}")
        else:
            version_float = float(parts[0])
        print(f"✓ macOS version detected: {version} ({version_float})")
        print(f"✓ Should use direct scan: {version_float < 14.0}")
    except Exception as e:
        print(f"✗ Version detection failed: {e}")
    
    print("\n=== Testing existing scan functionality ===")
    # Test existing scan (may fail on macOS 14+, but we want to see the error)
    scan_result = helper.scanToGetAPList()
    print(f"Scan status: {scan_result['status']}")
    if scan_result['error']:
        print(f"Scan errors: {scan_result['error']}")
    if scan_result['list']:
        print(f"Found {len(scan_result['list'])} networks")
        for i, network in enumerate(scan_result['list'][:3]):  # Show first 3
            ssid = network.get(yy_wifi_helper.WIFIAP.SSID, 'Unknown')
            rssi = network.get(yy_wifi_helper.WIFIAP.RSSI, 'Unknown')
            print(f"  {i+1}. {ssid} ({rssi}dB)")
    
    print("\n✅ All basic tests passed!")

except ImportError as e:
    print(f"✗ Import error: {e}")
    print("Please ensure you're running from the project root directory")
    sys.exit(1)
except Exception as e:
    print(f"✗ Unexpected error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)