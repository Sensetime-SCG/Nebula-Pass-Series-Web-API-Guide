# Function Parameters

##  Get device function parameters

Get device function parameters.

### Request address

https://HOST:PORT/v1/device/functions

### Request method

GET

### Request parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

### Response parameters

| Parameter name  | Type    | Description                                                  | Remark |
| --------------- | ------- | ------------------------------------------------------------ | ------ |
| device_run_type | Int     | Device running status configuration, 1: running; 2: shutdown |        |
| mode            | Int     | Verification mode: 0: swipe face 1: swipe face or card 2: swipe face or card or swipe QR code 3: swipe face and swipe card 4: swipe ID card 5: swipe face or swipe ID card 6: swipe face and swipe ID card |        |
| strong_hint     | Boolean | Strong hint mode switch, false: off; true: on                |        |
| avatar_status   | Int     | Show avatar 0: Don't show avatar 1: Show avatar 2. Show personalized avatar |        |
| name_status     | Int     | Show name: 0: No name show 1: Show name 2: Show encrypted name |        |
| record          | Boolean | Event record storage switch, false: off; true: on            |        |
| record_image    | Boolean | Event record picture storage switch, false: off; true: on    |        |
| alarm_record    | Boolean | Alarm record storage switch, false: off; true: on            |        |
| auth_mode       | Int     | Authentication type: 0: local authentication 1: local authentication + remote door opening |        |

Response example

```
{

  "code": 200,

  "msg": "OK"，
  
  "data": {

​    "device_run_type": 1,

​    "mode": 0,

​    "strong_hint": **true**,

​    "avatar_status": 1,

​    "name_status": 1,

​    "record": **true**,

​    "record_image": **true**,

​    "alarm_record": **true**,

​    "auth_mode": 0

  }

}
```



## Set device function parameters

Set device function parameters

### Request address

https://HOST:PORT/v1/device/functions

### Request method

POST

### Request parameters

| Parameter name  | Type    | Description                                                  | Remark |
| --------------- | ------- | ------------------------------------------------------------ | ------ |
| device_run_type | Int     | Device running status configuration, 1: running; 2: shutdown |        |
| mode            | Int     | Verification mode: 0: swipe face 1: swipe face or card 2: swipe face or card or swipe QR code 3: swipe face and swipe card 4: swipe ID card 5: swipe face or swipe ID card 6: swipe face and swipe ID card |        |
| strong_hint     | Boolean | Strong hint mode switch, false: off; true: on                |        |
| avatar_status   | Int     | Show avatar 0: Don't show avatar 1: Show avatar 2. Show personalized avatar |        |
| name_status     | Int     | Show name: 0: No name show 1: Show name 2: Show encrypted name |        |
| record          | Boolean | Event record storage switch, false: off; true: on            |        |
| record_image    | Boolean | Event record picture storage switch, false: off; true: on    |        |
| alarm_record    | Boolean | Alarm record storage switch, false: off; true: on            |        |
| auth_mode       | Int     | Authentication type: 0: local authentication 1: local authentication + remote door opening |        |

Request example

```
{
        "device_run_type": 1,
        "mode": 0,
        "strong_hint": true,
        "avatar_status": 1,
        "name_status": 1,
        "record": true,
        "record_image": true,
        "alarm_record": true,
        "auth_mode": 0
    }
```

### Response parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

