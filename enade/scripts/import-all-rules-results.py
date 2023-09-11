import pandas as pd

rules_table_2018 = pd.read_csv('../analysis/results/organized-associations-2018.csv', sep=',', encoding='UTF-8', index_col=0)
rules_table_2018['year'] = 2018

rules_table_2019 = pd.read_csv('../analysis/results/organized-associations-2019.csv', sep=',', encoding='UTF-8', index_col=0)
rules_table_2019['year'] = 2019

all_rules = pd.concat([rules_table_2018, rules_table_2019], ignore_index=True)
