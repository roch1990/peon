[![Build Status](https://travis-ci.org/roch1990/peon.svg?branch=master)](https://travis-ci.org/roch1990/peon)
[![codecov](https://codecov.io/gh/roch1990/peon/branch/master/graph/badge.svg)](https://codecov.io/gh/roch1990/peon)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=roch1990_peon&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=roch1990_peon)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=roch1990_peon&metric=alert_status)](https://sonarcloud.io/dashboard?id=roch1990_peon)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=roch1990_peon&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=roch1990_peon)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=roch1990_peon&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=roch1990_peon)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=roch1990_peon&metric=code_smells)](https://sonarcloud.io/dashboard?id=roch1990_peon)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=roch1990_peon&metric=security_rating)](https://sonarcloud.io/dashboard?id=roch1990_peon)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=roch1990_peon&metric=sqale_index)](https://sonarcloud.io/dashboard?id=roch1990_peon)
[![Hits-of-Code](https://hitsofcode.com/github/roch1990/peon)](https://hitsofcode.com/view/github/roch1990/peon)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![](https://www.meme-arsenal.com/memes/4310e01cdd1fbad0ef9a7b48bfe8fdca.jpg)

# PEON (In development now)

# Table of contents

- [Introduction](#introduction)
    - [What is that](#what-is-that)
    - [What eo principles i can check](#what-eo-principles-i-can-check)
- [Use-cases](#use-cases)
    - [Shell](#from-shell)
    - [Pre-commit hook](#add-linter-to-pre-commit-hooks)
- [Some theoretical nuances](#some-theoretical-nuances)
    - [Why naive](#why-naive)
- [Development](#development)
    - [Testing](#testing)
    - [Contributing](#contributing)
        - [Commit naming conventions](#commit-naming-conventions)
        - [Pull-request naming conventions](#pull-request-naming-conventions)
- [License](./LICENSE.txt)

# Introduction
## What is that?

 "Python Elegant Objects Naive" linter allows you to check your code for conditions of
 "[Elegant objects](https://www.elegantobjects.org/)" OOP architecture,
 proposed by [yegor256](https://github.com/yegor256)

 This repo work only for python code.

## What eo principles i can check?

 | Priciple| Yes/No|
 | ------------- |:------------------:|
 | No null       | :heavy_check_mark:    |
 | No code in constructors     | :heavy_check_mark: |
 | No getters and setters     | :heavy_check_mark: |
 | No mutable objects | :heavy_check_mark:         |
 | No readers, parsers, controllers, sorters, and so on | :heavy_check_mark:         |
 | No static methods, not even private ones | :heavy_check_mark:         |
 | No instanceof, type casting, or reflection | :heavy_check_mark:         |
 | No public methods without a contract | :x:         |
 | No statements in test methods except assertThat | :heavy_check_mark:  |
 | No ORM or ActiveRecord | :x:  |
 | No implementation inheritance | :heavy_check_mark: |

 :heavy_check_mark: - realized

 :interrobang: - so-so (not sure)

 :heavy_minus_sign: - not done yet

 :x: - will never be done, i think

# Use-cases

## From shell

Simply you should run something like this (dont forget to `python3 setup.py install`)

```bash
peon ./path/to/code
```

or not recommended way

```bash
python3 ./peon/__main__.py
```


## Add linter to pre-commit hooks

You can use this linter by adding it to [pre-commit](https://pre-commit.com/) configuration file.

For example (for check all project):
```yaml
  - repo: https://github.com/roch1990/peon
    rev: '0.13'
    hooks:
      - id: peon
        stages:
          - commit
        args:
          - ./peon
```

or (for check only changed files):
```yaml
  - repo: https://github.com/roch1990/peon
    rev: '0.13'
    hooks:
      - id: peon
        stages:
          - commit
```


# Some theoretical nuances
## Why naive?

 Because it checks only "plain definitions".

 For example:

 - good, linter check that:
 ```python
def some_function(some_arg):
    some_var = some_arg

```

- bad, linter skip that (definition inside definiton - discourage and decrease code quality):
 ```python
def some_function(some_arg):
    def some_another_function(some_arg):
        return some_arg
    some_var = some_another_function(some_arg)

```

- good, linter check that:
 ```python
class SomeClass:
    pass

```

- bad, linter skip that (definition inside definiton - discourage and decrease code quality):
 ```python
class SomeClass:
    class SomeAnotherClass:
        pass
    pass

```

# Development

## Pre-requisite

After you clone repo:
- create virtual env

`python3 -m venv /path/to/new/virtual/environment`

- install requirements

`pip3 install - r ./peon/requirements.txt`

- install pre-commit hooks

`pre-commit install`

- setup PYTHONPATH

`export PYTHONPATH=$PWD/peon`

And then feel free to make a changes.

## Testing

You can start local test:

```bash
make tests
```

this instruction starts both tests - unit and mutual.

Show results of mutual tests:

```bash
mutmut results
```

Show result of concrete mutual test:

```bash
mutmut show <test_id:int>
```

## Contributing

Easiest way is:
- fork
- make changes at your branch
- commit and create PR to dev branch of this repo

If all check would be passed - I check your changes so fast, as i can.

P.S.: falling of mutual tests - is normal now (in development, as you remember)

### Commit naming conventions

Every commit should start with keyword with colon:
- `feature:` (if you add new functionality)
- `fix:` (if you fix bug or invalid behaviour)
- `chore:` (if you fix something, that you were not going to fix)

Then, after keyword you should shortly describe your changes:
`feature: add sec test step to travis`

### Pull request naming conventions

Every pull request should start with keyword pr and issue number:
`pr-23`
