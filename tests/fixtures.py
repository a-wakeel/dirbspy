"""
Fixtures modules for tests.

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
import re
import json
import pytest
import httpretty

responses = {
    'tac_get': {
            "gsma": {
                "allocation_date": "string",
                "bands": "string",
                "bluetooth": "string",
                "brand_name": "string",
                "country_code": "string",
                "device_type": "string",
                "fixed_code": "string",
                "imeiquantitysupport": "string",
                "internal_model_name": "string",
                "manufacturer": "string",
                "marketing_name": "string",
                "model_name": "string",
                "nfc": "string",
                "nonremovable_euicc": "string",
                "nonremovable_uicc": "string",
                "operating_system": "string",
                "radio_interface": "string",
                "removable_euicc": "string",
                "removable_uicc": "string",
                "simslot": "string",
                "wlan": "string"
            },
            "tac": "string"
        },
    'tac_post': {
        "results": [
            {
                "gsma": {
                    "allocation_date": "string",
                    "bands": "string",
                    "bluetooth": "string",
                    "brand_name": "string",
                    "country_code": "string",
                    "device_type": "string",
                    "fixed_code": "string",
                    "imeiquantitysupport": "string",
                    "internal_model_name": "string",
                    "manufacturer": "string",
                    "marketing_name": "string",
                    "model_name": "string",
                    "nfc": "string",
                    "nonremovable_euicc": "string",
                    "nonremovable_uicc": "string",
                    "operating_system": "string",
                    "radio_interface": "string",
                    "removable_euicc": "string",
                    "removable_uicc": "string",
                    "simslot": "string",
                    "wlan": "string"
                },
                "tac": "string"
            }
        ]
    }
}


@pytest.yield_fixture(scope='session')
def dirbs_mock_server():
    """MOCK server fixture for DIRBS."""
    httpretty.enable()

    # DIRBS TAC GET API mock
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r'http://localhost:5000/api/v2/tac/\d'),
        body=json.dumps(responses.get('tac_get')),
        content_type='application/json'
    )

    # DIRBS TAC POST API mock
    httpretty.register_uri(
        httpretty.POST,
        'http://localhost:5000/api/v2/tac',
        body=json.dumps(responses.get('tac_post')),
        content_type='application/json'
    )

    yield
    httpretty.disable()
    httpretty.reset()
