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

def test_each_race_count():
    df = pd.read_csv("../adult_data.csv")
    count_race = df['race'].value_counts()

    # assert needs to be .equals not == cuz otherwise it returns boolean
    assert data_analyser.calculate_demographic_data(print_data=False)['race_count'].equals(count_race)

