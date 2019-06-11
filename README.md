# Jinja Simple CLI

This project offers a way to easily compose templates directly from the 
command line, ideal to use in junction with other cli utilities.

You could check the examples under the `examples` directory and check the	
By running `jinja-cli --help` on your terminal, you'll get all the basic functioning for the tool.


## Basics

If you know [Jinja][jinja], you will get how this works easily.

- `INPUT` or _template_, is the text stream or file that you are attempting to render _by default stdin_.
- `DATA` or _json-data_, is the text stream or file that contains the data used in the template and it's dependencies, _by default is an empty json_.
- `ROOT` or _template-directory_, is the search path for jinja's `FileSystemLoader`.
- `CONFIG` or _extensions-file_, is a python file that contains functions that will be avalible to call from the templates, could be filters. 
- `OUTPUT` or `output`, is where to write the rendered template, _by default is stdout_.

__Remark__: This is more related to `*sh` scripting than this tool, but notice that we mention streams, so we could run the following commands and they would be equivalent in output.

```
cat examples/templates/users.htm | jinja-cli -j examples/data/users.json
cat examples/data/users.json | jinja-cli -j - -i examples/templates/users.htm
jinja-cli -i examples/templates/users.htm -j examples/data/users.json
jinja-cli -i <(cat examples/templates/users.htm) -j <(cat examples/data/users.json)
```

This is because the argument parsing for the input template and json data, was thinked in a way that you send any of does two as streams so we could use and compose with other cli tools.


## Examples

All the examples could be reproduced with the files in the `examples` directory.

### Curl in to a template

Using the data variables you could fill templates pulling data from any kind of source, and insert it using standard input

```
$ curl https://xkcd.com/2/info.0.json 2> /dev/null | jinja-cli -i examples/templates/xkcd.htm -j -
<article>
    <h2>Petit Trees (sketch)</h2>
    <img src="https://imgs.xkcd.com/comics/tree_cropped_(1).jpg"/>
    <p>'Petit' being a reference to Le Petit Prince, which I only thought about halfway through the sketch</p>
</article>
```

### Using Jinja Filters

You could also use custom functions and call them as filters from your `config` file, eg.

```python3

# fragment of examples/extensions.py
import jinjasimplecli.extensions as je

@je.filter('issue')
def hello_world(issue_number):
    url = f"https://api.github.com/repos/ekiim/jinjasimplecli/issues/{issue_number}"
    data = requests.get(url).json()
    return f"Issue - {data['number']} - {data['title']}"
```

So now running `$ echo "{{ 1|issue }}" | jinja-cli -c examples/extensions.py` we get 
`Issue - 1 - Merge Guide and Readme`. 

### Jinja other features

When using template inheritance or referencing another template to import or include, 
you should make reference to it, considering the `ROOT` path you provided.


## License

Jinja Simple CLI is licensed under the [BSD 3-Clause license][license].


[jinja]: http://jinja.pocoo.org/docs/2.10/api/
[license]: blob/master/LICENSE
