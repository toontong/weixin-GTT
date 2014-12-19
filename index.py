#coding:utf8

import os, sys
dir = os.path.dirname(__file__)
sys.path.append(os.path.join(dir, "deps"))

import config
import menu
import urls

import werobot
from werobot.client import Client as mpClient





def _mpClient(cfg):
    mpCli = mpClient(cfg["wiexin"]["AppID"],
                     cfg["wiexin"]["AppSecret"],)
    return mpCli

def create_menu(cfg):
    mpCli = _mpClient(cfg)
    menu_data = menu.getMenuJson(cfg["ServerDomain"])
    return mpCli.create_menu(menu_data)


def get_menu(cfg):
    mpCli = _mpClient(cfg)
    return mpCli.get_menu()


def main(cfg):
    try:
        robot = werobot.WeRoBot(cfg['wiexin']['Token'])

        urls.register_urls(robot.app)

        @robot.handler
        def echo(message):
            print "get Msg:", message.content
            return message

        @robot.location
        def location(msg):
            print "Location:", msg.location, msg.scale, msg.label

        robot.run(server='tornado', host="0.0.0.0", port=80,
                  url=cfg['wiexin']["ServerUrl"])
    except KeyboardInterrupt:
        print "exit"


if __name__ == "__main__":


    cfg = config.parseConfig(tomlFile=os.path.join(dir, "cfg.toml"))

    if "create_memu" in sys.argv:
        create_menu(cfg)
    elif "get_menu"  in sys.argv:
        get_menu(cfg)
    else:
        main(cfg)
