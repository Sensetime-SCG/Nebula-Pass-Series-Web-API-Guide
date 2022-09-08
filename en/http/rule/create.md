# Add a rule

Add a rule.

**Access rules**:

Rule Interpretation: From Monday to Sunday, there are up to 3 rules per day; the special day plan is set by day, and a maximum of 31 days can be added, and there are up to 3 rules per day.

## Request address

> `/v1/rule`

## Request method

> POST

## Request parameters

| Parameter name | Type   | Required | Description | Remark                                                       |
| -------------- | ------ | -------- | ----------- | ------------------------------------------------------------ |
| rule_id        | int    | Y        | Rule id     | The unique identifier id set by the commit side, cannot be repeated, must be greater than 0 and less than 999999 |
| name           | string | Y        | Rule name   | The length must be greater than 0 and less than or equal to 32 |
| schedule       | object | Y        | Schedule    |                                                              |

schedule object field description：

| Parameter name | Type   | Description                              |
| -------------- | ------ | ---------------------------------------- |
| onset_point    | int    | Onset time, Unix, millisecond timestamp  |
| expire_point   | int    | Expire time, Unix, millisecond timestamp |
| mon_period     | object | Monday schedule                          |
| the_period     | object | Tuesday schedule                         |
| wed_period     | object | Wednesday schedule                       |
| thur_period    | object | Thursday schedule                        |
| fri_period     | object | Friday schedule                          |
| sat_period     | object | Saturday schedule                        |
| sun_period     | object | Sunday schedule                          |
| special_days   | object | Special day schedule                     |

xxx_period object field description：

| Parameter name | Type   | Description |
| -------------- | ------ | ----------- |
| start_time     | object | Onset time  |
| end_time       | object | Expire time |

special_days object field description：

| Parameter name | Type   | Description                                                  |
| -------------- | ------ | ------------------------------------------------------------ |
| year           | int    | The year of the onset time point. The valid value is ≥ 0. If it is 0, it means that it will take effect every year. |
| month          | int    | The month in the onset time point, the valid value is 0\~12, if it is 0, it means it will take effect every month. |
| day            | int    | The day in the onset time point, the valid value is 0\~31, if it is 0, it means it will take effect every day. |
| today_period   | object |                                                              |

start_time and end_time object field description：

| Parameter name | Type | Description                                                  |
| -------------- | ---- | ------------------------------------------------------------ |
| hour           | int  | The hour value in the onset time point, the valid value is 0\~23 |
| min            | int  | The minute value in the onset time point, the valid value is 0~59 |
| sec            | int  | The second value in the onset time point, the valid value is 0\~59 |

Request example：

```
{
    "rule_id": 4,
    "name": "Rule4",
    "schedule":{
        "onset_point":1660097956,
        "expire_point":2543710756,
        "mon_period": [
            {
            "start_time":{
				"hour":0,
				"min":0,
				"sec":0
			},
			"end_time": {
				"hour":12,
				"min":10,
				"sec":50
			}
            },
            {
            "start_time":{
				"hour":13,
				"min":0,
				"sec":0
			},
			"end_time": {
				"hour":18,
				"min":0,
				"sec":0
			},
            "start_time":{
				"hour":19,
				"min":0,
				"sec":0
			},
			"end_time": {
				"hour":23,
				"min":0,
				"sec":0
			}            
            }            
        ],
        "the_period": [],
        "wed_period": [],
        "thur_period": [],
        "fri_period": [],
        "sat_period": [],
        "sun_period": [],
        "special_days": []
    }
}
```

## Response parameters

| Parameter name | Type                        | Description |
| -------------- | --------------------------- | ----------- |
| rule_id        | int                         | Rule ID     |
| name           | string                      |             |
| schedule       | object                      |             |
| create_at      | Unix, millisecond timestamp |             |
| update_at      | Unix, millisecond timestamp |             |

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