# signalfx-lambda-python-metrics

This example creates a simple HelloWorld Lambda Function with metrics visible in SignalFx without CloudWatch enabled.

Requirements:

Same requirements as described at top of repo
AWS CLI installed 

#### Step #0 Create your lambda function in AWS

Name: PythonDemo

Handler: ```lambda_function.lambda_handler```

Runtime: Python 3.7

Check your realm and token in your SignalFx profile to set environment variables:
```
SIGNALFX_ACCESS_TOKEN
SIGNALFX_INGEST_ENDPOINT
```
These can be found in your SignalFx profile. SIGNALFX_METRICS_URL is the same as the “Real-time Data Ingest” URL.
i.e. use ```https://ingest.YOURREALMHERE.signalfx.com```

#### Step #1 Ensure Python 3 environment

Example:
```
$ python3 --version
Python 3.7.6
```
#### Step #2 Choose the  ```lambda_function.py``` from the enclosed folders and copy to this directory

```PythonDemo/lambda_function.py``` is for a successful invocation
```PythonBite/lambda_function.py``` is for a successful invocation with an error

#### Step #3 Add file lambda_function.py to deployment package ```lambda_function.zip```
```
mkdir ./package && pip3 install --target ./package signalfx_lambda
```
#### Step #4 Assemble the deployment package
```
zip lambda_function.zip lambda_function.py
cd ./package && zip -r ../lambda_function.zip . && cd ..
```
#### Step #5 Update lambda function

For PythonDemo:
```
aws lambda update-function-code --function-name PythonDemo --zip-file fileb://lambda_function.zip
```

For PythonBite:
```
aws lambda update-function-code --function-name PythonBite --zip-file fileb://lambda_function.zip
```
#### Step #6 Test lambda function and send output to test.txt
```
aws lambda invoke --function-name PythonDemo test.txt
```
or
```
aws lambda invoke --function-name PythonBite test.txt
```

You can use the enclosed load test scripts to test at scale.
