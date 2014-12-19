#coding: utf-8

import json

__all__ = ['GetMenuJson']

def getMenuJson(serverDomain, languageCN=True):
    language = {"Regist":"登记",
                "New":"新增",
                "List":"列表",
                "Plan of Trip":"差旅计划",
                "Help":"帮助"}

    menu = {
    "button": [
        {
            "name": "Regist",
            "sub_button": [
                {
                    "type": "view",
                    "name": "New",
                    "key": "reg_create",
                    "url":"http://{serverDomain}/weixin/reg_create.html",
                    "sub_button": [ ]
                },
                {
                    "type": "view",
                    "name": "List",
                    "key": "reg_list",
                    "url":"http://{serverDomain}/weixin/reg_list.html",
                    "sub_button": [ ]
                }
            ]
        },
        {
            "name": "Plan of Trip",
            "sub_button": [
                {
                    "type": "view",
                    "name": "New",
                    "key": "trip_create",
                    "url":"http://{serverDomain}/weixin/trip_create.html",
                   "sub_button": [ ]
                 },
                {
                    "type": "view",
                    "name": "List",
                    "key": "trip_list",
                    "url":"http://{serverDomain}/weixin/trip_list.html",
                    "sub_button": [ ]
                }
            ]
        },
        {
            "name": "Help",
            "type": "location_select",
            "key": "help_of_location"
        }
    ]
}
    js = json.dumps(menu).replace("{serverDomain}", serverDomain).encode("utf8")
    if languageCN:
        for k, v in language.iteritems():
            js = js.replace(k, v)
    return js

if __name__ == "__main__":
    print getMenuJson("test.com")
