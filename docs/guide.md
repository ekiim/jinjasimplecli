# Jinja Simple CLI Examples

Making reference to the files under this directory, we illustrate the following examples. 

With this examples I hope you can understand how to use it.

*NOTE*: This is not the final version for the documentation.

## Filling Variables in a template

In this example the json (`examples/data/externalword.json`) file only contains one key, and the template (`examples/data/one-variable.txt`) only
uses the variable `externalword`.

```
$ jinja-cli -t examples/templates/ -j examples/data/externalword.json examples/templates/one-variable.txt
In this document we only have one
variable to fill and this will be

This one: Cool title
```

If we modify the example a little we can do more complex things like
```
$ cat examples/templates/one-variable.txt | \
	jinja-cli -t examples/templates/ \
              -j <(echo '{"externalword": "Not a cool title"}')
In this document we only have one
variable to fill and this will be

This one: Not a cool title
```

Which is practically the same thing, except the sources for the data file and template file are expressed differently allowing you to use in more complicated bash scripts.

## Template Inheritance

Using template inheritance as jinja's documentation instructs taking in to account that the path of the templates you include should be relative to `template directory` provided.

```
$ jinja-cli -t examples/templates/ examples/templates/parent.txt
Parent Template

No inheritance applied
```

```
$ jinja-cli -t examples/templates/ examples/templates/child.txt
Parent Template

I'm a child block
```

## Including custom filters

If you want to write your own filters, you could write a python file and import `jinjasimplecli.extensions` and write a filter like the following. 

```python3
# examples/extensions.py
import jinjasimplecli.extensions as je

@je.filter('helloworld')
def hello_world(*args):
    return "hello world {}".format(*args)
```

The decorator recives as parameter the name for the filter when used from a template, if non provided the name for it, is the same as the functions `__name__`.

Once we have this file, we can run the following command

```
$ jinja-cli -t examples/templates/ -c examples/extensions.py examples/templates/extensions.txt
Filter Example
hello world 42
```
