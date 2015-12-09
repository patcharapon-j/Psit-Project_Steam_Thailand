"""Create Heatmap"""
import process as pr
import plotly.plotly as py
import plotly.graph_objs as go
data2 = pr.reader()
data2 = data2[2:-7] + data2[-8:-2]
games = [data2[x][0] for x in range(len(data2))]
data2 = [run[1] for run in data2]
data3 = []
for run in range(len(data2[0])):
    temp = []
    for run2 in range(len(data2)):
        temp.append(data2[run2][run])
    data3.append(temp)
data = [
    go.Surface(
        z=data3,
        x=games,
        y=[str(x) for x in range(1, 61)]
    )
]
layout = go.Layout(
    title='Steam Thailand Playtime 2015 (Aug - Sep)',
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Steam-heatmap')

