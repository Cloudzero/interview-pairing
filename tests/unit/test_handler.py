# -*- coding: utf-8 -*-
# Copyright (c) 2016-present, CloudZero, Inc. All rights reserved.
# Licensed under the BSD-style license. See LICENSE file in the project root for full license information.

import json

import pytest

from pairing import app


@pytest.fixture()
def kinesis_event():
    """ Generates Kinesis Event"""

    return {
    }


@pytest.mark.unit
def test_handler(kinesis_event, mocker):

    ret = app.handler(kinesis_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world"
    # assert "location" in data.dict_keys()
