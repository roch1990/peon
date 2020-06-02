.PHONY: tests
tests:
	coverage run -m pytest ./peon/tests --disable-warnings
	coverage xml -o coverage-report.xml
	mutmut --paths-to-mutate ./peon/src --tests-dir ./peon/tests run || true
	bandit -r ./peon -x ./peon/tests

.PHONY: cov-report
cov-report:
	coverage xml -o coverage-report.xml
