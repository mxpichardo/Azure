import json
import os
import azure.functions as func
import boto3
from botocore.exceptions import ClientError


def main(req: func.HttpRequest) -> func.HttpResponse:
    username = req.params.get('username')
    if username:
        try:
            iam = boto3.client('iam',
                               aws_access_key_id=os.environ["AWS_AccessKeyId"],
                               aws_secret_access_key=os.environ["AWS_SecretAccessKey"])
            response_list = []
            # List access keys through the pagination interface.
            paginator = iam.get_paginator('list_attached_user_policies')
            try:
                for response in paginator.paginate(UserName=username):
                    response_list.append(response["AttachedPolicies"])
                response_list = [response for sublist in response_list for response in sublist]
            except iam.exceptions.NoSuchEntityException or iam.exceptions.InvalidInputException as err:
                return func.HttpResponse(str(err), status_code=404)
            return func.HttpResponse(json.dumps(response_list), status_code=200)
        except ClientError as err:
            return func.HttpResponse(str(err), status_code=401)
    else:
        return func.HttpResponse("Please pass a username on the query string", status_code=400)