"""Create Heatmap"""
import process as pr
import numpy as np
from bokeh.plotting import *
from bokeh.models import HoverTool
data['games'] = [pr.reader()[x][0] for x in range(len(pr.reader()))]
games = list(data['games'])