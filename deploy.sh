#!/usr/bin/env bash

set -ue

aws cloudformation package  --template-file template.yaml --s3-bucket "aws-sam-cli-managed-default-samclisourcebucket-nyt2w42xlyal" --output-template-file output-template.yaml
aws cloudformation deploy  --template-file output-template.yaml --stack-name least-privilege-role --capabilities CAPABILITY_IAM

aws s3 cp template.yaml s3://apibucketleastprivilege/template.yaml
