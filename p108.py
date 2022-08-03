# -*- coding: utf-8 -*-
"""p108

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GbhpJfOGoHsgIwKYLwGJfMdmjQVEPISt
"""

from google.colab import files
data_to_load=files.upload()



import plotly.figure_factory as ff
import pandas as pd
import csv
df=pd.read_csv("project.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=False)
fig.show()