"""Pie-Chart for all day data"""
import plotly.plotly as py
import plotly.graph_objs as go
from process import request_day
py.sign_in("IMfluky", "80ck3k2e4n")

fig = {
    "data": [{"labels": [request_day(1)[i][0] for i in range(len(request_day(1)))],
              "values": [request_day(1)[i][1] for i in range(len(request_day(1)))],
              "type": "pie"}],
    "layout": {"title": "Steam play time 60 day"}
}

url = py.plot(fig, filename="Test Pie Chart")
