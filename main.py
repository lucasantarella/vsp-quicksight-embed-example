import os

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from flask import Flask, render_template

# load aws credentials from env
load_dotenv()

# init aws clients
qs = boto3.client('quicksight', region_name='us-east-1')
sts = boto3.client('sts')
app = Flask(__name__)


def get_dashboard_url(account_id, dashboard_id, quicksight_user_arn, quicksight_namespace, reset_disabled,
                      undo_redo_disabled):
    """
    From https://docs.aws.amazon.com/quicksight/latest/user/embedded-dashboards-for-authenticated-users-step-2.html
    :param quicksight_user_arn:
    :param quicksight_namespace:
    :param account_id:
    :param dashboard_id:
    :param reset_disabled:
    :param undo_redo_disabled:
    :return:
    """
    return qs.get_dashboard_embed_url(
        AwsAccountId=account_id,
        DashboardId=dashboard_id,
        IdentityType='QUICKSIGHT',
        Namespace=quicksight_namespace,
        SessionLifetimeInMinutes=600,
        UndoRedoDisabled=undo_redo_disabled,
        ResetDisabled=reset_disabled,
        UserArn=quicksight_user_arn
    )


@app.route('/embed/<string:dashboard_id>')
def get(dashboard_id):
    try:
        embed_data = get_dashboard_url(
            os.getenv('AWS_ACCOUNT_ID'),
            dashboard_id,
            os.getenv('AWS_QUICKSIGHT_USER_ARN'),
            os.getenv('AWS_QUICKSIGHT_NAMESPACE'),
            False,
            False
        )
        return render_template('embed.html', embed_url=embed_data['EmbedUrl'])
    except ClientError as e:
        print(e)


if __name__ == "__main__":
    app.run(port=int(os.getenv('HTTP_PORT', 5050)))
