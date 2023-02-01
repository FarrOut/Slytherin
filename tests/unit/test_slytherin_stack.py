import aws_cdk as core
import aws_cdk.assertions as assertions

from slytherin.slytherin_stack import SlytherinStack

# example tests. To run these tests, uncomment this file along with the example
# resource in slytherin/slytherin_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SlytherinStack(app, "slytherin")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
