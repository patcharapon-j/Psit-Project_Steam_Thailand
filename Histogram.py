import plotly.plotly as py
import plotly.graph_objs as go
from process import reader
py.sign_in("IMFluky", "80ck3k2e4n")

for x in range(len(reader())):
    data = [
        go.Bar(
            x=[i for i in range(1, 60)],
            y=reader()[x][1]
        )
    ]
    layout = go.Layout(
        title=reader()[x][0],
    )
    fig = go.Figure(data=data, layout=layout)
    url = py.plot(fig, filename=reader()[x][0])
