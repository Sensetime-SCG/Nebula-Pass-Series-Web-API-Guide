# 查询策略信息

根据指定的`rule_id`获取该策略信息

## 请求路径

> `/v1/rule/id/{id}`

## 请求方式

> GET


## 请求示例

获取`rule_id`为 1 的策略信息。

> `/v1/rule/id/1`

## 返回示例

```json
{
    "data": {
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
    },
    "code": 200,
    "msg": "OK"
}
```