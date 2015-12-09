import plotly.plotly as py
import plotly.graph_objs as go
from process import reader
py.sign_in("IMFluky", "80ck3k2e4n")

data = [
    go.Bar(
        x=[i for i in range(1, 60)],
        y=reader()[0][1]
    )
]
layout = go.Layout(
    title=reader()[0][0],
)
fig = go.Figure(data=data, layout=layout)
url = py.plot(fig, filename=reader()[0][0])
