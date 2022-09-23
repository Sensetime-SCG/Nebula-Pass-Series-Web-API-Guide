# 获取设备基本信息

获取设备基础相关信息，诸如产品名称、产品型号、软件版本等。

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
| app_ver   | string | 应用版本     |
| api_ver   | string | Pass 设备集成API版本     |
| model_ver   | Object | 设备算法版本     |
| --hunter | string | hunter版本     |
| --august  | string | august版本     |
| --aligner   | string | aligner版本     |
| --headpose  | string | headpose版本     |
| --blur   | string | blur版本     |
| --liveness  | string | liveness版本     |
| --feature  | string | feature版本     |
| --attribute  | string | attribute 版本    |

## 请求示例

> `​/v1​/device​/info`

## 返回示例

```json
{
    "data": {
        "model": "SPSC801C0FY01",
        "device_sn": "PSC800C0MC22G00025",
        "mac_wired": "AC:1D:DF:6A:C4:AC",
        "mac_wlan": "",
        "sw_ver": "V1.1.1",
        "hw_ver": "V1",
        "app_ver": "V3.5.0(3)",
        "api_ver": "1.1.0",
        "model_ver": {
            "hunter": "KM_Detect_Hunter_SamllFace",
            "august": "KM_August",
            "aligner": "KM_Aligner",
            "headpose": "KM_Headpose",
            "blur": "KM_Blur",
            "liveness": "KM_live2i_",
            "feature": "KM_featur",
            "attribute": "KM_Attribute_Classify"
        }
    },
    "code": 200,
    "msg": "OK"
}
```