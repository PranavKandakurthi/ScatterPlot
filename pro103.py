import plotly.express as px
import pandas as pd
csvv = pd.read_csv('data.csv')
gph = px.scatter(csvv, x='date', y='cases', color='country')
gph.show()