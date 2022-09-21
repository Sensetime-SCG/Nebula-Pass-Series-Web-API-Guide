# Time Parameters

##  Set device time

Set device time.

### Request address

> `​/v1​/device​/time`

### Request method

> POST

- Body Type: `application/json`


### Request parameters

| Parameter name | Type    | Description                                                  |
| -------------- | ------- | ------------------------------------------------------------ |
| local_time     | String  | Local time, unix timestamp (ms), 13 bits                     |
| manual_mode    | Boolean | Whether to manually set the time false: get the time automatically true: manually modify the time | Default false; non-manual mode is automatically configured through ntp |
| time_zone      | String  | Device timezone, {-11, 12} ,Default 8     |
| server_address | String  | ntp server address , Need to specify http or https                                          |

### Request example

```json
{
    "local_time": 1660038297736,
    "manual_mode": false,
    "time_zone": 8,
    "server_address": "https://link.bi.sensetime.com/sl"
}
```

### Response example

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```
--- 


##  Get device time

Get device time.

### Request address

> `​/v1​/device​/time`

### Request method

> GET

### Response example

```json
{
    "data": {
        "local_time": 1660310557866,
        "manual_mode": false,
        "time_zone": 8,
        "server_address": "ntp.aliyun.com"
    },
    "code": 200,
    "msg": "OK"
}
```