"""setup.py
"""
from setuptools import setup

def load_from_file(filename):
    with open(filename) as f:
        returnable = f.read()
    return returnable

setup(
    name = "jinjasimplecli",
    version = "0.0.1",
    author = "Miguel Salgado",
    author_email = "projects@ekiim.xyz",
    description = ("Jinja Simple CLI, is a tool that allows you to compose"
                   " and insert data in to templates, with support for "
                   "template inheritance and global functions. It uses "
                   "json files as input for the data, and it can handle "
                   "templates from standard input."),
    long_description=load_from_file('README.md'),
    license = "BSD",
    keywords = "jinja templates cli",
    url = "https://github.com/ekiim/jinjasimplecli",
    packages=['jinjasimplecli'],
    entry_points={
        'console_scripts': [
            'jinja-cli = jinjasimplecli.cli:main',
        ]
    }
)

