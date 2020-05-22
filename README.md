[![Build Status](https://travis-ci.org/roch1990/peon.svg?branch=master)](https://travis-ci.org/roch1990/peon)
[![codecov](https://codecov.io/gh/roch1990/peon/branch/master/graph/badge.svg)](https://codecov.io/gh/roch1990/peon)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=roch1990_peon&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=roch1990_peon)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=roch1990_peon&metric=alert_status)](https://sonarcloud.io/dashboard?id=roch1990_peon)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=roch1990_peon&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=roch1990_peon)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=roch1990_peon&metric=sqale_index)](https://sonarcloud.io/dashboard?id=roch1990_peon)
[![Hits-of-Code](https://hitsofcode.com/github/roch1990/peon)](https://hitsofcode.com/view/github/roch1990/peon)


![](https://www.meme-arsenal.com/memes/4310e01cdd1fbad0ef9a7b48bfe8fdca.jpg)

# In development now

# PEON

 "Python Elegant Objects Naive" linter allows you to check your code for conditions of
 "[Elegant objects](https://www.elegantobjects.org/)" OOP architecture,
 proposed by [yegor256](https://github.com/yegor256)

 This repo work only for python code.


 # Why naive?

 Becase it check only "plain definitions".

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


 # What eo principles i can check?

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

Simply you should run something like this

```bash
peon ./src
```

# Add linter to pre-commit hooks

You can use this linter by adding it to [pre-commit](https://pre-commit.com/) configuration file.

For example:
```yaml
  - repo: https://github.com/roch1990/peon
    rev: master
    hooks:
      - id: peon
        stages:
          - commit
        args:
          - ./src/peon
```
