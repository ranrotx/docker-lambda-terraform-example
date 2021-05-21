# docker-lambda-terraform-example
Example for how to deploy Docker-based Lambda functions using Terraform. This was adapted from instructions found here: https://hands-on.cloud/terraform-deploy-python-lambda-container-image/

## Steps to deploy

1. Clone repo
2. Make sure that Docker is running locally first.
3. `terraform apply`
4. Test the function invocation: `aws lambda invoke --function-name demo-lambda out --log-type Tail --query 'LogResult' --output text |  base64 -d`