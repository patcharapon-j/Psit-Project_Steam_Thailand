"""Create Heatmap"""
import process as pr
import numpy as np
from collections import OrderedDict
from bokeh.models import HoverTool
from bokeh.plotting import ColumnDataSource, figure, show, output_file
data = pr.reader()
games = [data[x][0] for x in range(len(data))]
data2 = {}
colors = [
    "#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce",
    "#ddb7b1", "#cc7878", "#933b41", "#550b1d"
]
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
    data=dict(games=h_game, day=h_day, color=h_color, value=h_value)
)

output_file("playtimeheatmep.html")
TOOLS = "resize,hover,save,pan,box_zoom,wheel_zoom"
p = figure(title="Thailand Steam Playtime 2015",
    x_range=games, y_range=[str(x) for x in range(60, 0, -1)],
    x_axis_location="above", plot_width=900, plot_height=400,
    toolbar_location="left", tools=TOOLS)

p.rect("games", "day", 1, 1, source = source,
    color="color", line_color=None)

p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "5pt"
p.axis.major_label_standoff = 0
p.xaxis.major_label_orientation = np.pi/3

#hover = p.select(dict(type=HoverTool))
#hover.snap_to_data = False
#hover.tooltips = OrderedDict([
#    ('Data', '@games @day'),
#    ('Playtime', '@value'),
#])

show(p) 