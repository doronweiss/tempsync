# This is a sample Python script.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import calcs
# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


data = pd.read_csv(r'c:\Users\User\OneDrive\Projects\BennyGranot\benny.csv', encoding='utf-8')

# fig1, ax = plt.subplots()
# ax.plot(data.CH1.values)
# ax.plot(data.CH2.values)
# ax.plot(data.CH3.values)
# ax.plot(data.CH4.values)
# ax.plot(data.CH5.values)
# fig1.show()
# exit(0)

res = calcs.corrSeries(data.CH1.values, data.CH2.values, 2)
fig2, ax = plt.subplots()
ax.plot(res)
fig2.show()

#plt.close(fig1)
plt.close(fig2)

