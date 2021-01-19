Pre-Commit hooks
################

This project uses `pre-commit`_ to install Git hooks that can be manually
invoked or automatically invoked before committing the change.

You can find the pre-commit configuration in the ``.pre-commit-config.yaml``

:ref:`contributing_first_time_setup` handles installing the pre-commit hooks
in the development environment.

To manually run the hook you can run::

    pre-commit run --all-files
