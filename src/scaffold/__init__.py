# scaffold/__init__.py

"""An example python project structure

Modules exported by this package:

- `calulator`: Provide several sample math calculations.
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("scaffold")
except PackageNotFoundError:
    # package is not installed
    pass
