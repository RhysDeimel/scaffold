# Scaffold
Basic python tox, pytest, & coverage project structure


## Installation
Simply clone, remove the `.git` folder (re-init if you like), and change any `scaffold` references to that of your
project name. EZPZ


## Usage
Slap your venv in the root dir, install the dev requirements with `pip install -e .[dev]`, then run `pytest` or `tox` from the root dir to see the
results. Tox will run through any specified python versions you put in the `env_list`.
For added bonus, I've thrown in coverage and markers for slow tests.

Coverage will run everytime you call `tox`, and it will also populate the htmlcov folder with
[jazz](https://www.youtube.com/watch?v=xuPSIbABYVU) so you can see how lazy you've been with your test coverage.
Feel free to check the `pyproject.toml` to see adjustable failure rates for coverage.
Additionally, coverage is aggregated across all the specified python versions,
so your body better be ready for that one.

With the slow test markers, tox will automatically run them. If you want to run pytest _in_ tox while skipping the
slow tests, use `tox -- -m "not slow"`. Keep in mind, this will mess with the coverage reporting.

If you only care about running the tests (and noting else), you don't have to use tox. You can simply run `pytest`.
To run the slow tests, you will have to use the marker: `pytest --runslow`. 

> [!CAUTION]
> Depending on how you're importing packages, running pytest outside tox might fail.
> Relative vs absolute imports and all that nonsense.


## Directory Structure
```
.
├── README.md
├── tox.ini
├── pyproject.toml  # project and tool settings
├── htmlcov
│   └── reporting html, css, and js files
├── src
│   ├── conftest.py
│   └── scaffold  # your actual project code
│       ├── __init__.py
│       ├── __main__.py
│       ├── bar.py
│       ├── baz.py
│       └── foo.py
├── tests
│   ├── __init__.py
│   ├── conftest.py  # global fixtures
│   ├── functional
│   │   ├── __init__.py
│   │   └── test_bar.py 
│   ├── integration
│   │   ├── __init__.py
│   │   └── test_baz.py
│   └── unit
│       ├── __init__.py
│       └── test_foo.py
└── venv        
```
