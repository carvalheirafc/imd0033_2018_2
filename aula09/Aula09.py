import pandas as pd
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None


