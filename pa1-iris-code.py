import pandas as pd

url = "https://raw.githubusercontent.com/quesoazucarado-ctrl/pa1-machinelearning/refs/heads/main/iris.csv"

df = pd.read_csv(url, header = None)

df.head()
