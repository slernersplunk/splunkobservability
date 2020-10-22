import json
import signalfx_lambda

@signalfx_lambda.emits_metrics
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! You are being bitten!'),
        x/0

    }
