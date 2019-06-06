# Scaffold
Basic python tox, pytest, & coverage project structure

## Installation
Maybe oneday I'll turn this into a [cookiecutter](https://github.com/audreyr/cookiecutter) template, but I'm too lazy atm.
Simply clone, remove the `.git` folder (re-init if you like), and change any `scaffold` references to that of your
project name. EZPZ

## Usage
Slap your venv in the root dir, install the requirements, then run `pytest` or `tox` from the root dir to see the
results. Tox will run through py3.6 & 3.7, so if it fails, that'll be why. For added bonus, I've thrown in coverage and
markers for slow tests.

Coverage will run everytime you run `tox`, and it will also populate the htmlcov folder with
[jazz](https://www.youtube.com/watch?v=xuPSIbABYVU) so you can see how lazy you've been with your test coverage. Fee
free to check the `.coveragerc` to see adjustable failure rates for coverage. Additionally, coverage aggregates across
all the specified python versions, so your body better be ready for that one.

 With the slow test markers, tox will automatically run them, but simply calling `pytest` will skip them. If you want to
 explicitly run them, use `pytest --runslow` 


## Directory Structure
```
.
├── .coveragerc
├── README.md
├── requirements.txt
├── setup.py
├── tox.ini
├── htmlcov
│   └── reporting html, css, and js files
├── src
│   ├── conftest.py
│   └── scaffold
│       ├── __init__.py
│       ├── __main__.py
│       ├── bar.py
│       ├── baz.py
│       └── foo.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
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


## What Is This Sorcery?!
Take a look. Most of the magic is in the `setup.py` which stops tox from derping out, and the stratigic placement of an
empty `conftest.py`, which lets pytest know where to find the code to test.