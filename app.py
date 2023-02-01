#!/usr/bin/env python3
import os

import aws_cdk as cdk

from slytherin.network_stack import NetworkStack

app = cdk.App()

NetworkStack(app, "NetworkStack",
             env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
             )

app.synth()
