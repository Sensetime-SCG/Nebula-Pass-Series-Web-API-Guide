# 获取设备基本信息

RT

## 请求路径

> `​/v1​/device​/info`

## 请求方式

> GET

### 响应参数

| 字段      | 类型   | 字段释义        |
| --------- | ------ | ----------- |
| model     | string | 产品型号    |
| device_sn | string | 设备序列号  |
| mac_wired | string | 有线Mac地址 |
| mac_wlan  | string | 无线Mac地址 |
| sw_ver    | string | ROM版本     |
| hw_ver    | string | 硬件版本    |
| api_ver   | string | API版本     |

## 请求示例

> `​/v1​/device​/info`

## 返回示例

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