#!/usr/bin/env python3
"""
setup.py for Cookiecutter template project.
"""

from setuptools import find_packages, setup

setup(
    name="cookiecutter-python-package",
    version="0.1.0",
    url="https://github.com/Digimach/cookiecutter-python-package",
    project_urls={
        "Code": "https://github.com/Digimach/cookiecutter-python-package",
        "Documentation": "https://github.com/Digimach/cookiecutter-python-package"
    },
    license="BSD-3-Clause",
    author="Digimach",
    author_email="",
    description="Cookiecutter for creating Python packages",
    long_description=__doc__,
    classifiers=[
        "License :: BSD-3-Clause",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(exclude=("tests", )),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[''],
    extras_require={
        "test": [
            'cookiecutter', 'coverage', 'flake8', 'gitpython', 'pylint',
            'pytest', 'pytest-cookies', 'pytest-cov', 'pyyaml', 'safety',
            'tox', 'yapf'
        ],
        "dev": []
    },
    zip_safe=False,
    platforms="any",
)
