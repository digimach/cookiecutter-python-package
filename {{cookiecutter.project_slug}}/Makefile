PYTEST_FLAGS=

# Clean rules
.PHONY: clean
clean :
	git clean -dX --force
# -------------------

# Setup rules for the dev environment
.PHONY: setup-dev
setup-dev :
	tox --develop --workdir .tox -e py
	pre-commit install
# -------------------

# Test rules
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
lint : bake flake8_check pylint_check black_check

.PHONY: flake8_check
flake8_check :
	flake8 --max-line-length=88 --count --statistics src/ tests/

.PHONY: pylint_check
pylint_check :
	pylint --jobs 0 src/ tests/

.PHONY: black_check
black_check :
	black --check --diff --verbose .
# -------------------

# Formatting related rules
.PHONY: black
black :
	black --verbose .
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

# Debug report rules
.PHONY: debug-report
debug-report :
	@echo "|*****************|"
	-which python
	@echo "|*****************|"
	-which pip
	@echo "|*****************|"
	-python --version
	@echo "|*****************|"
	-pip freeze
	@echo "|*****************|"
	-git status
	@echo "|*****************|"
	-git log -1
	@echo "|*****************|"
