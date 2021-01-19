Style Guide
###########

The style, syntax and structure of source code and raw files should be kept
consistent through out the evolution of the project.

To remain firm on this vision, linters are introduced and where possible auto
formatters are run to fix inconsistent formats.

This allows the focus to be on the content of the file and expecting a similar
style through out the project.

Python
******

Python source code files are linted using `flake8`_ and `pylint`_. This
ensures complaince with `PEP8`_ Style Guide for Python Code.

In addition to that `Black`_ code formatter is used to automatically format
Python source code files.

YAML
****

`YAML`_ (YAML Ain't Markup Language) is a human friendly data serialization
standard meant for all programming languages.

In this project all YAML files will have the extension ``.yaml`` in
accordance with this published `FAQ <https://yaml.org/faq.html>`.

While there is no style guide for YAML to follow, using a linter helps
keeping YAML files consistent.

YAML files are linted with `yamllint`_

JSON
****

`JSON`_ (JavaScript Object Notation) is a lightweight data-interchange open
standard used as file format and data transmission, that uses human-readable
text to store and transmit data objects consisting of attribute–value pairs and
array data types (or any other serializable value).

JSON filenames use the extension ``.json``.

To ensure JSON files are valid, they will be loaded to make sure
the syntax is valid. A pretty format will be applied as well.

reStructuredText (RST)
**********************

`reStructuredText`_ (RST, ReST, or reST) is a text file format for textual data
for technical documentation.

While this project uses `Sphinx`_ for generating documentation from
reStructuredText file, there are cases when reStructuredText files are
introduced outside the scope of Sphinx. Examples of such use cases include
``README.rst`` for easy to read documentation directly while browsing the
source code.

For the purpose of styling reStructuredText files we exclude files used
for Sphinx.

All other reStructuredText files will be linted with `rstcheck`_ via
`pre-commit`_ hooks.

Tabs and Spaces
***************

The mix use of Tabs and Spaces creates confusion and ugly diffs. It also
creates a bigger diff when somebody uses an editor which converts all tabs to
spaces.

Please use spaces every where except when the use of Tabs is required by
syntax.

Using `pre-commit`_ hooks, files will be checked for tab spaces and fail
accordingly. Exceptions are made for Makefile as they require tab spaces as
part of their syntax.

Trailing Spaces
***************

Trailing whitespace is spaces or tabs after the last non-whitespace character
on the line until the newline. This usually serves no purpose as part of the
format or coding structure.

Furthermore, other developers may use editors that remove trailing spaces as
they save the modified file and this can create a bigger diff then needed.

Using `pre-commit`_ hooks, files will be checked for trailing spaces and
remove it

Linting and Formatting
**********************

There are make rules that handle linting and formatting for the whole project
and its source code::

    make lint
    make format

The ``lint`` rule will only notify you of problems and not attempt to fix or
modify the source code.

The ``format`` rule will format the source code and modify it. Commit your
changes before running this rule.

Running these rules will help with the Styling principal outlined in on this
page.
