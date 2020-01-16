"""
TAC APi tests.

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
import pytest

from fixtures import *
from dirbspy import Core
from dirbspy.exceptions import InvalidArgumentException


def test_tac_get_method(dirbs_mock_server):
    """Verify the tac api get method."""
    core = Core()
    res = core.tac(12345678)

    expected_response = {
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
    assert res == expected_response


def test_tac_post_method(dirbs_mock_server):
    """Verify tac api post method."""
    core = Core()
    res = core.tac([12345678, 12345678])

    expected_response = {
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

    assert res == expected_response


def test_tac_api_validations(dirbs_mock_server):
    """Verify that the tac api do validations."""
    core = Core()

    # if length is less than 8
    with pytest.raises(InvalidArgumentException):
        res = core.tac(1234)

    # if length is greater than 8
    with pytest.raises(InvalidArgumentException):
        res = core.tac(1234567896)

    # if not list in post tac
    with pytest.raises(InvalidArgumentException):
        res = core.tac({'a': 12345678})

    # if list is empty
    with pytest.raises(InvalidArgumentException):
        res = core.tac([])
