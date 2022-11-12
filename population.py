import pandas as pd
import matplotlib.pyplot as plt

pdata= pd.read_csv("population data.csv")

plt.figure()

plt.plot(pdata["Country "], pdata["Population 2020"],color="red", label="population of countries at 2020")
plt.plot(pdata["Country "], pdata["Net Change"],color="green", label="Net Change")
plt.xticks(rotation=90)
plt.title("population of countries")
plt.legend()
plt.show()


plt.bar(pdata["Country "],pdata["Yearly Change"],color="green", label="population yearly change")
plt.xticks(rotation=90)
plt.title("yearly change in population")
plt.legend()
plt.show()

plt.scatter(pdata["Country "],pdata["Density  (P/Km²)"],color="green", label="population Density")
plt.xticks(rotation=90)
plt.title("population density")
plt.legend()
plt.show()