# py-wifi-helper

This is a Python tool/library developed for macOS 13.5 and Ubuntu 22.04, primarily providing operations for wireless interfaces. It includes functionalities such as listing available wireless interfaces, scanning for WiFi signals using a specified wireless interface, connecting a chosen wireless interface to a specific WiFi access point, retrieving information about the connected WiFi access points for the specified wireless interface, and disconnecting the specified wireless interface.

# Usage

```
% py-wifi-helper --help
usage: py-wifi-helper [-h] [--action {device,scan,connect,disconnect}] [--device DEVICE] [--ssid SSID] [--password PASSWORD]

options:
  -h, --help            show this help message and exit
  --action {device,scan,connect,disconnect}
                        command action
  --device DEVICE       interface
  --ssid SSID           ssid
  --password PASSWORD   password
```

## Ubuntu

```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.3 LTS
Release:	22.04
Codename:	jammy

$ sudo py-wifi-helper
{
    "version": "1.0.0",
    "device": {
        "default": "wlxd1234567890",
        "list": [
            "wlxd1234567890"
        ],
        "error": null,
        "select": "wlxd1234567890"
    },
    "connection": {
        "default": {
            "ssid": null,
            "log": null
        },
        "wlxd1234567890": {
            "ssid": null,
            "log": null
        }
    },
    "action": {
        "name": "device",
        "status": true,
        "error": null,
        "log": null
    }
}
```

## macOS

```
% sw_vers
ProductName:		macOS
ProductVersion:		13.5
BuildVersion:		22G74

% py-wifi-helper
{
    "version": "1.0.0",
    "device": {
        "default": "en0",
        "list": [
            "en0"
        ],
        "error": null,
        "select": "en0"
    },
    "connection": {
        "default": {
            "ssid": "MyHomeWIFIAP",
            "log": null
        },
        "en0": {
            "ssid": "MyHomeWIFIAP",
            "log": null
        }
    },
    "action": {
        "name": "device",
        "status": true,
        "error": null,
        "log": null
    }
}
```


### macos - Scan

```
% py-wifi-helper --action scan
{
    "version": "1.0.0",
    "device": {
        "default": "en0",
        "list": [
            "en0"
        ],
        "error": null,
        "select": "en0"
    },
    "connection": {
        "default": {
            "ssid": "MyHomeWIFIAP",
            "log": null
        },
        "en0": {
            "ssid": "MyHomeWIFIAP",
            "log": null
        }
    },
    "action": {
        "name": "scan",
        "status": true,
        "error": null,
        "log": null
    },
    "ssid": [
        "SSID01",
        "SSID02",
        "SSID03",
        "SSID04",
        "SSID05",
        "SSID06",
        "SSID07",
        "SSID08"
    ]
}
```

### macOS - Scan with DeviceID `xxxx` (not found):

```
% py-wifi-helper --action scan --device xxxx
{
    "version": "1.0.0",
    "device": {
        "default": "en0",
        "list": [
            "en0"
        ],
        "error": null,
        "select": "xxxx"
    },
    "connection": {
        "default": {
            "ssid": null,
            "log": null
        },
        "en0": {
            "ssid": "MyHomeWIFIAP",
            "log": null
        }
    },
    "action": {
        "name": "scan",
        "status": false,
        "error": [
            "interface not found: xxxx, current: ['en0']"
        ],
        "log": null
    },
    "ssid": []
}
```

---

### macOS - disconnect

```
% py-wifi-helper --action disconnect --device en0
{
    "version": "1.0.0",
    "device": {
        "default": "en0",
        "list": [
            "en0"
        ],
        "error": null,
        "select": "en0"
    },
    "connection": {
        "default": {
            "ssid": null,
            "log": null
        },
        "en0": {
            "ssid": null,
            "log": null
        }
    },
    "action": {
        "name": "disconnect",
        "status": true,
        "error": null,
        "log": null
    }
}
```

---

### macOS - Connect

```
% py-wifi-helper --action connect --device en0 --ssid MyHomeWIFIAP --password 12345678
{
    "version": "1.0.0",
    "device": {
        "default": "en0",
        "list": [
            "en0"
        ],
        "error": null,
        "select": "en0"
    },
    "connection": {
        "default": {
            "ssid": "MyHomeWIFIAP",
            "log": null
        },
        "en0": {
            "ssid": "MyHomeWIFIAP",
            "log": null
        }
    },
    "action": {
        "name": "connect",
        "status": true,
        "error": null,
        "log": null
    }
}
```
