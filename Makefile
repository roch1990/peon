.PHONY: tests
tests:
	coverage run -m pytest ./src/tests --disable-warnings
	mutmut --paths-to-mutate ./src/peon --tests-dir ./src/tests run || true
