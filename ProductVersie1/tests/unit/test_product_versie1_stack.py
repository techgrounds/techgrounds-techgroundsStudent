import aws_cdk as core
import aws_cdk.assertions as assertions

from product_versie1.product_versie1_stack import ProductVersie1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in product_versie1/product_versie1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ProductVersie1Stack(app, "product-versie1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
