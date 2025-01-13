import pandas as pd

from source import data_analyser


def test_can_read_data_from_file():         # the data_analyser.py file not used as we are testing just the ability to read
    # arrange
    test_columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num',
                    'marital-status', 'occupation', 'relationship', 'race', 'sex',
                   'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
                   'salary']

    # act
    df = pd.read_csv("../adult_data.csv")

    # assert

    assert list(df.columns) == test_columns

