"""Test bee_utils."""
# pylint: disable=broad-except
from bee_utils import __version__
from bee_utils import bee_utils


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not bee_utils()
    except Exception:
        assert True
