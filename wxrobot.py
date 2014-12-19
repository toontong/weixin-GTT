#coding:utf8

__all__ = ['register_handler']


from werobot import WeRoBot


def register_handler(robot):
    assert isinstance(robot, WeRoBot), 'must instance of WeRoBot()'


    robot.add_handler(echo, type="text")
    robot.add_handler(all_handler, type="all")


def echo(msg):
    print "get Msg:", msg.content
    return "I Got [%s]" % msg.content


def all_handler(msg):
    print "Location:", msg.raw
    return "I Got event"
