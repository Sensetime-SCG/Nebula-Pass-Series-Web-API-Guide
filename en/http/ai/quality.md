# Get the quality infomation of the face in the picture

Get the quality infomation of the face in the picture

## Request address

> `/v1/ai/recognitionquality`

## Request method

> POST

- Body Type: `multipart/form-data`

| Parameter name  | Type | Required | Description                    |
| ----- | ---- | ---- | --------------------------- |
| image | File | Y    | JPEG format image,file size should be less thann 4 MB |

### Response Parameter

#### data

| Parameter name      | Type    | Description              |
| --------- | ------- | ------------------------------------------------------------ |
| rect      | Object  | Face coordinates. Note: The valid range is that the minimum value of the face up and down or left and right is not less than 100 pixel |
| yaw       | float   | posture - yaw  Note:   -20 < valid < 20                        |
| pitch     | float   | posture - pitch Note:  -20 < valid < 20                        |
| roll      | float   | posture - roll Note:   -20 < valid < 20                        |
| hasMask   | int     | 0:not wearing a mask, 2: wearing a mask; Note: The field result is currently invalid             |
| hasHelmet | boolean | whether to wear a hat; Note: The field result is currently invalid                        |
| result    | Object  | result                                                     |

#### rect

**Take the lower left corner of the picture as the starting point of the XY axis coordinates**

| Parameter name   | Type    | Description      |
| ----- | ---- | ------------------- |
| left  | int  | The distance from the left border of the face to the Y axis |
| right | int  | The distance from the right border of the face to the Y axis |
| top   | int  | The distance from the top border of the face to the X axis |
| bottom  | int  | The distance from the bottom border of the face to the X axis |

#### result

**Face quality warehousing results**

| Parameter name   | Type    | Description      |
| ----- | ---- | ------------------- |
| code | int | 0: pass<br/>80200: wear mask<br/>80201: wear hat<br/>80202: face too small<br/>80204: pitch too big<br/>80205: yaw too big<br/>80206: roll too big |
| info | string | Interpretation of the corresponding code |


## Response example

```json
{
  "data": [
    {
      "rect": {
        "left": 105,
        "top": 108,
        "right": 336,
        "bottom": 360
      },
      "yaw": -5.201200008392334,
      "pitch": 10.41426372528076,
      "roll": 0.2670194208621979,
      "hasMask": 0,
      "hasHelmet": false,
      "result": {
        "code": 0,
        "info": "PASS"
      }
    }
  ],
  "code": 200,
  "msg": "OK"
}
```