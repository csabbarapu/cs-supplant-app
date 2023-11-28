import os
import aws_cdk as cdk


def get_aws_env():
    """Retrieve AWS account ID and region"""
    # todo: write code to retrieve dynamically.
    return cdk.Environment(region="eu-west-1", account="420921345904")
