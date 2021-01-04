======================
Cookiecutter PyPackage
======================

.. image:: https://github.com/Digimach/cookiecutter-python-package/workflows/tests/badge.svg?branch=master&event=push
    :target: https://github.com/Digimach/cookiecutter-python-package/actions?query=workflow%3Atests+event%3Apush+branch%3Amaster
    :alt: Test Status

Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/Digimach/cookiecutter-python-package
* Documentation: https://github.com/Digimach/cookiecutter-python-package/blob/master/README.rst
* Free software: BSD license

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Usage
-----

1. Install :code:`cookiecutter` in your Python environment. Ex: 
   :code:`pip install cookiecutter`

2. Use this template project to generate your project
   :code:`cookiecutter https://github.com/Digimach/cookiecutter-pypackage.git`

3. The `Project Variables`_ section defines the Cookiecutter variables that will
   be prompted and used to configure the generated project.

4. If you want to work in a Git repository for the generated project see
   `Git Repository`_.


.. _`Project Variables`:

Project Variables
-----------------

    * :code:`project_title`: The title of the project that is being created.

    * :code:`project_slug`: The slug is used to give the Python package an
      install name. This should be compliant with `PEP-0008: Package and Module 
      Names <https://www.python.org/dev/peps/pep-0008/#package-and-module-names>`_

    * :code:`project_short_description`: Project description that will be added
      to `setup.py <{{cookiecutter.project_slug}}/setup.py>`_ and published
      with the package.
    
    * :code:`project_author_email`: The author email address that will be used
      for license generation and also published with the package in
      `setup.py <{{cookiecutter.project_slug}}/setup.py>`_

    * :code:`project_author_name`: The author name that will be used for 
      license generation and also published with the package in
      `setup.py <{{cookiecutter.project_slug}}/setup.py>`_

    * :code:`project_source_url`: HTTP accessible URL that can link to the
      source of the generated project.

    * :code:`project_doc_url`: HTTP accessible URL that can link to the
      documentation of the generated project.

    * :code:`install_requires`: List of Python packages, in CSV form, that are
      required by the generated project at install.

    * :code:`project_extra_dev_requires`: List of Python packages, in CSV form,
      that are required by the generated project during development.

    * :code:`project_extra_test_requires`: List of Python packages, in CSV form,
      that are required to test the generated project.

    * :code:`initialize_git_repo`: If true, will setup a Git repository in the
      generated project and do an initial commit. You can amend the initial
      commit or add on top. See `Git Repository`_ for more information.

.. _`Git Repository`:

Git Repository
--------------

If :code:`initialize_git_repo` is :code:`yes` (the default) a Git repository will be initialized in
the target repository. This will also do a commit for you which you can then
amend or add on top. This allows you to diff against the templated project with
your own work.

You just have to add the remote to push the Git repository::

    git remote add origin <repo url>

If you chose :code:`initialize_git_repo` to be :code:`no` you can initialize
the Git repository in your templated project:

.. code-block::

    git init
    git add --all
    git remote add origin <repo url>
    git push

