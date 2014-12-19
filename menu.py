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
                    "url":"http://{serverDomain}/reg/create",
                    "sub_button": [ ]
                },
                {
                    "type": "view",
                    "name": "List",
                    "key": "reg_list",
                    "url":"http://{serverDomain}/reg/list",
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
                    "url":"http://{serverDomain}/trip/list",
                   "sub_button": [ ]
                 },
                {
                    "type": "view",
                    "name": "List",
                    "key": "trip_list",
                    "url":"http://{serverDomain}/trip/list",
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
