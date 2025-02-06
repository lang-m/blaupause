'''
A small sample project.

There are some functions and one class to demonstrate testing
and documentation.
'''

import pytest
import importlib.metadata
from .functions import add, subtract, multiply
from .blueprint import Blueprint

__version__ = importlib.metadata.version(__package__)


def test():
    '''Run doctests.
    '''
    return pytest.main(['-v', '--pyargs', 'blaupause'])  # pragma: no cover


if __name__ == '__main__':
    main()
