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
    - click Visual (you can see SageMaker action) -> Save changes
    - 
## Step3. Amazon API Gateway
  - AWS console -> API Gateway -> Create API -> Rest API -> Build -> New API -> API name (eg. ml-model-api) -> Create API 
  - Create resource (eg. api-ml-model)
  - Create method -> method type (POST) -> choose your Lambda function (eg. ml-model-lambda) -> Create
  - enter input in Request body -> Test
  - Deploy API -> New Stage -> Stage name (eg. PROD)
  - Invoke URL


# SageMaker

## 1. import sagemaker and boto3.
## 2. create s3 bucket for saving code and model artifacts.
## 3. import python libraries.
## 4. download the data and save it as .csv file in the local folder, and take a look at it.
## 5. split the data into training, validation, and testing dataset.
## 6. convert the datasets to the recordIO-wrapped protobuf format, and upload this data to s3. 
  - RecordIO-Protobuf format is used by SageMaker's built-in algorithms like:
    - Linear Learner
    - PCA
    - K-Means
    - Factorization Machines
    - Random Cut Forest
    - Laten Dirichlet Allocation

## 7. Specify container images used for training and hostin SageMaker's linear-learner



