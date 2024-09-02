from aws_cdk import (
    # Duration,
    aws_s3 as s3,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class CdkLearnStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_s3_bucket = s3.Bucket(self, "mybucket1", bucket_name="pkm-cdk-s3-bucket121")
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkLearnQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
