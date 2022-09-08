# Query a rule

Query a rule.

## Request address

> `/v1/rule/id/{id}`

## Request method

> GET

## Request parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

## Response parameters

| **Parameter name** | **Type** | **Description**             | **Remark** |
| ------------------ | -------- | --------------------------- | ---------- |
| rule_id            | int      | Rule id                     |            |
| name               | string   | Rule name                   |            |
| schedule           | object   | Schedule                    |            |
| create_at          | int      | Unix, millisecond timestamp |            |
| update_at          | int      | Unix, millisecond timestamp |            |

Example of successful return：

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