# Splunk OpenTelemetry Java Lambda Wrapper

The Splunk OpenTelemetry Java Lambda Wrapper is a modified version of the
wrappers in the [OpenTelemetry AWS Lambda Instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/master/instrumentation/aws-lambda-1.0/library)
that enables you to export spans from an AWS Lambda function with Java to
Splunk APM without any code changes to your Lambda functions.

Current release uses `OpenTelemetry AWS Lambda Instrumentation` version `0.12.0`.

The Splunk Lambda wrapper uses B3 context propagation and a jaeger-thrift
exporter by default to send trace metadata to Splunk APM. If needed, you can
customize context propagation and the exporter when you deploy the wrapper.

Outbound context propagation for lambdas instrumented with this wrapper can be easily implemented. Please have a look [here](outbound-context-propagation.md)

This project contains the custom wrapper code in the [wrapper](https://github.com/signalfx/splunk-otel-java-lambda-wrapper/tree/main/wrapper)
directory and examples in the [examples](https://github.com/signalfx/splunk-otel-java-lambda-wrapper/tree/main/examples) directory.

There are two options to use the Splunk Lambda wrapper:

- Use a Lambda function wrapper directly
- Use a Lambda layer that Splunk hosts

Splunk provides a Serverless Application Model (SAM) template for deploying
the Lambda wrapper with a Lambda handler or a Lambda layer. If you choose
deploy the Lambda wrapper with a layer, Splunk also hosts a layer in AWS.

## Deploy the wrapper directly with a Lambda function handler

A Splunk Lambda wrapper wraps around an existing AWS Lambda Java function
handler. This approach doesn't require any code changes to your Lambda function.
When you deploy the Lambda wrapper with a Lambda handler, you add it as a
dependency to your Lambda function. Whenever the Lambda function is invoked,
it runs the Lambda wrapper which in turn calls your code. For more information
about AWS Lambda function handlers, see
[AWS Lambda function handler in Java](https://docs.aws.amazon.com/lambda/latest/dg/java-handler.html)
on the AWS website.

Follow these steps to configure a Splunk Lambda wrapper to export spans to
Splunk APM. You can also deploy the handler with a SAM
template. For more information, see the [example](./examples/splunk-wrapper/README.md). 

1. Add the Splunk Lambda wrapper to your build definition:

   Gradle:
   ```
   dependencies {
     implementation("com.splunk.public:otel-lambda-wrapper:1.0.0")
   }
   ```

   Maven:
   ```
   <dependency>
     <groupId>com.splunk.public</groupId>
     <artifactId>otel-lambda-wrapper</artifactId>
     <version>1.0.0</version>
   </dependency>
   ```
2. From the AWS console, upload the .zip file to your Lambda function code.
   For more information, see [Deploy Java Lambda functions with .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/java-package.html)
   on the AWS website.
3. Set a wrapper class as the handler for your Lambda function. These wrappers
   are available:
   | Wrapper class | Description |
   | ------------- | ----------- |
   | `com.splunk.support.lambda.TracingRequestWrapper` | Wrap a regular handler. |
   | `com.splunk.support.lambda.TracingRequestApiGatewayWrapper` | Wrap a regular handler proxied through an API Gateway. |
   | `com.splunk.support.lambda.TracingRequestStreamWrapper` | Wrap a streaming handler and enable HTTP context propagation for HTTP requests. |
   
   For more information about setting a handler for your Lambda function in the AWS console, see [Configuring functions in the console](https://docs.aws.amazon.com/lambda/latest/dg/configuration-console.html) on the AWS website.
4. Set the `OTEL_LAMBDA_HANDLER` environment variable in your Lambda function
   code:
   ```
   OTEL_LAMBDA_HANDLER="package.ClassName::methodName"
   ```
   For more information about setting environment variables in the AWS console,
   see [Using AWS Lambda environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html)
   on the AWS website.
5. By default, the Splunk Lambda wrapper uses B3 context propagation. If you
   want to change this, set the `OTEL_PROPAGATORS` environment variable in your
   Lambda function code. For more information about available context
   propagators, see the [Propagator settings](https://github.com/open-telemetry/opentelemetry-java-instrumentation#propagator)
   for the OpenTelemetry Java Instrumentation.
6. By default, the Splunk Lambda wrapper uses a jaeger-thrift exporter to send
   traces to Splunk APM. If you want to use this exporter, set these environment
   variables in your Lambda function code:
   ```
   OTEL_EXPORTER_JAEGER_ENDPOINT="http://yourEndpoint:9080/v1/trace"
   OTEL_EXPORTER_JAEGER_SERVICE_NAME="serviceName"
   SIGNALFX_AUTH_TOKEN="orgAccessToken"
   ```
   If you want to use a different exporter, set the `OTEL_EXPORTERS`
   environment variable. Other exporters have their own configuration settings.
   For more information, see the [OpenTelemetry Instrumentation for Java](https://github.com/open-telemetry/opentelemetry-java-instrumentation)
   on GitHub.
7. Set the environment in Splunk APM for the service with the
   `OTEL_RESOURCE_ATTRIBUTES` environment variable:
   ```
   OTEL_RESOURCE_ATTRIBUTES="environment=yourEnvironment"
   ```
8. Save your settings and call the Lambda function.

## Deploy the wrapper with a Lambda layer

Add a layer that includes the Splunk Lambda wrapper to your Lambda function.
A layer is code and other content that you can run without including it in
your deployment package. Splunk provides layers in all supported regions you
can freely use. 

You can also deploy the layer with a SAM template. For more information, see the
[example](./examples/splunk-layer/README.md).

To reduce the size of the deployment package, make sure that your Lambda
artifact doesn't contain the wrapper.

Follow these steps to configure a Splunk Lambda wrapper to export spans to
Splunk APM with a layer that Splunk provides. 

1. From the AWS console, add a layer to your Lambda function code.
2. To add a layer that Splunk provides, specify an available ARN, depending on
   your region. For an available ARN, see
   [Latest available versions of SignalFx Lambda wrapper layers](https://github.com/signalfx/lambda-layer-versions).
3. Verify that dependencies in the layer aren't also in the Lambda function
   .jar file.
4. Deploy your Lambda function code.

## Logging

These environment variables control logging:

| Environment variable | Description |
| -------------------- | ----------- |
| `OTEL_LIB_LOG_LEVEL` | Controls logging for the OpenTelemetry library itself. By default, it's set to `WARNING` and uses `java.util.logging` values. |
| `OTEL_LAMBDA_LOG_LEVEL` | Controls logging of the Splunk Lambda wrapper. By default, it's set to `WARN` and uses `log4j2` values.
  
## License and versioning

The Splunk OpenTelemetry Java Lambda Wrapper uses the
[OpenTelemetry Instrumentation for Java](https://github.com/open-telemetry/opentelemetry-java-instrumentation),
which is released under the terms of the Apache Software License version 2.0.
For more information, see the [license](./LICENSE) file.
