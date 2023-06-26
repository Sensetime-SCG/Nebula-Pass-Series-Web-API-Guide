# 历史通行事件查询



该接口可以通过起止时间, user_id, job_number, ic_number 等相关过滤条件获取通行记录.

## 请求路径

> `/v1/event/records`

## 请求方式

> POST

- 请求体: `application/json`

| 字段       | 类型 | 必填 | 字段释义                                                   |
| ---------- | ---- | ---- | ---------------------------------------------------------- |
| begin_time | Int  | N    | 起始时间,Unix时间戳(秒级),可为空或0                                      |
| end_time       | Int  | N    | 结束时间,Unix时间戳(秒级),可为空或0,若存在则须大于等于 begin_time          |
| user_id    | String | N    | 可为空 |
| job_number | String| N | 可为空 |
| ic_number | String| N | 可为空 |
| offset | Int | N | 起始偏移,默认0 |
| limit | Int | N | 单次搜索限制获取条目,默认100,最大200 |
| sort | Int | N | 排序方式，0：asc正序:；1：desc倒序, 默认:0：正序 |

> 注: 不支持 `user_id`,`job_number`,`ic_number`同时填值搜索;  若`user_id`,`job_number`,`ic_number`其中存在两者或三者的值,则按照此优先级取过滤条件 :  `user_id` > `job_number` > `ic_number`


## 请求示例:

获取时间段 `1669552210` [2022-11-27 20:30:10] 到 `1669742085` [2022-11-30 01:14:45] 时间段中,`job_number`为 `1111`的通行记录,且单次请求获取`3`条记录.

> `/v1/event/records`

```json
{
    "begin_time": 1678784160,
    "end_time": 1778784400,
    "offset": 3,
    "limit": 3,
    "sort": 0
}
```

## 返回示例

其中`rgb_image`字段为base64后的图片内容.

```json
{
    "data": {
        "offset": 3,
        "limit": 3,
        "count": 3,
        "total": 260,
        "items": [
            {
                "recognitionType": 0,
                "entry_mode": 1,
                "deviceSN": "PSC700C0MC22F02542",
                "abnormal_type": 0,
                "uuid": "a969ec70-ce1f-4c8c-9b62-1cd5c6047dc7",
                "recognizeScore": 0.9120988845825195,
                "bodyTemperature": 0,
                "mask": 0,
                "rgb_image":"",
                "pass": false,
                "mode": 10,
                "user": {
                    "name": null,
                    "user_id": "",
                    "type": null,
                    "ic_number": "",
                    "id_number": "",
                    "job_number": ""
                },
                "timestamp": 1684379730,
                "groups": []
            },
            {
                "recognitionType": 1,
                "entry_mode": 1,
                "deviceSN": "PSC700C0MC22F02542",
                "abnormal_type": 20002,
                "uuid": "461521f7-d963-4124-b615-f87e077f52c7",
                "recognizeScore": 0.9401368498802185,
                "bodyTemperature": 0,
                "mask": 0,
                "rgb_image": "/57UwHgNgevX0qtqlx5FoW3ESOSBtPXNXFXZEtEZ1zP5lwQju0afKCT0/Cremr5l",
                "pass": false,
                "mode": 10,
                "user": {
                    "name": "王五",
                    "user_id": "5",
                    "type": 1,
                    "ic_number": "12345",
                    "id_number": "",
                    "job_number": "23385"
                },
                "timestamp": 1684379734,
                "groups": [
                    {
                        "id": "2",
                        "name": "测试2"
                    }
                ]
            },
            {
                "recognitionType": 1,
                "entry_mode": 1,
                "deviceSN": "PSC700C0MC22F02542",
                "abnormal_type": 20002,
                "uuid": "4e552d5a-6bd3-4f7b-bde0-2551e665afde",
                "recognizeScore": 0.9471220374107361,
                "bodyTemperature": 0,
                "mask": 0,
                "rgb_image": "/9k=",
                "pass": false,
                "mode": 10,
                "user": {
                    "name": "王五",
                    "user_id": "5",
                    "type": 1,
                    "ic_number": "12345",
                    "id_number": "",
                    "job_number": "23385"
                },
                "timestamp": 1684379898,
                "groups": [
                    {
                        "id": "2",
                        "name": "测试2"
                    }
                ]
            }
        ]
    },
    "code": 200,
    "msg": "OK"
}
```