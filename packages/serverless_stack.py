from aws_solutions_constructs.aws_apigateway_lambda import ApiGatewayToLambda
from aws_cdk import aws_lambda as _lambda, aws_apigateway as apigw, App, Stack
from constructs import Construct


class ServerlessStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # We implement an Amazon API Gateway REST API connected to an AWS Lambda function.

        self.api_triggers_lambda = ApiGatewayToLambda(
            self,
            "ApiGatewayTriggersLambda",
            lambda_function_props=_lambda.FunctionProps(
                function_name="cs-string-supplant",
                runtime=_lambda.Runtime.PYTHON_3_9,
                handler="string_supplant.lambda_handler",
                code=_lambda.Code.from_asset("./lambda/"),
            ),
            api_gateway_props=apigw.RestApiProps(
                rest_api_name="cs-supplant-api",
                default_method_options=apigw.MethodOptions(
                    authorization_type=apigw.AuthorizationType.NONE
                ),
            ),
        )
