# Modify rule information

Modify rule information.

## Request address

> `/v1/rule/id/{id}`

## Request method

> PUT

## Request parameters

| Parameter name | Type   | Required | Description | Remark |
| -------------- | ------ | -------- | ----------- | ------ |
| name           | string | Y        | Rule name   |        |
| schedule       | object | Y        | Schedule    |        |

Request example：

```
{

"rule_id": 1,

" name": "test_rule",

"schedule ": {


}

}
```

## Response parameters

| Parameter name | Type   | Description |
| -------------- | ------ | ----------- |
| id             | string | Rule id     |

```json
{
    "data": {
        "rule_id": 1,
        "name": "test_rule",
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