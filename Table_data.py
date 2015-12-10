import plotly.plotly as pty
import process as pr
import statistics as stat
from plotly.tools import FigureFactory
pty.sign_in("Chiibi", "lm7ftxursd")
data = pr.reader()

data_matrix = [['Games', 'Average', 'Ceiling', 'Floor', 'SD']] + [[i[0], stat.mean(i[1]), max(i[1]), min(i[1]), stat.stdev(i[1])] for i in data]

table = FigureFactory.create_table(data_matrix, index=True)
url = pty.plot(table, filename='data_table')
