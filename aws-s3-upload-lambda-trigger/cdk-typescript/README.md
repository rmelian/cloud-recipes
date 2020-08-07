# S3 upload trigger lambda function

### What is this?
A serverless application that demonstrates how to trigger a lambda function after a file is uploaded into an S3 bucket. This version is using [AWS CDK](https://aws.amazon.com/cdk/)

### The Architecture
![Diagram](../assets/diagram.png)
* A client is a person or system who uploads files to an S3 bucket
* An S3 bucket publishes events after files are uploaded
* A lambda function is invoked with context information about the S3 bucket and file metadata


### Tech Stack
* [AWS CDK](https://aws.amazon.com/cdk/)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [Amazon S3](https://aws.amazon.com/s3/)
* [TypeScript](https://www.typescriptlang.org/)


### Prerequisite
* [TypeScript](https://www.typescriptlang.org/)
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)


### How to deploy it
```
npm install
cdk bootstrap
cdk deploy
```

### How to remove it
```
cdk destroy
```


### Author: Raisel Melian
* [Twitter](https://twitter.com/raiselmelian)