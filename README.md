# Scaffold
> Basic python tox, pytest, & coverage project structure

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

