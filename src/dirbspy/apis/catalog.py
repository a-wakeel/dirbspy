"""
dirbspy core catalog api module.

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

from dirbspy.exceptions import InvalidArgumentException

class CATALOG:
    """Implements core catalog apis."""

    def __init__(self, conn_str, api_version, file_type, modified_since, cataloged_since, is_valid_zip=False,
                 order='ASC', offset=0, limit=10):
        """Constructor."""
        self.conn_str = conn_str
        self.api_version = api_version
        self.is_valid_zip = is_valid_zip
        self.modified_since = modified_since
        self.cataloged_since = cataloged_since
        self.offset = offset
        self.limit = limit

        # TODO: add more validation checks on args

        if order and order not in ['ASC', 'DESC']:
            raise InvalidArgumentException('order should be one of (ASC, DESC)')
        else:
            self.order = order

        if file_type and file_type not in ['operator', 'gsma_tac', 'stolen_list',
                             'pairing_list', 'registration_list', 'golden_list']:
            raise InvalidArgumentException('file type should be one of '
                                           '(operator, gsma_tac, stolen_list, '
                                           'pairing_list, registration_list, golden_list)')
        else:
            self.file_type = file_type

    def get_response(self):
        """Return api response back."""
        requests.get(
            '{conn_str}/api/{ver}/catalog?is_valid_zip={valid_zip}'
            '&modified_since={modified_date}&cataloged_since={catalog_date}&'
            'file_type={file_type}&offset={offset}&limit={limit}&order={order}'.format(
                conn_str=self.conn_str,
                ver=self.api_version,
                valid_zip=self.is_valid_zip,
                modified_date=self.modified_since,
                catalog_date=self.cataloged_since,
                file_type=self.file_type,
                offset=self.offset,
                limit=self.limit,
                order=self.order
            )
        ).json()

