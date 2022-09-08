# Third-party server push configuration

## Get third-party server push configuration
Get the push configuration of the third-party server, such as the address of the third-party service, whether to enable the push function.

### Request address

https://HOST:PORT/v1/event/subscribe

### Request method

GET

### Request parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

### Response parameters

| Parameter name | Type    | Description                                                  |
| -------------- | ------- | ------------------------------------------------------------ |
| event_dest     | string  | The address of the specified event receiving, using restful callback mode, supports http and https, the style is as follows: http://ip:port/eventRcv or https://ip:port/eventRcv<br/>The length is no more than 1024 bytes, the event receiving address is provided by the application side according to the specified specification, and the event receiving interface does not require authentication |
| enabled        | boolean | Whether to enable                                            |

Response example：

```
{

"code": 200,

"msg": "OK",

"data": {

}

}
```





## Set third-party server push configuration


Set the third-party server push configuration, such as the third-party service address, whether to enable the push function.

### Request address

https://HOST:PORT/v1/event/subscribe

### Request method

POST

### Request parameters

| Parameter name | Type    | Required | Description                                                  |
| -------------- | ------- | -------- | ------------------------------------------------------------ |
| event_dest     | string  | Y        | The address of the specified event receiving, using restful callback mode, supports http and https, the style is as follows: http://ip:port/eventRcv or https://ip:port/eventRcv<br/>The length is no more than 1024 bytes, the event receiving address is provided by the application side according to the specified specification, and the event receiving interface does not require authentication |
| enabled        | boolean | N        | Whether to enable                                            |

Request example:

```
{
    "event_dest" : "http://ip:port/eventRcv",
    "enabled" :true
}
```

### Response parameters

| Parameter name | Type | Description |
| -------------- | ---- | ----------- |
| None           | None | None        |

Response example：

```
{

"code": 200,

"msg": "OK",

"data": {

}

}
```





## Event Push Protocol（HTTP/HTTPS）

### Receiving method

POST application/json

### Respond structure

| **Parameter name** | **Type** | **Required** | **Description**                                              |
| ------------------ | -------- | ------------ | ------------------------------------------------------------ |
| **code**           | int      | Y            | Return code, 200 means success, other means failure          |
| **message**        | string   | Y            | Return information - record the description information of the interface implementation, success means successful description, other means failure |
| **data**           | Object   | Y            | Other information                                            |
| pass               | boolean  | Y            | Whether to open the door                                     |
| customtips         | string   | N            | The text of the interface prompt (recommended content 0-10 characters) |

### Response example

```
{

"code": 200,

"msg": "success",

"data": {
	"pass": true,
	"customtips":"Hello World"
}
}  
```

### Event push example

| **Parameter name** | **Type** | **Required** | **Description**                                              |
| ------------------ | -------- | ------------ | ------------------------------------------------------------ |
| **type**           | int      | Y            | Event type, currently only including 0, indicating the recognition event |
| **data**           | object   | Y            | Event object                                                 |

Recognition record

```
{
    "type": 0,
    "data": {
        "recognizeStatus": 2,
        "deviceSN":"PS71HD01MC22C00014",
        "recognizeScore": 0.9837480783462524,
        "livenessScore": 0.9073520302772522,
        "mask": 1,
        "rgb_image": "xxxxxxxxxxxxxx=",
        "pass": true,
        "mode": 0,
        "user": {
            "name": "Q",
            "user_id": 1,
            "type": 1
        },
        "timestamp": 1660625866
    }
}

```

###  Record event field attributes

| Parameter name  | Type    | Description                                                  |
| --------------- | ------- | ------------------------------------------------------------ |
| deviceSN        | string  | Device SN                                                    |
| recognizeStatus | int     | Classification of faces in the current screen: 0: Unknown 1: Non-liveness 2: People in the library 3: Strangers 4: Recognized 5: Authentication passed 6: Authentication failed |
| recognizeScore  | float   | Recognition score                                            |
| livenessScore   | float   | Liveness score                                               |
| mask            | int     | Whether to wear a mask: 0 not enabled 1 not worn 2 worn      |
| mode            | int     | Verification mode: 0: swipe face 1: swipe face or card 2: swipe face or card or swipe QR code 3: swipe face and swipe card 4: swipe ID card 5: swipe face or swipe ID card 6: swipe face and swipe ID card |
| **rgb_image**   | string  | Snapshot image of face in jpeg format after Base64           |
| pass            | Boolean | Whether to allow pass                                        |
| timestamp       | Int     | Recognition time                                             |
| user            | object  | User object                                                  |
| --name          | string  | User name                                                    |
| --user_id       | int     | User id                                                      |
| --type          | int     | User type                                                    |

