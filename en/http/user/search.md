# Search

Search the 'id' list of related objects according to the specified fields.


## Request address

> `/v1/user/id/{id}`

## Request method

> POST

- Body Type: `application/json`

## Request parameters
|  Parameter name       | Type   | Required | Description               |
| ---------- | ------ | ---- | ---------------------- |
| name       | String | N    | Search related objects according to this field |
| ic_number  | String | N    | Search related objects according to this field |
| job_number | String | N    | Search related objects according to this field |

> Note: The `name` / `ic_number` / `job_number`  fields cannot be searched by filling in values at the same time. If there are two or more values,then the filter conditions are obtained according to this priority : `name` > `ic_number` > `job_number`

## Request example:

> `/v1/user/search`

```json
{
    "name":"A"
}
```

## Response example

```json
{
    "data": {
        "items": [
            2,
            55,
            117
        ]
    },
    "code": 200,
    "msg": "OK"
}
```