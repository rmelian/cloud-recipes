import * as cdk from '@aws-cdk/core';
import * as s3 from "@aws-cdk/aws-s3";
import * as s3nots from '@aws-cdk/aws-s3-notifications';
import * as lambda from "@aws-cdk/aws-lambda";

export class CdkTypescriptStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const bucket = new s3.Bucket(this, 'MyBucket', {
      bucketName: 'cdk-typescript-upload-bucket'
    });

    const handler = new lambda.Function(this, "UploadHandler", {
      runtime: lambda.Runtime.NODEJS_12_X,
      code: lambda.Code.asset("lib"),
      handler: "upload-handler.handle",
    });
    
    bucket.addObjectCreatedNotification(new s3nots.LambdaDestination(handler));
  }
}
