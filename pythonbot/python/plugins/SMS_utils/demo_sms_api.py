#!/usr/bin/env python
# coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


def message_send(sms_code, phone_numbers):
    sign_name = "CN-DOTA"
    template_code = sms_code
    ACCESS_KEY_ID = ""
    ACCESS_KEY_SECRET = ""

    client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone_numbers)
    request.add_query_param('SignName', sign_name)
    request.add_query_param('TemplateCode', template_code)

    response = client.do_action(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))
