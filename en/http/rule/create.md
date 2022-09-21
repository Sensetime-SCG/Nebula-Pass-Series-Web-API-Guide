# Add a rule

Add a rule.

**Access rules**:

Rule Interpretation: From Monday to Sunday, there are up to 3 rules per day; the special day plan is set by day, and a maximum of 31 days can be added, and there are up to 3 rules per day.

## Request address

> `/v1/rule`

## Request method

> POST

- Body Type: `application/json`

## Request parameters

| Parameter name | Type   | Required | Description | Remark                                                       |
| -------------- | ------ | -------- | ----------- | ------------------------------------------------------------ |
| rule_id        | int    | Y        | Rule id     | The unique identifier id set by the commit side, cannot be repeated, must be greater than 0 and less than 999999 |
| name           | string | Y        | Rule name   | The length must be greater than 0 and less than or equal to 32 |
| schedule       | object | Y        | Schedule    |                                                              |

`schedule` object field description：

| Parameter name | Type   | Description                              |
| -------------- | ------ | ---------------------------------------- |
| onset_point    | int    | Onset time, Unix, millisecond timestamp  |
| expire_point   | int    | Expire time, Unix, millisecond timestamp |
| mon_period     | object array | Monday schedule                          |
| the_period     | object array| Tuesday schedule                         |
| wed_period     | object array| Wednesday schedule                       |
| thur_period    | object array| Thursday schedule                        |
| fri_period     | object array| Friday schedule                          |
| sat_period     | object array| Saturday schedule                        |
| sun_period     | object array| Sunday schedule                          |
| special_days   | object array| Special day schedule                     |

xxx_period object field description：

| Parameter name | Type   | Description |
| -------------- | ------ | ----------- |
| start_time     | object | Onset time  |
| end_time       | object | Expire time |

`special_days` object field description：

| Parameter name | Type   | Description                                                  |
| -------------- | ------ | ------------------------------------------------------------ |
| year           | int    | The year of the onset time point. The valid value is ≥ 0. If it is 0, it means that it will take effect every year. |
| month          | int    | The month in the onset time point, the valid value is 0\~12, if it is 0, it means it will take effect every month. |
| day            | int    | The day in the onset time point, the valid value is 0\~31, if it is 0, it means it will take effect every day. |
| today_period   | object |                                                              |

`start_time` and `end_time` object field description：

| Parameter name | Type | Description                                                  |
| -------------- | ---- | ------------------------------------------------------------ |
| hour           | int  | The hour value in the onset time point, the valid value is 0\~23 |
| min            | int  | The minute value in the onset time point, the valid value is 0~59 |
| sec            | int  | The second value in the onset time point, the valid value is 0\~59 |

## Request example：

```json
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

## Response example

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