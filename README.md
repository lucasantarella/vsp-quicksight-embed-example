# VSP QuickSight Embed Example

## Documentation Links

- https://docs.aws.amazon.com/quicksight/latest/user/embedded-dashboards-for-authenticated-users-step-2.html
- https://docs.aws.amazon.com/quicksight/latest/user/embedded-dashboards-for-authenticated-users-step-3.html

## Setup

### Python

Python 3.8 is required.

Install dependencies with pip: `pip install -r requirements.txt`

### Environment Variables

The following environment variables are required. You can put these in a `.env` file in the root of the project, or set
them at run time.

```dotenv
AWS_ACCOUNT_ID=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_QUICKSIGHT_NAMESPACE=
AWS_QUICKSIGHT_USER_ARN=
```

## Run

Default port is `5050`. You can change this with the env `HTTP_PORT`

`python main.py`

You must use an SSL proxy to use the quicksight embed sdk. This is a quicksight restriction.

Please contact [Luca Santarella]('mailto:luca.santarella@lmsgrp.com') to whitelist your domain in the quicksight
dashboard.

## Test

Navigate to `https://your-domain.com/embed/52e31035-56c9-4928-ad78-d8e7604ce88f` to see the dashboard running.