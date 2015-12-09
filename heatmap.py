"""Create Heatmap"""
import process as pr
import plotly.plotly as py
import plotly.graph_objs as go
data2 = pr.reader()
games = [data2[x][0] for x in range(len(data2))]
data2 = [run[1] for run in data2[2:-1]]
data3 = []
for run in range(len(data2[0])):
    temp = []
    for run2 in range(len(data2)):
        temp.append(data2[run2][run])
    data3.append(temp)
data = [
    go.Heatmap(
        z=data3
        x=games[2:-1]
        y=[str(x) for x in range(1, 61)]
    )
]
plot_url = py.plot(data, filename='Steam-heatmap')

