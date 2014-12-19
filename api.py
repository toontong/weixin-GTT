#coding:utf8

from bottle import request, response, abort, template


class API():

    def __call__(self):
        if request.method == "GET":
            return self.get()
        elif request.method == "POST":
            return self.post()
        elif request.method == "DELETE":
            return self.delete()

    def get(self):
        print request

    def post(self):
        print 'post'

    def delete(self):
        print 'delete'
