#!/usr/bin/env bash

set -ue

sam deploy --no-confirm-changeset
aws s3 cp template.yaml s3://apibucketleastprivilege/template.yaml
