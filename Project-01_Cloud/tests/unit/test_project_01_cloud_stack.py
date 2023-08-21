import aws_cdk as core
import aws_cdk.assertions as assertions

from project_01_cloud.project_01_cloud_stack import Project01CloudStack

# example tests. To run these tests, uncomment this file along with the example
# resource in project_01_cloud/project_01_cloud_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Project01CloudStack(app, "project-01-cloud")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
