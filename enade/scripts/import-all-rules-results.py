import pandas as pd

rules_table_2019 = pd.read_csv('../analysis/results/organized-associations-2019.csv', sep=',', encoding='UTF-8', index_col=0)
rules_table_2019['year'] = 2019

rules_table_2020 = pd.read_csv('../analysis/results/organized-associations-2020.csv', sep=',', encoding='UTF-8', index_col=0)
rules_table_2020['year'] = 2020

rules_table_2021 = pd.read_csv('../analysis/results/organized-associations-2021.csv', sep=',', encoding='UTF-8', index_col=0)
rules_table_2021['year'] = 2021

rules_table_2022 = pd.read_csv('../analysis/results/organized-associations-2022.csv', sep=',', encoding='UTF-8', index_col=0)
rules_table_2022['year'] = 2022

all_rules = pd.concat([rules_table_2019, rules_table_2020, rules_table_2021, rules_table_2022], ignore_index=True)
