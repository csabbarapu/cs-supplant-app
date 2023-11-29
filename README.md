# cs-supplant-app

This project deploys a fully functional CDK Pipeline together with a serverelss app that does string replacement.

    cs-supplant-sapp
    |
    +-- cdk_pipeline
    |   |
    |   +-- pipeline_stack.py
    +-- packages
    |   |
    |   +-- stack_1
    |   |   |
    |   +-- stack_2
    |   |   |   |
    |   +-- stack_N
    +-- lambda_functions
    |   |
    |   +-- lambda_a
    |   +-- lambda_b
    +-- operations
    |   |
    |   +-- environment.py
    +-- stages
    |   |
    |   +-- stage.py
    +-- tests
    |   |
    |   +-- unit_tests
    |   |   |
    |   |   +-- stack_1.py
    |   |   +-- stack_2.py
    +-- .gitignore
    +-- .pre-commit-config.yaml
    +-- .app.py
    +-- cdk.json
    +-- requirements.txt
    +-- README.md

## `/cdk_pipeline`: Pipeline_stack for CICD

At this location cdk pipeline stack will be stored.

## `/packages`: Packages

At this location, all stacks will be stored.

## `/operations`: environments/cloud targets

At this location, environments/cloud targets will be defined.

## `/stages`: Define Stages here for deploying inside the pipeline.

At this location, all stages will be stored. A stage can have a stack or group of stacks deployed together.

## `/lambda_functions`: lambda code

We use a lambda folder to store all lambda core under its own handler folder

## `/tests`: Tests

We use thisfor _unit_ tests:

- **Unit tests** should test the smallest independent units of your package code, i.e., functions or classes that only accomplish one piece of functionality.
  Each unit test should run very fast and should not connect to external services like AWS.
## Install the AWS CDK

Install the AWS CDK Toolkit globally using the following Node Package Manager command.

```
npm install -g aws-cdk
```

Run the following command to verify correct installation and print the version number of the AWS CDK.

```
cdk --version
```

## Bootstrapping
Deploying stacks with the AWS CDK requires dedicated Amazon S3 buckets and other containers to be available to AWS CloudFormation during deployment. Creating these is called bootstrapping. To bootstrap, issue:

```
cdk bootstrap aws://ACCOUNT-NUMBER/REGION
```

# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

## Usage

### AWS Management Console
- Open the AWS Management Console and navigate to the API Gateway service.
- Select the API Gateway that you created using the AWS CDK code.
- Click on the `Resources` link in the left-hand menu.
- Click on the resource that you created (in this example, it's called `cs-supplant-api`).
- Click on the `POST` method that you created.
- In the `Integration Request` section, you should see a "Body Mapping Templates" dropdown menu.
- Select `application/json` from the dropdown menu.
In the "Template" field, enter the following JSON payload:
```json
{
    "input_str": "The analysts of Rabo did a great job!."
}
```

### Curl
- CURL command that you can use to invoke the API Gateway resource with an input string
```
curl -X POST \
  https://6mix60gim9.execute-api.eu-west-1.amazonaws.com/prod/ \
  -H 'Content-Type: application/json' \
  -d '{
    "input_str": "The analysts of ING did a great job!."
  }'
```
