# Record History Search

This API can search record history 

This API can be accessed by begin and ending time, user_ id, job_ number, ic_number and other relevant filtering conditions to obtain the traffic record

## Request address

> `/v1/event/history`

## Request method

> POST

- Body Type:  `application/json`

| Parameter   name    | Type   | Required | Description                                                     |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| begin_time | Int    | N    | begin time,Unix timestamp(second)                          |
| type       | Int    | N    | end time,Unix timestamp(second) |
| user_id    | Int    | N    | Range:  0 ~ 99999999                 |
| job_number | String | N    |                                                        
| ic_number  | String | N    |                                                        |
| offset     | Int    | N    | Default: 0                                               |
| limit      | Int    | N    | Default: 20, Upper limit: 25         |

> Note:  Not support  `user_id`,`job_number`,`ic_number` both exist;  if not, there are priority :  `user_id` > `job_number` > `ic_number`


### Response example

The value of `rgb_image` is the image content after base64 .

```json
{
    "data": {
        "offset": 0,
        "limit": 3,
        "count": 3,
        "total": 8,
        "items": [
            {
                "recognitionType": 1,
                "deviceSN": "PS71HD01MC22C00114",
                "recognizeScore": 0.9225929379463196,
                "mask": 0,
                "rgb_image": "xxxxxxxx",
                "pass": true,
                "mode": 9,
                "user": {
                    "name": "aa",
                    "user_id": 3,
                    "type": 1,
                    "ic_number": "2222",
                    "job_number": "1111"
                },
                "timestamp": 1669552219
            },
            {
                "recognitionType": 1,
                "deviceSN": "PS71HD01MC22C00114",
                "recognizeScore": 0.9295129179954529,
                "mask": 0,
                "rgb_image": "xxxxxxxx",
                "pass": true,
                "mode": 9,
                "user": {
                    "name": "aa",
                    "user_id": 3,
                    "type": 1,
                    "ic_number": "2222",
                    "job_number": "1111"
                },
                "timestamp": 1669690700
            },
            {
                "recognitionType": 1,
                "deviceSN": "PS71HD01MC22C00114",
                "recognizeScore": 0.9219599366188049,
                "mask": 0,
                "rgb_image": "xxxxxxxx",
                "pass": true,
                "mode": 9,
                "user": {
                    "name": "aa",
                    "user_id": 3,
                    "type": 1,
                    "ic_number": "2222",
                    "job_number": "1111"
                },
                "timestamp": 1669690852
            }
        ]
    },
    "code": 200,
    "msg": "OK"
}
```