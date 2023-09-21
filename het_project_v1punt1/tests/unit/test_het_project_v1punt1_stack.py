import aws_cdk as core
import aws_cdk.assertions as assertions

from het_project_v1punt1.het_project_v1punt1_stack import HetProjectV1Punt1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in het_project_v1punt1/het_project_v1punt1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = HetProjectV1Punt1Stack(app, "het-project-v1punt1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
