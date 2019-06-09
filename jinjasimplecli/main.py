"""
"""

import json
import importlib.util
import os
import sys


import jinja2 as j

import jinjasimplecli.extensions as je

def main(template_dir, template=None, output=None, data={}):
    env = j.Environment(
        loader = j.ChoiceLoader([
            j.FileSystemLoader(template_dir),
            j.PrefixLoader({ 'content': j.FileSystemLoader('./content')})
        ])
    )
    load_to_enviroment(env)
    temp_ref = env.from_string(template.read())
    rendered = temp_ref.render(**data)
    output.write(rendered)


def load_json(filename=None):
    data = {}
    try:
        with open(filename) as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        raise argparse.ArgumentTypeError('Error Decoding JSON file')
    except OSError:
        raise argparse.ArgumentTypeError("Can' open file")
    except TypeError:
        pass
    except:
        raise argparse.ArgumentTypeError(
            'Unkwon error occur while attempting to open JSON file')
    return data


def load_config(filename):
    spec = importlib.util.spec_from_file_location('user_extensions', filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)



def load_to_enviroment(env):
    for name, function in je.__custom_functions__['filters'].items():
        env.filters[name] = function

if __name__ == '__main__':
    pass
