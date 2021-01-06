#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests, json

class Request:
    def __init__(self,url):
        """
        传入url,初始化对象
        :param url: 请求接口地址
        """
        self.url = url
    def getStatusName(self):
        """
        请求接口，得到返回的状态
        :return:
        """
        se = requests.session()
        res = se.get(self.url).text.replace("'", '"').replace('/ ', '/')
        j = json.loads(res)
        return j.get("jobs")[0].get("state")
