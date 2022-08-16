# 批量获取策略信息

根据指定的`offset`与`limit`获取策略信息。要求 `offset`值范围是 0 到 100000；`limit`值范围是 0 到 10。

## 请求路径

> `/v1/rule/offset/{offset}/limit/{limit}`

## 请求方式

> GET


## 响应参数

| 字段   | 类型         | 释义                   |
| ------ | ------------ | ---------------------- |
| offset | int          | 当前数据条目请求偏移量 |
| limit  | int          | 当前数据条目获取上限   |
| count  | int          | 当前获取数据条目数量   |
| total  | int          | 数据条目总量           |
| items  | object array | 数据条目               |

## 请求示例

获取起始偏移为0，当前获取数据条目上限为10，其中`count`字段表示为当前获取到的数据条目量，`total`字段表示数据库中的总条目数。

> `/v1/rule/offset/0/limit/10`

## 返回示例

```json
{
    "data": {
        "offset": 0,
        "limit": 10,
        "count": 2,
        "total": 2,
        "items": [
            {
                "rule_id": 4,
                "name": "4",
                "schedule": {
                    "onset_point": 1660284813955,
                    "expire_point": 1690284813955,
                    "mon_period": [],
                    "the_period": [],
                    "wed_period": [],
                    "thur_period": [],
                    "fri_period": [],
                    "sat_period": [],
                    "sun_period": [],
                    "special_days": []
                },
                "create_at": 1660293169267,
                "update_at": 1660293169267
            },
            {
                "rule_id": 1,
                "name": "1",
                "schedule": {
                    "onset_point": 1640966400000,
                    "expire_point": 1672502399000,
                    "mon_period": [
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
                    ],
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
                                }
                            ]
                        },
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
                "update_at": 1660297993368
            }
        ]
    },
    "code": 200,
    "msg": "OK"
}
```