# AWS-SageMaker-Lambda-API-Gateway

## step1. SageMaker
- Create notebook instance
  - Notebook instance name (eg. ml-model-instance)
  - IAM role -> Create a new role -> Create role -> Create notebook instance
  - Open Jupyter
- Run your notebook and save the endpoint
- Inference -> Endpoints

## step2. Lambda (trigger endpoint with a payload which is delivered by api gateway)

