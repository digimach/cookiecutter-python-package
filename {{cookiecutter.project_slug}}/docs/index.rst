{% set title_length = cookiecutter.project_title | length -%}
Welcome to {{ cookiecutter.project_title }}
###########{{ title_length * "#" }}

{{ cookiecutter.project_short_description | wordwrap(79)}}

.. toctree::
   :maxdepth: 3

   Contributing </dev_guide/contributing>
   Developers' Guide </dev_guide/index>


.. toctree::
   :maxdepth: 3

   addendums/index

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
