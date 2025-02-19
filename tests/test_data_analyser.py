import pandas as pd
from source import data_analyser
from source.data_analyser import calculate_demographic_data


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


def test_average_age_men():
    df = pd.read_csv("../adult_data.csv")

    # df = pd.DataFrame({'a': [1, 2], 'b': [2, 3]}, index=['tiger', 'zebra'])
# df
#        a   b
# tiger  1   2
# zebra  2   3
# df.mean()
# a   1.5
# b   2.5
# dtype: float64


    expected = df[df["sex"] == "Male"]["age"].mean().round(1)
    result = calculate_demographic_data(print_data=False)["average_age_men"].round(1)
    assert result == expected

def test_percentage_of_ppl_with_bachelor_degree():
    df = pd.read_csv("../adult_data.csv")


    expected = df[df["education"] == "Bachelor"].mean().round(1)
    result = calculate_demographic_data(print_data=False)["average_age_men"].round(1)
    assert result == expected
