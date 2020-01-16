"""
dirbspy core tac api module.

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

class TAC:
    """Implements core TAC apis."""

    def __init__(self, conn_str, api_version):
        """Constructor."""
        self.conn_str = conn_str
        self.api_version = api_version

    def get(self, tac):
        """TAC Api get method."""
        if len(tac) == 8:
            return requests.get(
                '{conn_str}/api/{ver}/tac/{tac}'.format(
                    conn_str=self.conn_str,
                    ver = self.api_version,
                    tac = tac
                )
            ).json()
        raise InvalidArgumentException('TAC length must be 8 digits')

    def post(self, tacs):
        """TAC api post method for batch TACs."""
        if not isinstance(tacs, list):
            raise InvalidArgumentException('list of tacs is expected')
        elif len(tacs) == 0:
            raise InvalidArgumentException('list should contain at-least one TAC')
        else:
            return requests.post('{conn_str}/api/{ver}/tac'.format(
                conn_str=self.conn_str,
                ver = self.api_version
            ), data=json.dumps(tacs)).json()

