"""
dirbspy exceptions module.

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


class DIRBSPyException(Exception):
    """Exception to raise when DIRBS returns a non-ok http status code."""

class InvalidArgumentException(DIRBSPyException):
    """Exception to raise when arguments supplied are not expected ones."""


class HTTPError(DIRBSPyException):
    """Exception raise when DIRBS returns a non-ok http status code."""

    @property
    def status_code(self):
        """Http status code of the error."""
        return self.args[0]

    @property
    def error_message(self):
        """A string error message."""
        return self.args[1]

    @property
    def error_info(self):
        """dict of returned error from DIRBS."""
        return self.args[2]


class ConnError(HTTPError):
    """Error raised when there was an exception when talking to DIRBS."""


class SSLError(ConnError):
    """Error raised when encountering ssl errors."""


class ConnTimeoutError(ConnError):
    """Raised when a network timeout encountered."""


class NotFoundError(HTTPError):
    """Raised when a 404 error encountered."""


class RequestError(HTTPError):
    """Raised when a 400 error encountered."""
