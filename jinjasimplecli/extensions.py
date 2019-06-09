"""Extensions
Here we lay out the functions that we expose to the users to use
as wrappers for functions and classes that will be exposed to the
user.
"""

__custom_functions__ = { 'filters': {}}

def filter(name=None):

    def registration(f):
        __custom_functions__['filters'][name or f.__name__] = f
        return f

    return registration
