"""
"""

import json
import os
import sys

import jinja2 as j

#def load_global_functions(env, functions={}):
#    env.global.update(**functions)

def main(template_dir, template=None, output=None, data={}):
    env = j.Environment(
        loader = j.ChoiceLoader([
            j.FileSystemLoader(template_dir),
            j.PrefixLoader({ 'content': j.FileSystemLoader('./content')})
        ])
    )
    #    load_global_functions(env, functions)
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

if __name__ == '__main__':
    pass
