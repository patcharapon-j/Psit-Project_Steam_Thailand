"""Create Heatmap"""
import process as pr
import plotly.plotly as py
import plotly.graph_objs as go
data2 = pr.reader()
games = [data2[0][x] for x in range(len(data2))]
data = [
    go.Heatmap(
        z=[run[1:] for run in data2],
        x=[games],
        y=[str(x) for x in range(1, 61)]
    )
]
plot_url = py.plot(data, filename='labelled-heatmap')
plot_url = py.plot(data, filename='basic-heatmap')