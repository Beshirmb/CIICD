"""
Tests
"""
from run import import_data, rename_columns, get_sample

def test_import_data():
    """
    Test
    """
    data = import_data()
    assert data.shape[0] > 0

def test_rename_columns():
    """
    Test
    """
    data = import_data()
    data_renamed = rename_columns(data)
    assert "sepal_length" in data_renamed.columns

def test_get_sample():
    """
    Test
    """
    data = import_data()
    data_sample = get_sample(data)
    
