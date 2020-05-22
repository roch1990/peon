.PHONY tests
tests:
	coverage run -m pytest ./src/tests
	mutmut --paths-to-mutate ./src/peon --tests-dir ./src/unit run
