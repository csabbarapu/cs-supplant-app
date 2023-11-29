import aws_cdk as cdk
from constructs import Construct
from packages.serverless_stack import ServerlessStack


class DeployAll(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ServerlessApp
        self.serverless_stack = ServerlessStack(
            self,
            "cs-serverless-stack",
        )
