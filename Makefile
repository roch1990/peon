.PHONY: tests
tests:
	coverage run -m pytest ./src/tests --disable-warnings
	coverage xml -o coverage-report.xml
	mutmut --paths-to-mutate ./src/peon --tests-dir ./src/tests run || true
	bandit -r ./src -x ./src/tests

.PHONY: cov-report
cov-report:
	coverage xml -o coverage-report.xml
