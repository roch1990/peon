![](https://www.meme-arsenal.com/memes/4310e01cdd1fbad0ef9a7b48bfe8fdca.jpg)

# In development now

# PEON

 "Python Elegant Objects Naive" linter allows you to check your code for conditions of
 "[Elegant objects](https://www.elegantobjects.org/)" OOP architecture,
 proposed by [yegor256](https://github.com/yegor256)

 This repo work only for python code.


 # Why naive?

 Becase this linter is simple ast-nodes reader.


 # What eo principles i can check?

 | Priciple| Yes/No|
 | ------------- |:------------------:|
 | No null       | :heavy_check_mark:    |
 | No code in constructors     | :heavy_check_mark: |
 | No mutable objects | :heavy_minus_sign:         |
 | No readers, parsers, controllers, sorters, and so on | :heavy_check_mark:         |
 | No static methods, not even private ones | :heavy_check_mark:         |
 | No instanceof, type casting, or reflection | :heavy_check_mark:         |
 | No public methods without a contract | :x:         |
 | No statements in test methods except assertThat | :heavy_minus_sign:  |
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
