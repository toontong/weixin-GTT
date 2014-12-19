#coding:utf8

import os, sys
dir = os.path.dirname(__file__)
sys.path.append(os.path.join(dir, "deps"))

import config
import menu
import urls
import wxrobot

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

        wxrobot.register_handler(robot)

        robot.run(server='tornado', host="0.0.0.0", port=80,
                  url=cfg['wiexin']["ServerUrl"])
    except KeyboardInterrupt:
        print "exit"


if __name__ == "__main__":


    cfg = config.parseConfig(tomlFile=os.path.join(dir, "cfg.toml"))

    if "create_menu" in sys.argv:
        print create_menu(cfg)
        print get_menu(cfg)
    elif "get_menu"  in sys.argv:
        print get_menu(cfg)
    else:

        main(cfg)
