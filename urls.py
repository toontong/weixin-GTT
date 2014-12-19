#codig:utf8
import os, sys
from bottle import Bottle
from bottle import static_file


__all__ = ["register_urls"]

import api

GET = "GET"
POST = "POST"
PUT = "PUT"
DElETE = "DELETE"

dir = os.path.dirname(__file__)
html_root = os.path.join(dir, "static", "html")
static_root = os.path.join(dir, "static")

def _static_file(typ, filename):
    print typ, filename
    return static_file(os.path.join(typ, filename), static_file)

def _html_file(filename):
    print filename
    return static_file(filename, root=html_root)

URLS = (
    ([GET, POST, DElETE], "/api", api.API()),

    # static:
    (GET, "/weixin/<filename:path>", _html_file),
    (GET, "/static/<typ>/<filename:*.[js$|css$|.png$|.jpg$]>", _static_file),
)


def register_urls(app):
    assert isinstance(app, Bottle), "must class Bottle() instance."

    global URLS

    for method, path, callback in URLS:
        app.route(path, method, callback)
