import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("games.csv")

df.plot.hist(column="white_rating")
plt.show()