import pandas as pd

from pandas.core.frame import DataFrame

file_path: str = "/home/leandro/studyspace/data_science/codigos/modulo_5/dados/kc_house_data.csv"
# data_set: DataFrame = pd.read_csv(file_path, sep=",", header=0)

data_set: DataFrame = pd.read_csv(file_path, sep=",")

# print(data_set)
# print(data_set.columns)
# print(data_set.count())
# print(data_set.describe())
print(data_set.shape)
# print(data_set.info())