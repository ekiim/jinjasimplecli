"""Jinja Simple CLI Main Module
In this module we find all the functions needed
to operate this package. 

It is important to remark that this package, doesn't
improves on jinja's functionality, it just allows you to 
call for template "filling" using jinja as it's backbone
from the command line.
"""

import argparse
import json
import importlib.util
import os
import sys

import jinja2 as j

import jinjasimplecli.extensions as je


def main(template_dir, template=None, output=None, data={}, **kwargs):
    """main
    This function, will recieve exactly as many arguments
    as the command line options we expose.

    :param template_dir: Path to where the templates are located.
    :type template_dir: string
    :param template: Template name inside `template dir` or template path.
    :type template: string
    :param output: Where to write the output.
    :type output: stream object 
    :param data: Object with the data to be reference in the templates
    :type data: dictionary
    """
    env = j.Environment(
        loader = j.ChoiceLoader([
            j.FileSystemLoader(template_dir or '.'),
        ])
    )
    load_to_enviroment(env)
    try:
        temp_ref = env.from_string(template)
    except:
        temp_ref = env.from_string(template.read())

    rendered = temp_ref.render(**data)
    output.write(rendered)


def load_json(stream):
    """load_json
    This function recieves the path to a json file and loads it.
    If no file provided or can't find file, it will return an
    empty `dict` object.
    If any errors occure it will raise an `argparse.ArgumentErrorType`
    because this function runs when the argument is first loaded.
    """
    data = {}
    try:
        data = json.loads(stream.read() or '{}')
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
    """load_config
    This function will import the extension file in order to execute and
    reference all the registered functions using the `jinjasimplecli.extensions`
    module.
    """
    spec = importlib.util.spec_from_file_location('user_extensions', filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


def load_to_enviroment(env):
    """load_to_enviroment
    This function reads the global variable `jinjasimplecli.extensions.__custom_functions__`
    and adds it to the `jinja.Enviroment` object.
    """
    for name, function in je.__custom_functions__['filters'].items():
        env.filters[name] = function
