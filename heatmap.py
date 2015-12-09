"""Create Heatmap"""
import process as pr
import numpy as np
from bokeh.plotting import *
from bokeh.models import HoverTool
data = pr.reader()
games = [data[x][0] for x in range(len(data))]
data2 = {}
for run in data:
    data2[run[0]] = run[1]
h_game = []
h_day = []
h_value = []
H_color = []
for run in games:
    for run2 in range(1, 61):
        h_game.append(run)
        h_day.append(run2)
        h_value.append(data2[run][run2-1])
        h_color = "#ddb7b1"

