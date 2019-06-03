# -*- coding: utf-8 -*-
# Copyright (c) 2016-present, CloudZero, Inc. All rights reserved.
# Licensed under the BSD-style license. See LICENSE file in the project root for full license information.

# import base64

import simplejson as json


def handler(event, context):
    """CloudTrail Analytics Handler

    Parameters
    ----------
    event: dict, required
        Kinesis Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    Kinesis Processor Output Format: dict
    """

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
