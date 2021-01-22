Contributing to {{ cookiecutter.project_title }}
################{{ cookiecutter.project_title | length * "#" }}

Thank you for considering contributing to {{ cookiecutter.project_title }}!

Support Questions
*****************

During development if you have any questions **about your code** please do
not use the issue tracker. Instead, use one of the following methods:

- Send an email to {{ cookiecutter.project_author_email }}

..
    GARNISH: Add additional developer support methods

Reporting issues
****************

If **while development** you discover an issue with existing code, first ensure
that:

- you are developing off a supported branch. This is usually the ``master``
  branch;

- you have the latest version of repository and the workspace reflects the
  latest version of the upstream supported branch;

- you started of a clean development environment and setup a fresh environment.
  In most cases you can ensure this by saving your work and try doing::

    make clean
    make setup-dev

  If after this you still see the issue continue reading;

- ensure the test is passing without your modifications.
  Run the ``test`` rule in the Makefile::

    make test

  If the test fails, include this information when reporting.

If after all the above steps you are still seeing the problem, report it and
include:

- A description of what you expected to happen.

- If possible, a `minimal reproducible example`_ to help the support
  group identify the issue. This also helps check that the issue is not with
  your own modification to the code.

- A description of what actually happened. Include the full traceback if there
  was an exception or any log output that help describe the difference in
  behaviour.

- Include the output from::

    make debug-report

Submitting Patches
******************

We welcome contributions in any way or form and thank you for doing so as well.

Before you start working on your patch its important to distinguish between:

1. Bug Fixes

  a. Functional

  b. Documentation

2. New Features

Functional Bug Fixes
====================

Every functional bug fix patch must have a reported issue associated with it.
This gives everyone a chance to have a look at the problem statement and
validate the problem before work starts on a patch.

Documentation Bug Fixes
=======================

If you plan to work on the documentation bug fix you can jump ahead and start
coding. If you do not plan to do the fix, we ask you still report the issue
so someone can have a look and fix it.

New Features
============

New features should be discussed with the community before being implemented.
This gives everyone the opportunity to propose alternatives, design ideas,
and solutions or participate in discussions around this feature.

The best way to start this discussion is to open an issue for a new feature
request.

In your request include what problem you are solving or the plan on how you
would make use of this new feature.

.. _contributing_first_time_setup:

First time setup
================

- Famialirze yourself with :doc:`/dev_guide/index`.
  It covers certain elements mentioned on this page in detail.

- Download and install the
  `latest version of Git <https://git-scm.com/downloads>`_.

- Configure Git with your username and email::

    git config --global user.name '<your full name>'
    git config --global user.email '<your email>'

- Fork and download the source_ locally.

- Install tox_::

    pip install tox

- From within the source directory setup the development environment using
  tox_ via make rule provided for ease of use:::

    make setup-dev

  If for some reason you do not have make you can have a look at the Makefile
  and run the tox command under ``setup-dev`` rule which looks like::

    tox --develop --workdir .tox --devenv .tox/py -e py

- Activate the development environment::

    source .tox/py/bin/activate

Begin Coding
============

- Create a branch in your local workspace to identify the issue you would like
  to work on. You can use the issue number in your branch name if you prefer.
  If you are working on a functional or documentation bug fix, branch off of
  the latest ".x" branch::

    git checkout -b your-branch-name origin/1.0.x

  If you are working on a **new** feature addition or change, branch off of
  the ``master`` branch::

    git checkout -b your-branch-name origin/master

- Using your favorite editor, make your changes, commit as you go.

- Use ``git rebase`` to make your past commits atomic. You can do this at the
  very end before opening a pull request for review.

- Include test(s) for any code changes you make. Make sure the test fails
  without your patch. Read more about :doc:`/dev_guide/testing/index`.

- Push your commits to your fork::

        git push --set-upstream origin your-branch-name


Formatting Patches
==================

- Use the make rule ``format`` for :doc:`Styling </dev_guide/style>` your code
  appropriately::

    make format

- Make sure your commits are `atomic <https://en.wikipedia.org/wiki/Atomic_commit#Atomic_commit_convention>`_,
  descriptive in their message and easy to follow. If your commit is fixing
  an issue include the issue identifier in the commit message.

Running Tests
=============

Run the basic test suite with::

    make test

This only runs the tests for the current environment which in most cases is the
latest development environment.

The full set of test suite includes running the test on multiple Python
environments to ensure all supported Python versions and their dependencies
work. This is achieved using `tox`_ and can be executed by invoking::

  tox

Running Test Coverage
---------------------

Test coverage is part of the test infrastructure to report coverage threshold
failures as part of the test.

Reports are generated under ``htmlcov`` after every test run.

You can view the report by opening ``htmlcov/index.html``

Read more about `coverage`_.

Running the full test suite with ``tox`` combines the coverage reports
from all the environment runs.


Building the docs
-----------------

Build the project documentation by invoking the ``docs`` target in the
Makefile::

  make docs

Open ``docs/_build/html/index.html`` in your browser to view the docs.

Read more about `Sphinx <https://www.sphinx-doc.org/en/master/>`_.
