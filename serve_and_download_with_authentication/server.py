# Alexandros I. Metsai
# alexmetsai@gmail.com

from functools import partial
from http.server import SimpleHTTPRequestHandler#, test
import base64
import os


class AuthHTTPRequestHandler(SimpleHTTPRequestHandler):
    """ Main class to present webpages and authentication. """

    def __init__(self, *args, **kwargs):
        username = kwargs.pop("username")
        password = kwargs.pop("password")
        self._auth = base64.b64encode(f"{username}:{password}".encode()).decode()
        super().__init__(*args)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Test"')
        self.send_header("Content-type", "text/html")
        self.end_headers()
