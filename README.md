# AWS-SageMaker-Lambda-API-Gateway

## step1. SageMaker
- Create notebook instance
  - Notebook instance name (eg. ml-model-instance)
  - IAM role -> Create a new role -> Create role -> Create notebook instance
  - Open Jupyter
- Run your notebook and save the endpoint
- Inference -> Endpoints

## step2. Lambda (trigger endpoint with a payload which is delivered by api gateway)
- Create a function
  - Function name (ml-model-lambda)
  - Runtime (Python 3.6)   
  - Create function
- write your lambda function
  - deploy
- Configuration
  - Environment variables -> Edit -> Add environment variable -> Key (eg. ENDPOINT_NAME) Value (eg. DEMO-linear-endpoint-202509161659), that means my lambda function will trigger this endpoint with a payload which just goes from api gateway. -> Save
  - AWS console -> IAM -> Roles -> click 'ml-model-lambda-role-...' -> click Policy name (eg. AWSLambdaBasicExecutionRole-...) -> Permissions -> {}JSON -> Edit Policy -> JSON -> addd the following codes:
    - {
        "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": "sagemaker:InvokeEndpoint",
      "Resource": "*"
      }
    - click Visual (you can see SageMaker action)
