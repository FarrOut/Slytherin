#!/usr/bin/env python3
import os

import aws_cdk as cdk

from slytherin.network_stack import NetworkStack
from slytherin.ec2_stack import Ec2Stack

app = cdk.App()

net = NetworkStack(app, "NetworkStack",
                   env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'),
                                       region=os.getenv('CDK_DEFAULT_REGION')),
                   )

ec2 = Ec2Stack(app, "Ec2Stack",
               vpc=net.vpc,
               key_name=app.node.try_get_context("key_name"),
               env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
               )

app.synth()
