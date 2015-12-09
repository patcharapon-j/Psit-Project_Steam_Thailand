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
h_color = []
for run in games:
    for run2 in range(1, 61):
        h_game.append(run)
        h_day.append(run2)
        h_value.append(data2[run][run2-1])
        h_color = "#ddb7b1"
source = ColumnDataSource(
    data=dict(games=h_game, day=h_game, color=h_color, value=h_value)
)

output_file = ("playtimeheatmep.html")
TOOLS = "resize,hover,save,pan,box_zoom,wheel_zoom"
p = figure(title="Thailand Steam Playtime 2015",
    x_range=games, y_range=[str(x) for x in range(60, 0, -1)],
    x_axis_location="above", plot_width=900, plot_height=400,
    toolbar_location="left", tools=TOOLS)
