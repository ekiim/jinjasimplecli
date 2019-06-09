"""Extensions Example file

"""

import jinjasimplecli.extensions as je

@je.filter('helloworld')
def hello_world(*args):
    return "hello world {}".format(*args)
