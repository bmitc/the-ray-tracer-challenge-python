[![build and test](https://github.com/bmitc/the-ray-tracer-challenge-python/actions/workflows/build-and-test.yml/badge.svg?branch=main)](https://github.com/bmitc/the-ray-tracer-challenge-python/actions/workflows/build-and-test.yml)

**Note**: This is a work in progress. Only a portion of the ray tracer is currently implemented.

# The Ray Tracer Challenge in Python

This repository is a Python implementation of the ray tracer found in [*The Ray Tracer Challenge: A Test-Driven Guide to Your First 3D Renderer*](https://pragprog.com/titles/jbtracer/the-ray-tracer-challenge/) by Jamis Buck.

This code is effectively a port of that found in [bmitc/the-ray-tracer-challenge-fsharp](https://github.com/bmitc/the-ray-tracer-challenge-fsharp), but the port was not dogmatic in carrying over the F# style. In other words, it has been attempted to be as idiomatic to Python as possible, given my personal up to date knowledge of Python. The style will certainly be adjusted as I move more towards a Pythonic implementation and continue to evolve the codebase by finishing the ray tracer implementation and performing refactors. Updating my knowledge of the latest and greatest in Python 3.12, which is the latest Python version just released, and the ecosystem was a primary impetus for this project (I even discovered an issue with Mypy for Python 3.12), so there is a lot of incentive in evolving this code rather than maintaining its status as a port of the F# code. The port is only to kickstart the initial implementation, and even then, the word port is used loosely here.

One might notice some similarity, perhaps unexpected if one is unfamiliar with F#, between the F# and Python code. One of the main differences is due to the fact that F# is statically typed but has type inference, which means type annotations are not required except for clarity and certain situations. Python is dynamically typed, which necessitates the heavy use of type hints, as found in this project. Thus, Mypy was utilized to do as much static type checking as possible. This project utilizes Poetry to organize the project and has incorporated Mypy, Pylint, and Black to enforce types, style, and formatting. All of the tests found in the book, since the book is effectively a test-driven design book, are implemented via `unittest`. Pytest may be investigated in the future.

## Example renders

### [Chapter 2: Drawing on a Canvas: Putting it Together](https://github.com/bmitc/the-ray-tracer-challenge-python/blob/main/ray_tracer_challenge/projectile.py)

To run the script and see the image, run:

```
poetry run projectile
```

![image](https://github.com/bmitc/the-ray-tracer-challenge-python/assets/65685447/61b6241a-bd6b-4ac8-bed7-13b426bd4f27)


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
