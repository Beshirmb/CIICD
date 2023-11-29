"""
Tests
"""
from run import import_data, rename_colums

def test_import_data():
    """
    Test
    """
    data = import_data()
    assert data.shape[0] > 0
    return data
