"""Extensions Example file

"""

import requests

import jinjasimplecli.extensions as je

@je.filter('helloworld')
def hello_world(*args):
    return "hello world {}".format(*args)


@je.filter('issue')
def hello_world(issue_number):
    url = f"https://api.github.com/repos/ekiim/jinjasimplecli/issues/{issue_number}"
    data = requests.get(url).json()
    return f"Issue - {data['number']} - {data['title']}"
