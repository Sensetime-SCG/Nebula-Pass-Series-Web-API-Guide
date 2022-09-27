# 设备识别参数
use_mode使用模式为单人模式时，设备功能参数 mode中都有效；  
use_mode使用模式为多人模式时，设备功能参数 mode中的“人脸”、“人脸或刷卡”有效，同时支持多重认证；

## 提交配置

### 请求路径

> `​/v1​/device​/recognize`

### 请求方式

> POST

- 请求体: `application/json`

注意，字段`Float`类型由于为浮点型，在转换时会存在精度偏差，其偏差值小于*0.000001*

| 字段                   | 类型    | 必填 | 字段释义                                    |
| ---------------------- | ------- | ---- | ------------------------------------------- |
| use_mode               | Int     | Y    | 使用模式, 3:单人模式，4:多人模式; 默认:3        |
| multi_auth_mode        | Boolean | N    | 多重认证开关，false:关，true:开; 默认:false            |
| multi_auth_timeout     | Int     | N    | 多重认证间隔(s); 默认:3                             |
| liveness               | Boolean | Y    | 活体检测，false:关，true:开; 默认:true                 |
| liveness_threshold     | Float   | Y   | 活体检测阈值,范围: 0 < x < 1; 默认:0.995 |
| verify_threshold       | Float   | Y    | 活体检测阈值,范围: 0 < x < 1; 默认:0.90    |
| certificate_threshold  | Float   | Y    | 认证对比阈值,范围: 0 < x < 1; 默认:0.6     |
| recognition_distance   | Int     | Y    | 人脸识别距离,单位：米,范围: 0.5 < x < 2; 默认:2  |
| open_interval          | Int     | Y    | 同一个人员再次识别间隔(s); 默认: 5                             |
| mask_detect            | Boolean | Y    | 人员口罩检测开关, false：关；true：开          |
| no_access_without_mask | Boolean | N    | 人员未带口罩不允许通行开关，false：关；true：开;为true时,mask_detect 须为 true，且 no_access_with_mask 为 false |
| no_access_with_mask    | Boolean | N    | 人员带口罩不允许通行开关，false：关；true：开;为true时,mask_detect 须为 true，且 no_access_without_mask 为 false   |

### 请求示例:

> `​/v1​/device​/recognize`

```json
{
    "use_mode": 3,
    "multi_auth_mode": false,
    "multi_auth_timeout": 3,
    "liveness": true,
    "liveness_threshold": 0.98,
    "verify_threshold": 0.90,
    "certificate_threshold": 0.60,
    "recognition_distance": 2,
    "open_interval": 5,
    "mask_detect": true,
    "no_access_without_mask": false,
    "no_access_with_mask": false
}
```
### 返回示例

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```

## 获取配置

### 请求路径

> `​/v1​/device​/recognize`

### 请求方式

> GET

### 请求示例

> `​/v1​/device​/recognize`

### 返回示例

```json
{
    "data": {
        "use_mode": 3,
        "multi_auth_mode": false,
        "multi_auth_timeout": 3,
        "liveness": true,
        "liveness_threshold": 0.9800000190734863,
        "verify_threshold": 0.8999999761581421,
        "certificate_threshold": 0.6000000238418579,
        "recognition_distance": 2,
        "open_interval": 5,
        "mask_detect": false,
        "no_access_without_mask": true,
        "no_access_with_mask": false
    },
    "code": 200,
    "msg": "OK"
}
```

