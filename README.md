# Jinja Simple CLI

This projects offers a way to easily compose templates directly from the 
command line, ideal to use in junction with other cli utilities.

By running `jinja-cli --help` on your terminal, you'll get all the basic functioning for the tool.

```
usage: jinja-cli [-h] [--template-directory [TemplatesDirectory]]
                 [--json-data DATAFILE] [--extensions-file CONFIGFILE]
                 [-o [OUTPUT]]
                 [TargetTemplate]

This tool will allow you to compose jinja templatesin an easy way

positional arguments:
  TargetTemplate        path to the template file you want to build, this
                        could be full path, relative to current directory or
                        relative to the templates directory if provided. If
                        this parameter is ommited it will be taken from stdin.

optional arguments:
  -h, --help            show this help message and exit
  --template-directory [TemplatesDirectory], -t [TemplatesDirectory]
                        Path to a directory with jinja templates, this
                        templates will be loaded and avalible to reference
                        from the template we are providing for the build.
  --json-data DATAFILE, -j DATAFILE
                        Json data, this could be a filepath relative or
                        absolute, or a stream where the content it's json
                        formated.
  --extensions-file CONFIGFILE, --config CONFIGFILE, -c CONFIGFILE
                        A python file that includes the functions you and
                        additional enviroment changes.
  -o [OUTPUT]           Where will the rendered template will be outputed
```

