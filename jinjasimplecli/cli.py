"""Command line interface
Here we layout the behaviour for the CLI

"""

import argparse
import sys

import jinjasimplecli.main

def main():
    parser = argparse.ArgumentParser(
        description=('This tool will allow you to compose jinja templates'
                     'in an easy way')
    )
    parser.add_argument('--template-directory', '-t',
                        help="Path to templates directory",
                        default='template',
                        dest="template_dir",
                        metavar="TemplatesDirectory",
                        nargs="?")
    parser.add_argument('--json-data', '-j',
                        help="Json data file, to fill the template variables",
                        default={},
                        dest="data",
                        type=jinjasimplecli.main.load_json,
                        metavar="DATAFILE"
                        )
    parser.add_argument('--extensions-file', '--config',
                        help=("A python file that includes the functions you and"
                              " additional enviroment changes."),
                        default=None,
                        dest="data",
                        type=jinjasimplecli.main.load_config,
                        metavar="CONFIGFILE"
                      )
    parser.add_argument('template', 
                        help="Path to template you want to build/compose",
                        nargs='?', 
                        metavar="TargetTemplate",
                        type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('-o',
                        help="Where will the rendered template will be outputed",
                        nargs='?', 
                        dest="output",
                        metavar="OUTPUT",
                        type=argparse.FileType('w'),
                        default=sys.stdout)
    jinjasimplecli.main.main(**vars(parser.parse_args()))

if __name__ == '__main__':
    main()
