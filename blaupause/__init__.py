'''
A small sample project.

There are some functions and one class to demonstrate testing
and documentation.
'''

import pytest
import pkg_resources
from .functions import add, subtract, multiply
from .blueprint import Blueprint

__version__ = pkg_resources.get_distribution(__name__).version
__dependencies__ = pkg_resources.require(__name__)


def test():
    '''Run doctests.
    '''
    return pytest.main(['-v', '--pyargs', 'blaupause'])  # pragma: no cover
