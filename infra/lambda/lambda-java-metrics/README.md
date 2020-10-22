# signalfx-lambda-java-metrics

This example creates a simple HelloWorld Lambda Function with metrics visible in SignalFx without CloudWatch enabled.

Requirements:

Same requirements as described at top of repo
AWS CLI installed 

#### Step #0 Create your lambda function in AWS

Name: JavaDemo

Handler: ```com.signalfx.lambda.wrapper.SignalFxRequestWrapper::handleRequest```

Runtime: Java 8

Check your realm and token in your SignalFx profile to set environment variables:

```
SIGNALFX_AUTH_TOKEN     YOUR TOKEN HERE
SIGNALFX_API_HOSTNAME   ingest.YOURREALMHERE.signalfx.com
SIGNALFX_LAMBDA_HANDLER HelloWorld.App::handleRequest
```

These can be found in your SignalFx profile. SIGNALFX_METRICS_URL is the same as the “Real-time Data Ingest” URL.
DO NOT include "https://" in the values- i.e. use only ```ingest.YOURREALMHERE.signalfx.com```

#### Step #1 Ensure Java 8 and Maven build environment

Example:

```
$ java -version
openjdk version "1.8.0_232"
OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_232-b09)
OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.232-b09, mixed mode)


$ javac -version
javac 1.8.0_232

$ mvn -version
Apache Maven 3.6.3 (cecedd343002696d0abb50b32b541b8a6ba2883f)
Maven home: /usr/local/Cellar/maven/3.6.3/libexec
Java version: 1.8.0_232, vendor: AdoptOpenJDK, runtime: /Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "mac os x", version: "10.14.6", arch: "x86_64", family: "mac"
```

#### Step #2 After cloning this repo, build Java application at root directory

```
git clone https://github.com/stevelsplunk/lambda-java
cd lambda-java
mvn package
```

#### Step #3 Upload resulting Java deployment package to Lambda function
```
aws lambda update-function-code --function-name JavaDemo --zip-file fileb://target/lambda-java-example-1.0-SNAPSHOT.jar
```

#### Step #4 Test lambda function and send output to test.txt
```
aws lambda invoke --function-name JavaDemo test.txt
```

stdout should show:

{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}

test.txt should contain:

```
"Hello from Lambda!"
```

#### Step #5 Your Lambda (SignalFx Overview) dashboard will show the Active Functions each time the function is invoked
