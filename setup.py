"""setup.py
"""
from setuptools import setup

def load_from_file(filename):
    with open(filename) as f:
        returnable = f.read()
    return returnable

setup(
    name = "jinjasimplecli",
    version = "1.0.0",
    author = "Miguel Salgado",
    author_email = "me@ekiim.xyz",
    description = ("Jinja Simple CLI, is a tool that allows you to compose"
                   " and insert data in to templates, with support for "
                   "template inheritance and global functions. It uses "
                   "json files as input for the data, and it can handle "
                   "templates from standard input."),
    long_description=load_from_file('README.md'),
    long_description_content_type="text/markdown",
    license = "BSD",
    keywords = "jinja templates cli",
    url = "https://github.com/ekiim/jinjasimplecli",
    packages=['jinjasimplecli'],
    entry_points={
        'console_scripts': [
            'jinja-cli = jinjasimplecli.cli:main',
        ]
    },
    install_requires=[
          'jinja2',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing",
    ],
)

