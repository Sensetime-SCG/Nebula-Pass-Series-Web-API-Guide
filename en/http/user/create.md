# Add a user

Add a user.

## Request address

> `/v1/user`

## Request method

> POST

- Body Type: `application/json`

## Request parameters

| Parameter name   | Type    | Required                                     | Description                                        | Remark                                                       |
| ---------------- | ------- | -------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------ |
| name             | string  | Y                                            | User name                                          | The length should be greater than 0 and less than or equal to 128 |
| user_id          | int     | Y                                            | The unique id set by the commit side               | Cannot be repeated, must be greater than 0 and less than 999999 |
| type             | int     | N                                            | 1：employee 2：visitor                             | Default：1, cannot be modified after creating                |
| avatar           | string  | Y (When feature has a value, it can be null) | Person avatar, basemap                             | base64 encoding, limited to 10MB                             |
| feature          | string  | N                                            | Feature value                                      | When avatar and feature have values at the same time, the feature shall prevail, and the limit is less than 10KB |
| ic_number        | string  | N                                            | IC number                                          | The length limit is 128 bytes                                |
| id_number        | string  | N                                            | ID number                                          | The length limit is 128 bytes                                |
| job_number       | string  | N                                            | Job number                                         | The length limit is 128 bytes                                |
| guest_time_start | int     | N                                            | Visit start time, Unix, timestamp in milliseconds. |                                                              |
| guest_time_end   | int     | N                                            | Visit end time, Unix, timestamp in milliseconds.   |                                                              |
| groups           | int []  | N                                            | List of binding groups                             | Min: 1 Max: 100 Binding group types are not mutually exclusive |
| is_admin         | boolean | Y                                            | Whether to enable administrator privileges         | Face-swiping authentication on user device management interface |
| remark           | string  | N                                            | Remark                                             | Cannot exceed 256 bytes                                      |

## Request example：

add a user, this user `user_id` is `3`, `name` is `Jack`, `type` is `1`, and bind group `1` and `2`

```json
{
  "user_id":3,
  "name": "Jack",
  "avatar": "/9j/2wCEAAoHBwgHBgoICAgLCgoLDhgQDg0NDh0VFhEYIx8lJCIfIiEmKzcvJik0KSEiMEExNDk7Pj4",
  "type": 1,
  "groups": [1,2]
}
```


## Response example

```json
{
  "data": {
        "user_id":3,
        "name": "张三",
        "avatar": "/9j/2wCEAAoHBwgHBgoICAgLCgoLDhgQDg0NDh0VFhEYIx8lJCIfIiEmKzcvJik0KSEiMEExNDk7Pj4",
        "type": 1,
        "ic_number":"",
        "job_number":"",
        "id_number":"",
        "groups": [1,2],
        "is_admin":false,
        "remark":"",
        "create_at": 1660222970940,
        "update_at": 1660222970940
  },
  "code": 200,
  "msg": "OK"
}
```