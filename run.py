"""
CI/CD
"""
import pandas as pd

def main():
    """
    Main
    """
    data = import_data()
    data = rename_columns(data)

    
def import_data() -> pd.DataFrame:
    """
    Import csv file as a dataframe
    Output: data [pd.DataFrame]
    """
    data = pd.read_csv("data/iris.csv")
    print(data.shape)
    return data

def rename_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Doc
    """
    data_renamed = data.rename(columns={"sepal.length": 'sepal_length',
                                "sepal.width": 'sepal_width',
                                "petal.length": 'petal_length',
                                "petal.width": 'petal_width'})
    return data_renamed

import pandas as pd

def get_sample(dataset, sample_size=50):
    """
    This function takes a portion of the dataset (sample) of the specified size.
    
     Args:
     - dataset: A pandas DataFrame representing the dataset.
     - sample_size: The size of the sample to extract. By default, it is 50.
    
     Returns:
     A DataFrame representing the sample.
    """
    print(dataset.head(sample_size))
    return get_sample

if __name__ == '__main__':
    """
    Doc
    """
    main()
