#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
=================================================
tiehu parking Class Library
-------------------------------------------------
作者：[郭磊]
手机：[15210720528]
Email：[174000902@qq.com]
Github：https://github.com/guolei19850528/guolei_py3_tiehu
=================================================
"""
import hashlib
from datetime import datetime
from typing import Iterable, Callable

from addict import Dict
from guolei_py3_requests import RequestsResponseCallable, requests_request
from requests import Response


class RequestsResponseCallable(RequestsResponseCallable):
    @staticmethod
    def status_code_200_json_addict_status_1(response: Response = None):
        json_addict = RequestsResponseCallable.status_code_200_json_addict(response=response)
        return json_addict.status == 1 or json_addict.status == "1"

    @staticmethod
    def status_code_200_json_addict_status_1_data(response: Response = None):
        print(response.json())
        if RequestsResponseCallable.status_code_200_json_addict_status_1(response=response):
            return RequestsResponseCallable.status_code_200_json_addict(response=response).Data
        return Dict({})


class Api(object):
    def __init__(
            self,
            base_url: str = "",
            parking_id: str = "",
            app_key: str = "",
    ):
        self._base_url = base_url
        self._parking_id = parking_id
        self._app_key = app_key

    @property
    def base_url(self):
        return self._base_url[:-1] if self._base_url.endswith("/") else self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value

    @property
    def app_key(self):
        return self._app_key

    @app_key.setter
    def app_key(self, value):
        self._app_key = value

    def timestamp(self):
        return int(datetime.now().timestamp() * 1000)

    def app_key_md5_upper(self):
        return hashlib.md5(self.app_key.encode('utf-8')).hexdigest().upper()

    def signature(
            self,
            data: dict = {},
    ):
        sign_temp = ""
        data = Dict(data)
        if data.keys():
            data_sorted = sorted(data.keys())
            if isinstance(data_sorted, list):
                sign_temp = "&".join([f"{i}={data[i]}" for i in
                                      data_sorted if
                                      i != "appKey"]) + f"{hashlib.md5(self.app_key.encode('utf-8')).hexdigest().upper()}"
        return hashlib.md5(sign_temp.encode('utf-8')).hexdigest().upper()

    def query_pklot(
            self,
            request_request_json: dict = {},
            requests_response_callable: Callable = RequestsResponseCallable.status_code_200_json_addict_status_1_data,
            requests_request_args: Iterable = tuple(),
            requests_request_kwargs: dict = {},
    ):
        """
        获取车场信息

        @see https://www.showdoc.com.cn/1735808258920310/8101548494440115
        :param request_request_json:
        :param requests_response_callable:
        :param requests_request_args:
        :param requests_request_kwargs:
        :return:
        """
        request_request_json = Dict(request_request_json)
        requests_request_kwargs = Dict(requests_request_kwargs)
        requests_request_kwargs = Dict({
            "url": f"{self.base_url}/cxzn/interface/queryPklot",
            "method": "POST",
            "json": {
                **request_request_json,
                **requests_request_kwargs.json,
                # "sign":self.signature(data=request_request_json),
            },
            **requests_request_kwargs,
        })
        requests_request_kwargs.json.sign = self.signature(data=request_request_json)
        return requests_request(
            requests_response_callable=requests_response_callable,
            requests_request_args=requests_request_args,
            requests_request_kwargs=requests_request_kwargs
        )

    def pay_monthly(
            self,
            request_request_json: dict = {},
            requests_response_callable: Callable = RequestsResponseCallable.status_code_200_json_addict_status_1,
            requests_request_args: Iterable = tuple(),
            requests_request_kwargs: dict = {},
    ):
        """
        月卡续期

        @see https://www.showdoc.com.cn/1735808258920310/10765088021068182
        :param request_request_json:
        :param requests_response_callable:
        :param requests_request_args:
        :param requests_request_kwargs:
        :return:
        """
        request_request_json = Dict(request_request_json)
        requests_request_kwargs = Dict(requests_request_kwargs)
        requests_request_kwargs = Dict({
            "url": f"{self.base_url}/cxzn/interface/payMonthly",
            "method": "POST",
            "json": {
                **request_request_json,
                **requests_request_kwargs.json,
            },
            **requests_request_kwargs,
        })
        requests_request_kwargs.json.sign = self.signature(data=request_request_json)
        return requests_request(
            requests_response_callable=requests_response_callable,
            requests_request_args=requests_request_args,
            requests_request_kwargs=requests_request_kwargs
        )

    def get_monthly_rent(
            self,
            request_request_json: dict = {},
            requests_response_callable: Callable = RequestsResponseCallable.status_code_200_json_addict_status_1_data,
            requests_request_args: Iterable = tuple(),
            requests_request_kwargs: dict = {},
    ):
        """
        用于获取月租信息

        @see https://www.showdoc.com.cn/1735808258920310/8140245610945503
        :param request_request_json:
        :param requests_response_callable:
        :param requests_request_args:
        :param requests_request_kwargs:
        :return:
        """
        request_request_json = Dict(request_request_json)
        requests_request_kwargs = Dict(requests_request_kwargs)
        requests_request_kwargs = Dict({
            "url": f"{self.base_url}/cxzn/interface/getMonthlyRent",
            "method": "POST",
            "json": {
                **request_request_json,
                **requests_request_kwargs.json,
            },
            **requests_request_kwargs,
        })
        requests_request_kwargs.json.sign = self.signature(data=request_request_json)
        return requests_request(
            requests_response_callable=requests_response_callable,
            requests_request_args=requests_request_args,
            requests_request_kwargs=requests_request_kwargs
        )

    def del_monthly_rent(
            self,
            request_request_json: dict = {},
            requests_response_callable: Callable = RequestsResponseCallable.status_code_200_json_addict_status_1,
            requests_request_args: Iterable = tuple(),
            requests_request_kwargs: dict = {},
    ):
        """
        用于删除月租信息

        @see https://www.showdoc.com.cn/1735808258920310/8139961106723173
        :param request_request_json:
        :param requests_response_callable:
        :param requests_request_args:
        :param requests_request_kwargs:
        :return:
        """
        request_request_json = Dict(request_request_json)
        requests_request_kwargs = Dict(requests_request_kwargs)
        requests_request_kwargs = Dict({
            "url": f"{self.base_url}/cxzn/interface/delMonthlyRent",
            "method": "POST",
            "json": {
                **request_request_json,
                **requests_request_kwargs.json,
            },
            **requests_request_kwargs,
        })
        requests_request_kwargs.json.sign = self.signature(data=request_request_json)
        return requests_request(
            requests_response_callable=requests_response_callable,
            requests_request_args=requests_request_args,
            requests_request_kwargs=requests_request_kwargs
        )

    def save_monthly_rent(
            self,
            request_request_json: dict = {},
            requests_response_callable: Callable = RequestsResponseCallable.status_code_200_json_addict_status_1,
            requests_request_args: Iterable = tuple(),
            requests_request_kwargs: dict = {},
    ):
        """
        用于对车场月租车信息增加或修改

        @see https://www.showdoc.com.cn/1735808258920310/8137812760676532
        :param request_request_json:
        :param requests_response_callable:
        :param requests_request_args:
        :param requests_request_kwargs:
        :return:
        """
        request_request_json = Dict(request_request_json)
        requests_request_kwargs = Dict(requests_request_kwargs)
        requests_request_kwargs = Dict({
            "url": f"{self.base_url}/cxzn/interface/saveMonthlyRent",
            "method": "POST",
            "json": {
                **request_request_json,
                **requests_request_kwargs.json,
            },
            **requests_request_kwargs,
        })
        requests_request_kwargs.json.sign = self.signature(data=request_request_json)
        return requests_request(
            requests_response_callable=requests_response_callable,
            requests_request_args=requests_request_args,
            requests_request_kwargs=requests_request_kwargs
        )

    def get_monthly_rent_list(
            self,
            request_request_json: dict = {},
            requests_response_callable: Callable = RequestsResponseCallable.status_code_200_json_addict_status_1_data,
            requests_request_args: Iterable = tuple(),
            requests_request_kwargs: dict = {},
    ):
        """
        用于根据车场ID获取所以月卡车

        @see https://www.showdoc.com.cn/1735808258920310/8140994456347800
        :param request_request_json:
        :param requests_response_callable:
        :param requests_request_args:
        :param requests_request_kwargs:
        :return:
        """
        request_request_json = Dict(request_request_json)
        requests_request_kwargs = Dict(requests_request_kwargs)
        requests_request_kwargs = Dict({
            "url": f"{self.base_url}/cxzn/interface/getMonthlyRentList",
            "method": "POST",
            "json": {
                **request_request_json,
                **requests_request_kwargs.json,
            },
            **requests_request_kwargs,
        })
        requests_request_kwargs.json.sign = self.signature(data=request_request_json)
        return requests_request(
            requests_response_callable=requests_response_callable,
            requests_request_args=requests_request_args,
            requests_request_kwargs=requests_request_kwargs
        )

    def del_monthly_rent_list(
            self,
            request_request_json: dict = {},
            requests_response_callable: Callable = RequestsResponseCallable.status_code_200_json_addict_status_1,
            requests_request_args: Iterable = tuple(),
            requests_request_kwargs: dict = {},
    ):
        """
        批量删除月租

        https://www.showdoc.com.cn/1735808258920310/8213900511212297
        :param request_request_json:
        :param requests_response_callable:
        :param requests_request_args:
        :param requests_request_kwargs:
        :return:
        """
        request_request_json = Dict(request_request_json)
        requests_request_kwargs = Dict(requests_request_kwargs)
        requests_request_kwargs = Dict({
            "url": f"{self.base_url}/cxzn/interface/delMonthlyRentList",
            "method": "POST",
            "json": {
                **request_request_json,
                **requests_request_kwargs.json,
            },
            **requests_request_kwargs,
        })
        requests_request_kwargs.json.sign = self.signature(data=request_request_json)
        return requests_request(
            requests_response_callable=requests_response_callable,
            requests_request_args=requests_request_args,
            requests_request_kwargs=requests_request_kwargs
        )

    def get_parkinfo(
            self,
            request_request_json: dict = {},
            requests_response_callable: Callable = RequestsResponseCallable.status_code_200_json_addict_status_1_data,
            requests_request_args: Iterable = tuple(),
            requests_request_kwargs: dict = {},
    ):
        request_request_json = Dict(request_request_json)
        requests_request_kwargs = Dict(requests_request_kwargs)
        requests_request_kwargs = Dict({
            "url": f"{self.base_url}/cxzn/interface/getParkinfo",
            "method": "POST",
            "json": {
                **request_request_json,
                **requests_request_kwargs.json,
            },
            **requests_request_kwargs,
        })
        requests_request_kwargs.json.sign = self.signature(data=request_request_json)
        return requests_request(
            requests_response_callable=requests_response_callable,
            requests_request_args=requests_request_args,
            requests_request_kwargs=requests_request_kwargs
        )
