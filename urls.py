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

def static_file(type, filename):
    return static_file(os.path.join(type, filename), root=static_file)

def html_file(filename):
    return static_file(filename, root=html_root)

URLS = (
    ([GET, POST, DElETE], "/api", api.API()),

    # static:
    (GET, "/weixin/<filename:path", html_file),
    (GET, "/static/<typ>/<filename:*.[js$|css$|.png$|.jpg$]>", static_file),
)


def register_urls(app):
    assert isinstance(app, Bottle), "must class Bottle() instance."

    global URLS

    for method, path, callback in URLS:
        app.route(path, method, callback)
