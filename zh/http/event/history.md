# 历史通行事件查询



该接口可以通过起止时间, user_id, job_number, ic_number 等相关过滤条件获取通行记录.

## 请求路径

> `/v1/event/history`

## 请求方式

> POST

- 请求体: `application/json`

| 字段       | 类型 | 必填 | 字段释义                                                   |
| ---------- | ---- | ---- | ---------------------------------------------------------- |
| begin_time | Int  | N    | 起始时间,Unix时间戳(秒级),可为空或0                                      |
| type       | Int  | N    | 结束时间,Unix时间戳(秒级),可为空或0,若存在则须大于等于 begin_time          |
| user_id    | Int  | N    | 可为空或0,若存在则范围: 大于 0 小于 99999999 |
| job_number | String| N | 可为空 |
| ic_number | String| N | 可为空 |
| offset | Int | N | 起始偏移,默认0 |
| limit | Int | N | 单次搜索限制获取条目,默认20,最大25 |

> 注: 不支持 `user_id`,`job_number`,`ic_number`同时填值搜索;  若`user_id`,`job_number`,`ic_number`其中存在两者或三者的值,则按照此优先级取过滤条件 :  `user_id` > `job_number` > `ic_number`


## 请求示例:

获取时间段 `1669552210` [2022-11-27 20:30:10] 到 `1669742085` [2022-11-30 01:14:45] 时间段中,`job_number`为 `1111`的通行记录,且单次请求获取`3`条记录.

> `/v1/event/history`

```json
{
    "begin_time": 1669552210,
    "end_time": 1669742085,
    "job_number": "1111",
    "limit": 3
}
```

## 返回示例

其中`rgb_image`字段为base64后的图片内容.

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