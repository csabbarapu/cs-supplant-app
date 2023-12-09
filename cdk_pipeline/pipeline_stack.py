import aws_cdk as cdk
from aws_cdk import (
    pipelines as pipelines,
    Stack,
)
from constructs import Construct
from operations.get_aws_env import get_aws_env
from stages.serverless_app import DeployAll


class PipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Defining Environment
        aws_env = get_aws_env()

        # We are creating a pipeline for deploying to AWS account.
        self.pipeline = pipelines.CodePipeline(
            self,
            "CsPipeline",
            pipeline_name="cs-cdk-supplant-app-deploy",
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.git_hub(
                    "chaitanyasabbarapu/cs-supplant-app",
                    branch="master",
                ),  # Make sure to create a secret in AWS Secrets manager with github token.
                commands=[
                    "npm install -g aws-cdk",
                    "gem install cfn-nag",
                    "pip install -r requirements.txt",
                    "cdk synth",
                    "mkdir ./cfnnag_output",
                    "for template in $(find ./cdk.out -type f -maxdepth 2  \
                        -name '*.template.json'); do cp $template ./cfnnag_output; done",
                    "cfn_nag_scan --input-path ./cfnnag_output",
                ],
            ),
        )

        # Passing Serverless stack in a stage to pipeline to deploy.
        # self.deploy = self.pipeline.add_stage(
        #     DeployAll(self, "Deploy", env=aws_env),
        # )

        self.destroy = self.pipeline.add_stage(
            DeployAll(self, "Destroy", env=aws_env),
        )
        # self.destroy.add_post(pipelines.ManualApprovalStep("approval"))
