import plotly.graph_objects as go
from pandas import *

data = read_csv("sankey.csv")

source = data['source'].tolist()
target = data['target'].tolist()
value = data['value'].tolist()

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = source, # rishiraj acharya
      color = "blue"
    ),
    link = dict(
      source = source, # indices correspond to labels
      target = target,
      value = value
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()
