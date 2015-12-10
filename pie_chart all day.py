"""Pie-Chart for all day data"""
import plotly.plotly as py
import plotly.graph_objs as go
from process import request_day
py.sign_in("IMfluky", "tq0lke37dz")

for day in range(1, 61):
    fig = {
        "data": [{"labels": [request_day(day)[i][0] for i in range(len(request_day(day)))],
                  "values": [request_day(day)[i][1] for i in range(len(request_day(day)))],
                  "type": "pie"}],
        "layout": {"title": "Steam Play Time Day "+str(day)}
    }

    url = py.plot(fig, filename="Play Time Pie Chart Day"+str(day))
