import pandas as pd

systems = pd.read_csv('products.csv')
df = systems['os'].value_counts()
print(df)


