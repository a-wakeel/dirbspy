"""
dirbspy core imei api module.

MIT License

Copyright (c) 2019 Abdul Wakeel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import json
import requests

from dirbspy.exceptions import InvalidArgumentException


class IMEI:
    """Implements core imei apis."""

    def __init__(self, conn_str, api_version):
        """Constructor."""
        self.conn_str = conn_str
        self.api_version = api_version

    def get_imei(self, imei, include_registration_status=False, include_stolen_status=False):
        """Handles IMEI GET API."""
        return requests.get('{conn_str}/api/{version}/imei/{imei}?'
                            'include_registration_status={reg_status}&'
                            'include_stolen_status={stolen_status}'.format(
                                conn_str=self.conn_str,
                                version=self.api_version,
                                imei=imei,
                                reg_status=include_registration_status,
                                stolen_status=include_stolen_status
                            ))

    def get_imeis(self, imeis, include_registration_status=False, include_stolen_status=False):
        """Handles IMEI POST API."""
        if not isinstance(imeis, list):
            raise InvalidArgumentException('invalid argument type \'imeis\', must be a list of strings')

        if len(imeis) == 0:
            raise InvalidArgumentException('invalid argument length, \'imeis\' can not be empty')

        payload = {'imeis': imeis,
                   'include_registration_status': include_registration_status,
                   'include_stolen_status': include_stolen_status}

        return requests.post('{conn_str}/api/{version}/imei-batch'.format(
            conn_str=self.conn_str,
            version=self.api_version),
            data=json.dumps(payload)).json()

    def get_imei_info(self, imei):
        """Handles IMEI INFO API."""
        return requests.get('{conn_str}/api/{version}/imei/{imei}/info'.format(
            conn_str=self.conn_str,
            version=self.api_version,
            imei=imei
        )).json()

    def get_imei_subscribers(self, imei):
        """Handles IMEI Subscribers API."""
        return requests.get('{conn_str}/api/{version}/imei/{imei}/subscribers'.format(
            conn_str=self.conn_str,
            version=self.api_version,
            imei=imei
        )).json()

    def get_imei_pairings(self, imei):
        """Handles IMEI pairings api."""
        return requests.get('{conn_str}/api/{version}/imei/{imei}/pairings'.format(
            conn_str=self.conn_str,
            version=self.api_version,
            imei=imei
        )).json()
