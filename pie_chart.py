"""Create pie chart from process"""
import plotly.plotly as py
import plotly.graph_objs as go
from process import avgerage #it's average but miss spelling
py.sign_in("IMfluky", "80ck3k2e4n")

fig = {
    "data": [{"labels": [avgerage()[i][0] for i in range(2, len(avgerage())-1)],
              "values": [avgerage()[j][1] for j in range(2, len(avgerage())-1)],
              "type": "pie"}],
    "layout": {"title": "Thailand Steam Play Time August-September 2015"}
}

url = py.plot(fig, filename="Pie_Chart")
