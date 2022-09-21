# Get device information

Obtain basic information about the device, such as product name, product model, software version, etc.

## Request address

> `​/v1​/device​/info`

## Request method

> GET

## Response parameters

| Parameter name | Type   | Description          |
| -------------- | ------ | -------------------- |
| model          | string | Product model        |
| device_sn      | string | Device SN            |
| mac_wired      | string | Wired mac address    |
| mac_wlan       | string | Wireless mac address |
| sw_ver         | string | ROM version          |
| hw_ver         | string | Hardware version     |
| app_ver        | string | APP version          |

## Response example

```json
{
    "data": {
        "model": "SPS31HD12",
        "device_sn": "xxxx",
        "mac_wired": "11:11:11:11:11:11",
        "mac_wlan": "",
        "sw_ver": "V3.0.10",
        "hw_ver": "PassCV1",
        "app_ver": "v3.0(122)"
    },
    "code": 200,
    "msg": "OK"
}
```



