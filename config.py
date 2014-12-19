#coding:utf-8

import toml

def parseConfig(tomlFile):
    '''return dict'''
    with open(tomlFile) as conffile:
        config = toml.loads(conffile.read())
        return config

if __name__ == "__main__":
    d = parseConfig("./cfg.toml")
    assert isinstance(d, dict), type(d)
    print d
