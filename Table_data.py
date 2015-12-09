import plotly.plotly as pty
import process as pr
import statistics as stat
from plotly.tools import FigureFactory

data = pr.reader()
data_avg = pr.avgerage()
data_matrix = [['Games', 'Average', 'Ceiling', 'Floor', 'SD'],]

table = FigureFactory.create_table(data_matrix, index=True)
pty.iplot(table, filename='index_table')