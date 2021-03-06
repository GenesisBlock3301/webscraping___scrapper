import pandas as pd

readFile = pd.read_csv('results.csv')
readFile.to_excel('results.xlsx',index=False,header=True)
