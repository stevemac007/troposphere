# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSHelperFn, Ref
from .validators import integer


class Stack(AWSObject):
    type = "AWS::CloudFormation::Stack"

    props = {
        'TemplateURL': (basestring, True),
        'TimeoutInMinutes': (integer, False),
        'Parameters': (dict, False),
    }


class WaitCondition(AWSObject):
    type = "AWS::CloudFormation::WaitCondition"

    props = {
        'Count': (integer, False),
        'Handle': (Ref, True),
        'Timeout': (integer, True),
    }


class WaitConditionHandle(AWSObject):
    type = "AWS::CloudFormation::WaitConditionHandle"

    props = {}

class Init(AWSHelperFn):
    def __init__(self, data):
        self.data = { "AWS::CloudFormation::Init" : data}

    def JSONrepr(self):
        return self.data
