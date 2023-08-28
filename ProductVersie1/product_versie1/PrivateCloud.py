import aws_cdk as cdk
from aws_cdk import aws_ec2 as ec2

class CloudStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "PrivateWolk", max_azs=2)





