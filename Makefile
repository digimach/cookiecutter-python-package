PYTEST_FLAGS=

# Clean rules
.PHONY: clean
clean : 
	git clean -fdX
# -------------------

# Setup rules for the dev environment
.PHONY: setup-dev
setup-dev :
	tox --develop --workdir .tox -e py
# -------------------

# Test rules
.PHONY: pytest
pytest :
	pytest -vvvv --strict-markers --basetemp=./.pytest_tmp/ $(PYTEST_FLAGS)

.PHONY: test
test : pytest lint
# -------------------

# Lint Check rules
.PHONY: lint
lint : flake8_check pylint_check yapf_check

.PHONY: flake8_check
flake8_check :
	flake8 --max-line-length=80 --count --statistics *.py hooks 

.PHONY: pylint_check
pylint_check :
	pylint --jobs 0 --extension-pkg-whitelist ujson,rapidjson *.py hooks 

.PHONY: yapf_check
yapf_check :
	yapf --recursive --parallel --verbose --diff .
# -------------------

# Formatting related rules
.PHONY: yapf
yapf:
	yapf --recursive --in-place --parallel --verbose .
# -------------------
