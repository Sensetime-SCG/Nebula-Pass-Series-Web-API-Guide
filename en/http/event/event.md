# Event Subscription( WebSockets)

该接口为 Websocket 接口，由 GET 请求方式升级为 Websocket。

## Receiving address

> `wss://HOST:PORT/v1/event/`

## Receiving method

> Websockets application/json

## Respond structure

| Parameter name | Type   | Description                                                  |
| -------------- | ------ | ------------------------------------------------------------ |
| **type**       | int    | Event type, currently only including 0, indicating the recognition event |
| **data**       | Object | Other information                                            |

## Receiving example

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

## Recognition event parameter description

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



