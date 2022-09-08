# Time Parameters

##  Get device time

Get device time.

### Request address

https://HOST:PORT/v1/device/time

### Request method

GET

### Request parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

### Response parameters

| Parameter name | Type    | Description                                                  | Remark                                                       |
| -------------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| local_time     | String  | Local time, unix timestamp (ms), 13 bits                     |                                                              |
| manual_mode    | Boolean | Whether to manually set the time false: get the time automatically true: manually modify the time | Default false; non-manual mode is automatically configured through ntp |
| time_zone      | String  | Device timezone, {-11, 12}                                   | Default 8                                                    |
| server_address | String  | ntp server address                                           | Need to specify http or https                                |

Response example：

```
{

  "code": 200,

  "msg": "OK"，
  
  "data": {

​    "local_time": 1660038271259,

​    "manual_mode": **false**,

​    "time_zone": 8,

​    "server_address": "https://link.bi.sensetime.com/sl"

  },

}
```



##  Set device time

Set device time.

### Request address

https://HOST:PORT/v1/device/time

### Request method

POST

### Request parameters

| Parameter name | Type    | Description                                                  | Remark                                                       |
| -------------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| local_time     | String  | Local time, unix timestamp (ms), 13 bits                     |                                                              |
| manual_mode    | Boolean | Whether to manually set the time false: get the time automatically true: manually modify the time | Default false; non-manual mode is automatically configured through ntp |
| time_zone      | String  | Device timezone, {-11, 12}                                   | Default 8                                                    |
| server_address | String  | ntp server address                                           | Need to specify http or https                                |

Request example

```
{
        "local_time": 1660038297736,
        "manual_mode": false,
        "time_zone": 8,
        "server_address": "https://link.bi.sensetime.com/sl"
    }
```

### Response parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

