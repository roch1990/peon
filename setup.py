from setuptools import setup, find_packages

setup(
    name='peon',
    version='0.13',
    description='Python "Elegant Object" Naive linter. ',
    url='https://github.com/roch1990/peon',
    author='roch1990',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.*']),
    entry_points={
      'console_scripts': [
          'peon = peon.__main__:main',
      ],
    },
)
