# Query rule list

Query rule list.

## Request address

> `/v1/rule/offset/{offset}/limit/{limit}`

## Request method

> GET

## 请求示例

The starting offset of acquisition is 0, and the upper limit of currently acquired data items is 10, where the `count` field represents the number of currently acquired data items, and the `total` field represents the total number of entries in the database.

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