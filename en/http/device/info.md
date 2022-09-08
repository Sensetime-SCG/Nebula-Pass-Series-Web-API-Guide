# Get device information

Obtain basic information about the device, such as product name, product model, software version, etc.

## Request address

> `​/v1​/device​/info`

## Request method

GET

## Request parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

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
|                |        |                      |

Response example：

```
{

"code": 200,

"msg": "OK",

"data": {
        "model": "SPSC700C0HD01",
        "device_sn": "PS71HD01MC22C00014",
        "mac_wired": "AC:1D:DF:6A:9F:D5",
        "mac_wlan": "",
        "sw_ver": "V1.0.6",
        "hw_ver": "V1",
        "app_ver": "v3.4(122)"
}

}
```



