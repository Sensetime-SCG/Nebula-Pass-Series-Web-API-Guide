# Query rule list

Query rule list.

## Request address

> `/v1/rule/offset/{offset}/limit/{limit}`

## Request method

> GET

## Request parameters

| Parameter name | Type | Required | Description                                                  |
| -------------- | ---- | -------- | ------------------------------------------------------------ |
| offset         | int  | Y        | The data offset of the current page, which must be greater than or equal to 0 and less than 100000 |
| limit          | int  | Y        | The data item limit of the current page must be greater than 0 and less than or equal to 10 |

## Response parameters

| Parameter name | Type  | Description                     |
| -------------- | ----- | ------------------------------- |
| offset         | int   | The current offset              |
| limit          | int   | The current data item limit     |
| total          | int   | The total item number           |
| items          | array | The currently fetched data item |

Description of each element field in items:

| **Parameter name** | **Type** | **Description** | **Remark** |
| ------------------ | -------- | --------------- | ---------- |
| rule_id            | int      | Rule id         |            |
| name               | string   | Rule name       |            |
| schedule           | object   | Schedule        |            |

Response example：

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