[![build and test](https://github.com/bmitc/the-ray-tracer-challenge-python/actions/workflows/build-and-test.yml/badge.svg?branch=main)](https://github.com/bmitc/the-ray-tracer-challenge-python/actions/workflows/build-and-test.yml)

# The Ray Tracer Challenge in Python

This repository is a Python implementation of the ray tracer found in [*The Ray Tracer Challenge: A Test-Driven Guide to Your First 3D Renderer*](https://pragprog.com/titles/jbtracer/the-ray-tracer-challenge/) by Jamis Buck.

This code is effectively a port of that found in https://github.com/bmitc/the-ray-tracer-challenge-fsharp, but the port was not dogmatic in carrying over F# style. The code has been attempted to be as idiomatic to Python as possible, given my personal up to date knowledge of Python, and the style will be adjusted as I come across new things. One might notice some unexpected similarity, if one is unfamiliar with F#, between the F# and Python code, although the Python code is actually more often than not the more verbose of the two. This is particularly the case since F# is statically typed but has type inference and thus does not require type annotations, whereas Python is dynamically typed and requires the heavy use of type hints, as found in this project. Mypy was utlizied as much as possible to do as much static type checking as possible. Also, that brings up the point that this project has utilized Mypy, Pylint, and Black to enforce types, style, and formatting. All of the tests found in the book, since the book is effectively a test-driven design book, are implemented via `unittest`. Pytest may be investigated in the future.

## Setup

This project is configured as a [Poetry project](https://python-poetry.org/). All dependencies are listed in `pyproject.toml`. The following assumes `python` is Python 3, so you can replace `python` with `python3` if your system needs that disambiguation.

```
python -m pip install --user pipx
python -m pipx ensurepath
pipx install poetry
poetry install
```

This installs all needed dependencies.

## Running tests, formatters, linters, and type checkers

All of the following commands should be run at the repository's root. And all of these checks are currently run in a GitHub Action to verify that the code maintains full compliance with the checks.

### Unit tests

```
poetry run python -m unittest discover tests
```

### Mypy

Mypy is configured in `pyproject.toml` to run in strict mode.

```
poetry run mypy ray_tracer_challenge
```

### Black formatter

Black is configured in `pyproject.toml`.

```
poetry run black .
```

### Run Pylint

Pylint is configured in `.pylintrc`.

```
poetry run pylint ray_tracer_challenge
```
