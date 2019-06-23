# Contributing to resurfaceio-logger-python
&copy; 2016-2019 Resurface Labs Inc.

## Coding Conventions

Our code style is whatever PyCharm does by default, with the exception of allowing lines up to 130 characters.
If you don't use PyCharm, that's ok, but your code may get reformatted.

## Git Workflow

```
git clone git@github.com:resurfaceio/logger-python.git resurfaceio-logger-python
cd resurfaceio-logger-python
pip install --upgrade setuptools wheel twine mamba
```

Running unit tests:

```
mamba --format=documentation
```

Committing changes:

```
git add -A
git commit -m "#123 Updated readme"       (123 is the GitHub issue number)
git pull --rebase                         (avoid merge bubbles)
git push origin master
```

## Release Process

All [integration tests](https://github.com/resurfaceio/logger-tests) must pass first.

Push artifacts to [pypi.org](https://pypi.org/):

```
python setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*
```

Tag release version:

```
git tag v1.x.x
git push origin master --tags
```

Start the next version by incrementing the version number in both `setup.py` and `__init__.py` files.