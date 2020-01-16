"""
dirbspy core client module.

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
from dirbspy.exceptions import InvalidArgumentException
from dirbspy.apis import *


class Core(object):
    """Http client implementation for DIRBS Core."""

    def __init__(self, host='localhost', port=5000, use_ssl=False, api_version='v2'):
        """
        Constructor.
        We take http://localhost:5000 as default parameters.
        """
        self._host = host
        self._port = port
        self.use_ssl = use_ssl
        self.api_version = api_version

    @property
    def host(self):
        """Returns current host address."""
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def conn_str(self):
        """Returns complete connection string."""
        proto = 'https://' if self.use_ssl else 'http://'
        return '{0}{1}:{2}'.format(proto, self.host, self.port)

    def version(self):
        """Calls core version api."""
        return Version(self.conn_str, self.api_version).get_response()

    def imei(self, imei):
        """Calls core imei_api."""
        return IMEI(self.conn_str, self.api_version, imei).get_response()

    def msisdn(self, msisdn):
        """Calls msisdn api."""
        return MSISDN(self.conn_str, self.api_version, msisdn).get_response()

    def tac(self, tacs):
        """Calls tac apis."""
        if isinstance(tacs, int):
            return TAC(self.conn_str, self.api_version).get(str(tacs))
        elif isinstance(tacs, list):
            return TAC(self.conn_str, self.api_version).post(tacs)
        else:
            raise InvalidArgumentException('Invalid argument type: {type} expected types are: int, list'.format(
                type=type(tacs)))