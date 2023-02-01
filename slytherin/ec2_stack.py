from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct


class Ec2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, vpc: ec2.Vpc, key_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ec2.Instance(self, 'MyInstance',
                     vpc=vpc,
                     instance_type=ec2.InstanceType.of(
                         ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
                     key_name=key_name,
                     machine_image=ec2.MachineImage.latest_amazon_linux(),
                     )
