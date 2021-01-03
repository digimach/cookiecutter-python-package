======================
Cookiecutter PyPackage
======================

Usage
-----

1. Install :code:`cookiecutter` in your Python environment. Ex: 
   :code:`pip install cookiecutter`

2. Use this template project to generate your project
   :code:`cookiecutter https://github.com/Digimach/cookiecutter-pypackage.git`

3. The `Project Variables`_ section defines the Cookiecutter variables that will
   be prompted and used to configure the generated project.

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
