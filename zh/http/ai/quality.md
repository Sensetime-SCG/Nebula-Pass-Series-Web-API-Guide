# 获取图片中人脸质量
获取图片中人脸质量信息

## 请求路径

> `/v1/ai/recognitionquality`

## 请求方式

> POST

- 请求体: `multipart/form-data`

| 字段  | 类型 | 必填 | 字段释义                    |
| ----- | ---- | ---- | --------------------------- |
| image | File | Y    | JPEG 图像,文件不可大于 4 MB |

### 响应参数

#### data

| 字段      | 类型    | 字段释义                                                     |
| --------- | ------- | ------------------------------------------------------------ |
| rect      | Object  | 脸部坐标 注: 有效范围是 面部上下或左右的最小值不低于 100 pixel |
| yaw       | float   | 姿态-偏航角 注:   -20 < 有效范围 < 20                        |
| pitch     | float   | 姿态-俯仰角 注:   -20 < 有效范围 < 20                        |
| roll      | float   | 姿态-横滚角 注:   -20 < 有效范围 < 20                        |
| hasMask   | int     | 0:未戴口罩, 2: 已戴口罩 注意: 该字段结果目前无效             |
| hasHelmet | boolean | 是否佩戴帽子 注意: 该字段结果目前无效                        |
| result    | Object  | 判断结果                                                     |

#### rect

**以图片的左下角为XY轴坐标起点**

| 字段  | 类型 | 字段释义            |
| ----- | ---- | ------------------- |
| left  | int  | 人脸左边框到Y轴距离 |
| right | int  | 人脸右边框到Y轴距离 |
| top   | int  | 人脸上边框到X轴距离 |
| bottom  | int  | 人脸下边框到X轴距离 |

#### result

**人脸质量入库结果**

| 字段  | 类型 | 字段释义            |
| ----- | ---- | ------------------- |
| code | int | 0: 通过<br/>80200: 佩戴口罩<br/>80201: 佩戴帽子<br/>80202: 面部像素过少<br/>80204: pitch过大<br/>80205: yaw过大<br/>80206: roll过大 |
| info | string | 对应 code 的释义 |


## 返回示例

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