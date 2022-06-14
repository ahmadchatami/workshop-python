import pandas as pd
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv"
df = pd.read_csv(url)


df.head()

df.index

df.T