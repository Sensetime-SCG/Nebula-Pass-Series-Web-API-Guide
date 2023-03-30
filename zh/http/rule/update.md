# 更新策略信息

更新策略信息，其中`rule_id`字段值不可修改。

## 请求路径

> `/v1/rule/id/{id}`

## 请求方式

> PUT

- 请求体: `application/json`


| 字段     | 类型   | 必填 | 字段释义                            |
| -------- | ------ | ---- | ----------------------------------- |
| name     | String | Y    | 策略名称，内容长度1~128字节，不可重 |
| schedule | Object | Y    | 通行策略的具体内容                  |

其中`schedule`字段值的具体内容字段如下:

| 字段         | 类型         | 必填 | 字段释义                                                     |
| ------------ | ------------ | ---- | ------------------------------------------------------------ |
| onset_point  | Int          | Y    | 起效时间点,毫秒级Unix时间戳,范围: 大于 0 小于 4102415999000 (2099-12-31 23:59:59) |
| expire_point | Int          | Y    | 失效时间点,毫秒级Unix时间戳,范围: 大于 0 小于 4102415999000 (2099-12-31 23:59:59) |
| mon_period   | Object array | N    | 周一时刻表,上限12条;默认空                                   |
| the_period   | Object array | N    | 周二时刻表,上限12条;默认空                                   |
| wed_period   | Object array | N    | 周三时刻表,上限12条;默认空                                   |
| thur_period  | Object array | N    | 周四时刻表,上限12条;默认空                                   |
| fri_period   | Object array | N    | 周五时刻表,上限12条;默认空                                   |
| sat_period   | Object array | N    | 周六时刻表,上限12条;默认空                                   |
| sun_period   | Object array | N    | 周日时刻表,上限12条;默认空                                   |
| special_days | Object array | N    | 特殊日期时刻表,上限31条;默认空                               |

各`period`字段值的具体内容字段如下:

| 字段       | 类型   | 必填 | 字段释义            |
| ---------- | ------ | ---- | ------------------- |
| start_time | Object | N    | 当日起效时间;默认空 |
| end_time   | Object | N    | 当日失效时间;默认空 |

`special_days`字段值的具体内容字段如下：

| 名称         | 类型         | 必填 | 说明                                                     |
| ------------ | ------------ | ---- | -------------------------------------------------------- |
| year         | Int          | N    | 起效时间点的年,有效值0~2099，若为0则表示每年都生效;默认0 |
| month        | Int          | N    | 起效时间点的月,有效值0~12，若为0则表示每月都生效;默认0   |
| day          | Int          | N    | 起效时间点的日,有效值0~31，若为0则表示每日都生效;默认0   |
| today_period | Object array | N    | 当日时刻表,上限12条;默认空                               |

`start_time`与`end_time`字段值的具体内容如下：

| 名称 | 类型 | 必填 | 说明                                 |
| ---- | ---- | ---- | ------------------------------------ |
| hour | Int  | N    | 起效时间点中的小时，有效值0~23;默认0 |
| min  | Int  | N    | 起效时间点中的分钟，有效值0~59;默认0 |
| sec  | Int  | N    | 起效时间点中的秒数，有效值0~59;默认0 |


## 请求示例:

更新`rule_id`为 1 的策略信息。

> `/v1/rule/id/1`

```json
{
    "name": "1",
    "schedule": {
        "onset_point": 1640966400000,
        "expire_point": 1672502399000,
        "special_days": [
            {
                "year": 0,
                "month": 0,
                "day": 1,
                "today_period": [
                    {
                        "start_time": {
                            "hour": 6,
                            "min": 30,
                            "sec": 0
                        },
                        "end_time": {
                            "hour": 12,
                            "min": 30,
                            "sec": 0
                        }
                    },
                    {
                        "start_time": {
                            "hour": 14,
                            "min": 0,
                            "sec": 0
                        },
                        "end_time": {
                            "hour": 18,
                            "min": 30,
                            "sec": 30
                        }
                    }
                ]
            }
        ]
    }
}
```

## 返回示例

```json
{
    "data": {
        "rule_id": "1",
        "name": "1",
        "schedule": {
            "onset_point": 1640966400000,
            "expire_point": 1672502399000,
            "mon_period": [],
            "the_period": [],
            "wed_period": [],
            "thur_period": [],
            "fri_period": [],
            "sat_period": [],
            "sun_period": [],
            "special_days": [
                {
                    "year": 0,
                    "month": 0,
                    "day": 1,
                    "today_period": [
                        {
                            "start_time": {
                                "hour": 6,
                                "min": 30,
                                "sec": 0
                            },
                            "end_time": {
                                "hour": 12,
                                "min": 30,
                                "sec": 0
                            }
                        },
                        {
                            "start_time": {
                                "hour": 14,
                                "min": 0,
                                "sec": 0
                            },
                            "end_time": {
                                "hour": 18,
                                "min": 30,
                                "sec": 30
                            }
                        }
                    ]
                }
            ]
        },
        "create_at": 1660297993368,
        "update_at": 1660298961022
    },
    "code": 200,
    "msg": "OK"
}
```