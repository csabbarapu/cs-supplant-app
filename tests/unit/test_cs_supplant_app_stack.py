import aws_cdk as core
import aws_cdk.assertions as assertions

from packages.serverless_stack import ServerlessStack


# example tests. To run these tests, uncomment this file along with the example
# resource in cs_supplant_app/cs_supplant_app_stack.py
def test_lambda_apigateway_created():
    app = core.App()
    stack = ServerlessStack(app, "cs-supplant-app")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
