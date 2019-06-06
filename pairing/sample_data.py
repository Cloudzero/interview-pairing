# -*- coding: utf-8 -*-
# Copyright (c) 2016-present, CloudZero, Inc. All rights reserved.
# Licensed under the BSD-style license. See LICENSE file in the project root for full license information.

import base64

import simplejson as json

from pairing.utils import ExtendedEncoder

START_INSTANCES_EVENT = """
{
  "eventVersion":"1.05",
  "userIdentity":{
    "type":"AssumedRole",
    "principalId":"BBBBBBBBBBBBBBBBBBBBB:creator@user.com",
    "arn":"arn:aws:sts::123456789012:assumed-role/creator-user/creator@user.com",
    "accountId":"123456789012",
    "accessKeyId":"AAAAAAAAAAAAAAAAAAAA",
    "sessionContext":{
      "attributes":{
        "mfaAuthenticated":"false",
        "creationDate":"2018-07-17T14:58:35Z"
      },
      "sessionIssuer":{
        "type":"Role",
        "principalId":"BBBBBBBBBBBBBBBBBBBBB",
        "arn":"arn:aws:iam::123456789012:role/creator-user",
        "accountId":"123456789012",
        "userName":"creator-user"
      }
    }
  },
  "eventTime":"2018-03-02T16:17:18Z",
  "eventSource":"ec2.amazonaws.com",
  "eventName":"StartInstances",
  "awsRegion":"us-west-1",
  "sourceIPAddress":"10.10.10.10",
  "userAgent":"reactor unit tests",
  "requestParameters":{
    "instancesSet":{
      "items":[
        {
          "instanceId":"i-99999999991111111"
        },
        {
          "instanceId":"i-99999999992222222"
        }
      ]
    }
  },
  "responseElements":{
    "requestId":"da57afd6-34d3-4ac5-977f-d87328414baa",
    "instancesSet":{
      "items":[
        {
          "instanceId":"i-99999999991111111",
          "currentState":{
            "code":0,
            "name":"pending"
          },
          "previousState":{
            "code":80,
            "name":"stopped"
          }
        },
        {
          "instanceId":"i-99999999992222222",
          "currentState":{
            "code":0,
            "name":"pending"
          },
          "previousState":{
            "code":80,
            "name":"stopped"
          }
        }
      ]
    }
  },
  "requestID":"da57afd6-34d3-4ac5-977f-d87328414baa",
  "eventID":"a6e1634d-4fa3-4b99-be61-9524e513b911",
  "eventType":"AwsApiCall",
  "recipientAccountId":"123456789012"
}
"""

CREATE_NAT_GATEWAY = """
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "AAAAAAAAAAAAAAAAAAAA",
    "arn": "arn:aws:iam::123456789012:user/creator-user",
    "accountId": "123456789012",
    "accessKeyId": "BBBBBBBBBBBBBBBBBBBBB",
    "userName": "creator-user"
  },
  "eventTime": "2018-03-02T16:17:18Z",
  "eventSource": "ec2.amazonaws.com",
  "eventName": "CreateNatGateway",
  "awsRegion": "us-west-1",
  "sourceIPAddress": "10.10.10.10",
  "userAgent": "reactor unit tests",
  "requestParameters": {
    "CreateNatGatewayRequest": {
      "AllocationId": "eipalloc-abcdefgh",
      "SubnetId": "subnet-ababab"
    }
  },
  "responseElements": {
    "CreateNatGatewayResponse": {
      "xmlns": "http://ec2.amazonaws.com/doc/2016-11-15/",
      "natGateway": {
        "subnetId": "subnet-ababab",
        "natGatewayAddressSet": {
          "item": {
            "allocationId": "eipalloc-abcdefgh",
            "networkInterfaceId": "eni-adadadad"
          }
        },
        "createTime": "2018-07-16T08:47:50.000Z",
        "vpcId": "vpc-abababab",
        "natGatewayId": "nat-00000001111111111",
        "state": "pending"
      },
      "requestId": "d615c5f3-4ad2-40ba-97d7-951d050607f6"
    }
  },
  "requestID": "d615c5f3-4ad2-40ba-97d7-951d050607f6",
  "eventID": "a6e1634d-4fa3-4b99-be61-9524e513b911",
  "eventType": "AwsApiCall",
  "recipientAccountId": "123456789012"
}
"""

ATTACH_INTERNET_GATEWAY = """
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "AAAAAAAAAAAAAAAAAAAA",
    "arn": "arn:aws:iam::123456789012:user/creator-user",
    "accountId": "123456789012",
    "accessKeyId": "BBBBBBBBBBBBBBBBBBBBB",
    "userName": "creator-user"
  },
  "eventTime": "2018-03-02T16:17:18Z",
  "eventSource": "ec2.amazonaws.com",
  "eventName": "AttachInternetGateway",
  "awsRegion": "us-west-1",
  "sourceIPAddress": "10.10.10.10",
  "userAgent": "reactor unit tests",
  "requestParameters": {
    "internetGatewayId": "igw-01234567890123456",
    "vpcId": "vpc-ababababab"
  },
  "responseElements": {
    "_return": true
  },
  "requestID": "1b838b48-4eb9-415d-967e-e5cabcdb2d55",
  "eventID": "a6e1634d-4fa3-4b99-be61-9524e513b911",
  "eventType": "AwsApiCall",
  "recipientAccountId": "123456789012"
}
"""

CREATE_ROUTE_TABLE_IPV4 = """
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "AAAAAAAAAAAAAAAAAAAAAA",
    "arn": "arn:aws:iam::123456789012:user/creator-user",
    "accountId": "123456789012",
    "accessKeyId": "BBBBBBBBBBBBBBBBBBBBB",
    "userName": "creator-user"
  },
  "eventTime": "2018-03-02T16:17:18Z",
  "eventSource": "ec2.amazonaws.com",
  "eventName": "CreateRouteTable",
  "awsRegion": "us-west-1",
  "sourceIPAddress": "10.10.10.10",
  "userAgent": "reactor unit tests",
  "requestParameters": {
    "vpcId": "vpc-abababab"
  },
  "responseElements": {
    "routeTable": {
      "routeTableId": "rtb-bcbcbcbc",
      "vpcId": "vpc-abababab",
      "routeSet": {
        "items": [
          {
            "destinationCidrBlock": "172.20.0.0/16",
            "gatewayId": "local",
            "state": "active",
            "origin": "CreateRouteTable"
          }
        ]
      },
      "associationSet": {},
      "propagatingVgwSet": {},
      "tagSet": {}
    }
  },
  "requestID": "6d282543-4fa1-4f38-84ec-2eafbc245d5d",
  "eventID": "a6e1634d-4fa3-4b99-be61-9524e513b911",
  "eventType": "AwsApiCall",
  "recipientAccountId": "123456789012"
}
"""


def create_kinesis_lambda_event(payloads):
    """
    Given an iterable of payloads, embed them in properly-formatted kinesis messages batched for consumption by lambda.

    Args:
        payloads: (iterable) - an iterable of payloads.  Can literally be anything that can be serialized to JSON

    Returns:
        dict - the lambda function payload.
    """
    return {
        "Records": [
            {
                "kinesis": {
                    "partitionKey": "partitionKey-03",
                    "kinesisSchemaVersion": "1.0",
                    "data": base64.b64encode(json.dumps(payload, cls=ExtendedEncoder,
                                                        iterable_as_array=True).encode('utf-8')),
                    "sequenceNumber": "49545115243490985018280067714973144582180062593244200961",
                    "approximateArrivalTimestamp": 1428537600.0
                },
                "eventSource": "aws:kinesis",
                "eventID": "shardId-000000000000:49545115243490985018280067714973144582180062593244200961",
                "invokeIdentityArn": "arn:aws:iam::EXAMPLE",
                "eventVersion": "1.0",
                "eventName": "aws:kinesis:record",
                "eventSourceARN": "arn:aws:kinesis:EXAMPLE",
                "awsRegion": "us-east-1"
            }
            for payload in payloads
        ]
    }


def generate_kinesis_batch(n=100):
    """
    Create a batch of kinesis events that contain embedded cloudtrail events.
    This can be ingested by a lambda function.

    Args:
        n: (int) - The number of events to generate (technically, we'll generate 4 different types for each)

    Returns:
        dict - The sample lambda event
    """
    payloads = []
    for i in range(0, n):
        event_string = START_INSTANCES_EVENT.replace('i-99999999991111111', f'i-99999999991{i}')
        event_string = event_string.replace('i-99999999992222222', f'i-99999999992{i}')
        instance_event = json.loads(event_string)

        event_string = CREATE_NAT_GATEWAY.replace('nat-00000001111111111', f'nat-00000001{i}')
        nat_gateway_event = json.loads(event_string)

        event_string = CREATE_ROUTE_TABLE_IPV4.replace('rtb-bcbcbcbc', f'rtb-bcbcbcbc{i}')
        route_table_event = json.loads(event_string)

        event_string = ATTACH_INTERNET_GATEWAY.replace('igw-01234567890123456', f'igw-01234567890{i}')
        internet_gateway_event = json.loads(event_string)

        payloads += [instance_event, nat_gateway_event, route_table_event, internet_gateway_event]
    return create_kinesis_lambda_event(payloads)
