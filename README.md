# the-ray-tracer-challenge-python
 
## Setup

This project is configured as a [Poetry project](https://python-poetry.org/). All dependencies are listed in `pyproject.toml`. The following assumes `python` is Python 3, so you can replace `python` with `python3` if your system needs that disambiguation.

```
python -m pip install --user pipx
python -m pipx ensurepath
pipx install poetry
poetry install
```

This installs all needed dependencies.

## Running unit tests

At the root of the repository, execute

```
poetry run python -m unittest discover tests
```

to run all unit tests.

## Running Mypy

```
poetry run mypy ray_tracer_challenge
```
