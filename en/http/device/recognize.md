# Recognition Parameters

## Get device recognition parameters

When the use mode of use_mode is single-player mode, the device access parameter modes are all valid;
When the use mode of use_mode is multi-player mode, "face" and "face or card swipe" in the device access parameter mode are valid, and multi-authentication is supported;

### Request address

https://HOST:PORT/v1/device/recognize

### Request method

GET

### Request parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

### Response parameters

| Parameter name         | Type    | Description                                                  | Remark                                  |
| ---------------------- | ------- | ------------------------------------------------------------ | --------------------------------------- |
| use_mode               | Int     | use mode: 3: single-player mode  4: multi-player mode        |                                         |
| multi_auth_mode        | Boolean | Multi-authentication switch, false: off true: on             | use_mode = 4                            |
| multi_auth_timeout     | Int     | Multi-authentication interval                                |                                         |
| liveness               | Boolean | Liveness detection，false：off true：on                      |                                         |
| liveness_threshold     | Float   | Liveness threshold（Default 0.995）                          | 0 \< x \< 1 , default value: 0.995000   |
| verify_threshold       | Float   | Verification threshold（Default 0.90）                       | 0 \< x \< 1 , default value: 0.900000   |
| certificate_threshold  | Float   | Certification threshold（Default 0.6）                       | 0 \< x \< 1 , default value: 0.600000   |
| recognition_distance   | Int     | Face recognition distance (unit: meters)                     | 0.5 \< x \< 2 , default value: 2.000000 |
| open_interval          | Int     | Re-identification interval (s)                               |                                         |
| mask_detect            | Boolean | Mask detection switch， false：off；true：on                 |                                         |
| no_access_without_mask | Boolean | Whether to allow passage without a mask, false: allowed; true: not allowed |                                         |
| no_access_with_mask    | Boolean | Whether to allow passage with a mask, false: allowed; true: not allowed |                                         |

Response example

```
    {
    "code": 200,
    "msg": "OK"， 
    "data": {
        "use_mode": 3,
        "multi_auth_mode": false,
        "multi_auth_timeout": 3,
        "liveness": true,
        "liveness_threshold": 0.9950000047683716,
        "verify_threshold": 0.8999999761581421,
        "certificate_threshold": 0.6000000238418579,
        "recognition_distance": 2,
        "open_interval": 5,
        "mask_detect": false,
        "no_access_without_mask": true,
        "no_access_with_mask": false
    }
    }
```



##  Set device recognition parameters

When the use mode of use_mode is single-player mode, the device access parameter modes are all valid;
When the use mode of use_mode is multi-player mode, "face" and "face or card swipe" in the device access parameter mode are valid, and multi-authentication is supported;

### Request address

https://HOST:PORT/v1/device/recognize

### Request method

POST

### Request parameters

| Parameter name         | Type    | Description                                                  | Remark                                  |
| ---------------------- | ------- | ------------------------------------------------------------ | --------------------------------------- |
| use_mode               | Int     | use mode: 3: single-player mode  4: multi-player mode        |                                         |
| multi_auth_mode        | Boolean | Multi-authentication switch, false: off true: on             | use_mode = 4                            |
| multi_auth_timeout     | Int     | Multi-authentication interval                                |                                         |
| liveness               | Boolean | Liveness detection，false：off true：on                      |                                         |
| liveness_threshold     | Float   | Liveness threshold（Default 0.995）                          | 0 \< x \< 1 , default value: 0.995000   |
| verify_threshold       | Float   | Verification threshold（Default 0.90）                       | 0 \< x \< 1 , default value: 0.900000   |
| certificate_threshold  | Float   | Certification threshold（Default 0.6）                       | 0 \< x \< 1 , default value: 0.600000   |
| recognition_distance   | Int     | Face recognition distance (unit: meters)                     | 0.5 \< x \< 2 , default value: 2.000000 |
| open_interval          | Int     | Re-identification interval (s)                               |                                         |
| mask_detect            | Boolean | Mask detection switch， false：off；true：on                 |                                         |
| no_access_without_mask | Boolean | Whether to allow passage without a mask, false: allowed; true: not allowed |                                         |
| no_access_with_mask    | Boolean | Whether to allow passage with a mask, false: allowed; true: not allowed |                                         |

Request example

```
{
        "use_mode": 3,
        "multi_auth_mode": false,
        "multi_auth_timeout": 3,
        "liveness": true,
        "liveness_threshold": 0.9950000047683716,
        "verify_threshold": 0.8999999761581421,
        "certificate_threshold": 0.6000000238418579,
        "recognition_distance": 2,
        "open_interval": 5,
        "mask_detect": true,
        "no_access_without_mask": true,
        "no_access_with_mask": false
}
```

### Response parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

