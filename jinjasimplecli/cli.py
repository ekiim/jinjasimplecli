"""Command line interface
Here we layout the behaviour for the CLI
"""

import argparse
import io
from pprint import pprint
import sys

import jinjasimplecli.main


def main():
    parser = argparse.ArgumentParser(
        description=('This tool will allow you to compose jinja templates'
                     'in an easy way')
    )
    parser.add_argument('--template-directory', '-t',
                        help=("Path to a directory with jinja templates, "
                        "this templates will be loaded and avalible to reference "
                        "from the template we are providing for the build."
                        ),
                        default=['templates'],
                        action='append',
                        dest="template_dir",
                        nargs='+',
                        metavar="ROOT",
    )
    parser.add_argument('--extensions-file', '--config', '-c',
                        help=("A python file that includes the functions you and"
                              " additional enviroment changes."),
                        default=None,
                        dest="config",
                        type=jinjasimplecli.main.load_config,
                        metavar="CONFIG",
                      )
    parser.add_argument('--json-data', '-j',
                        help=("Json data, this could be a filepath relative"
                        " or absolute, or a stream where the content it's json"
                        " formated."
                        ),
                        dest="data",
                        type=lambda x: jinjasimplecli.main.load_json(argparse.FileType('r')(x)),
                        metavar="DATA",
                        default={}
                        )
    parser.add_argument('--template', '-i',
                        help=("path to the template file you want to build"
                        ", this could be full path, relative to current directory"
                        " or relative to the templates directory if provided."
                        " If this parameter is ommited it will be taken from stdin."
                        ),
                        metavar="INPUT",
                        dest='template',
                        type=argparse.FileType('r'),
                        default=sys.stdin
                        )
    parser.add_argument('-o',
                        help="Where will the rendered template will be outputed",
                        dest="output",
                        metavar="OUTPUT",
                        type=argparse.FileType('w'),
                        default=sys.stdout)
    args = parser.parse_args()
    jinjasimplecli.main.main(**vars(args))


if __name__ == '__main__':
    main()
