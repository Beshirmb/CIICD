"""
Tests
"""
from run import import_data, rename_columns, get_sample, multiply_dataset


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


def test_get_sample(self):
    """
    Test
    """
    data = import_data()
    data_sample = get_sample(data)
    self.assertIsNotNone(data_sample)
    self.assertIsInstance(data_sample, pd.DataFrame)
    self.assertEqual(len(data_sample), 50)


def test_multiply_dataset(self):
    """
    Test
    """
    data = import_data()
    data_sample = get_sample(data)
    data_multiply = multiply_dataset(data_sample)
    self.assertIsNotNone(data_multiply)
    self.assertIsInstance(data_multiply, pd.DataFrame)

