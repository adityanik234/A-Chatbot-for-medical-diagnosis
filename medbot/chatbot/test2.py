import csv
import pandas as pd
words = pd.read_table('/Users/adityanaik/Desktop/Summer project/CODE files/glove.840B.300d.txt', sep=" ", index_col=0, header=None, quoting=csv.QUOTE_NONE)
reza = words.iloc[0]
print(reza)
