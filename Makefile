PYTEST_FLAGS=

# Clean rules
.PHONY: clean
clean : 
	git clean -dX --force 
	rm -rf .baked/
# -------------------

# Setup rules for the dev environment
.PHONY: setup-dev
setup-dev :
	tox --develop --workdir .tox -e py
# -------------------

# Test rules
.PHONY: bake
bake :
	cookiecutter --overwrite-if-exists --no-input --output-dir ./.baked --config-file ./tests/cookiecutter_test_user_config.yml .

.PHONY: pytest
pytest :
	pytest -vvvv --strict-markers --basetemp=./.pytest_tmp/ --numprocesses=auto $(PYTEST_FLAGS)

.PHONY: safety
safety :
	safety check

.PHONY: test
test : pytest lint
# -------------------

# Lint Check rules
.PHONY: lint
lint : bake flake8_check pylint_check yapf_check rst_check

.PHONY: flake8_check
flake8_check :
	flake8 --max-line-length=80 --count --statistics *.py hooks .baked/

.PHONY: pylint_check
pylint_check :
	pylint --jobs 0 --extension-pkg-whitelist ujson,rapidjson *.py hooks .baked/baked_cookie/setup.py .baked/baked_cookie/src/baked_cookie

.PHONY: yapf_check
yapf_check :
	yapf --recursive --parallel --verbose --diff .

.PHONY: rst_check
rst_check : 
	rst-lint *.rst
# -------------------

# Formatting related rules
.PHONY: yapf
yapf:
	yapf --recursive --in-place --parallel --verbose .
# -------------------

# Documentation Testing rules
.PHONY: doc_test
doc_test : doc_dry_run_test doc_link_check

.PHONY: doc_dry_run_test 
doc_dry_run_test :
	make --directory=./docs SPHINXOPTS="-W -n --keep-going" html

.PHONY: doc_link_check
doc_link_check :
	make --directory=./docs linkcheck
# -------------------

# Documentation build rules
.PHONY: docs
docs :
	make --directory=./docs html
# -------------------