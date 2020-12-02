import pytest
import pkg_resources
from .function import add

__version__ = pkg_resources.get_distribution(__name__).version
__dependencies__ = pkg_resources.require(__name__)


def test():
    return pytest.main(['-v', '--pyargs', 'sampleproject'])  # pragma: no cover
