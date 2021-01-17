# {{ cookiecutter.project_title }}

{{ cookiecutter.project_short_description }}

---

## Installation

### Git Submodule and Installing locally in Python

* Place the repository as a submodule inside your application repository
at the root level in `{{ cookiecutter.project_slug }}` directory. If choosing another directory
name make sure to use that in the next steps. For example <your_project>/{{ cookiecutter.project_slug }}
* Change directory into `{{ cookiecutter.project_slug }}`.
* Install the `{{ cookiecutter.project_slug }}` package by invoking `make install`. This will
install the `{{ cookiecutter.project_slug }}` Python package in the local Python that is first
in the path. If using a virtual environment like
[conda](https://docs.conda.io/en/latest/) or
[venv](https://docs.python.org/3/library/venv.html) make sure the appropriate
environment is active before invoking the install command.

---

## Usage
```python
TODO
```

---

## Development

### Environment Setup

* To develop this project an environment will have to be setup. There is an
easy way to set this up using [tox](https://tox.readthedocs.io/en/latest/). To
setup a test environment `tox --recreate --devenv <path to place env>`.

* The path where the dev environment is placed will have Python installed and
can be launched `<path to place env>/bin/python`. It will also have the
`{{ cookiecutter.project_slug }}` package linked to the repository allowing you to load the module
directly from Python.

* If `tox` is not installed in your local Python environment, you can install
it by invoking `pip install tox`.

* You can also add `<path to place env>/bin/` to your PATH to make use of
`make` rules outside of `tox`. This is optional but highly recommended.

### Style Guidelines

* This project follows
[Google Python Style Guide](http://google.github.io/styleguide/pyguide.html).
* Using [yapf](https://github.com/google/yapf/) the code should be formatted to
ensure consistent code structure between developers. The `yapf` make rule can
be used to format the code by running `make yapf`.

### Testing

* This project contains `pytest` based unit and integration tests located in
[tests](./tests).
* Testing also includes linting the code and checking for code coverage.
* Tests can be executed by invoking the `tox` command from within the project.
* [tox](https://tox.readthedocs.io/en/latest/) will setup the environment for
testing and call the test rule in the [Makefile](./Makefile) by running
`make test`.

---
