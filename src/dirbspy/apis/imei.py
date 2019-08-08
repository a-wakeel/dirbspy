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
import requests


class IMEI:
    """Implements core imei apis."""

    def __init__(self, conn_str, api_version, imei, include_paired_with=False, include_seen_with=False):
        """Constructor."""
        self.conn_str = conn_str
        self.api_version = api_version
        self.imei = imei
        self.include_paired = include_paired_with
        self.include_seen = include_seen_with

    def get_response(self):
        """Send request and get response back."""
        return requests.get('{conn}/api/{version}/imei/{imei_str}?'
                            'include_paired_with={paired}&'
                            'include_seen_with={seen}'.format(
                                                            conn=self.conn_str,
                                                            version=self.api_version,
                                                            imei_str=self.imei,
                                                            paired=self.include_paired,
                                                            seen=self.include_seen)).json()
