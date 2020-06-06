.PHONY: local-run
local-run:
	pre-commit try-repo ./

.PHONY: tests
tests:
	pre-commit run --all
	coverage run -m pytest ./peon/tests --disable-warnings
	coverage xml -o coverage-report.xml
	mutmut --paths-to-mutate ./peon/src --tests-dir ./peon/tests run || true
	bandit -r ./peon -x ./peon/tests

.PHONY: cov-report
cov-report:
	coverage xml -o coverage-report.xml

.PHONY: help
help:
	@echo "You can run this helpfull commands:"
	@echo
	@echo -e "\tmake local-run   try your changes in pre-commit environment"
	@echo -e "\tmake tests       start tests"
	@echo -e "\tmake cov-report  generate coverage-report at cobertura format"
