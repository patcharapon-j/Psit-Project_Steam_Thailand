import plotly.plotly as pty
import process as pr
import statistics as stat
from plotly.tools import FigureFactory
pty.sign_in("Chiibi", "lm7ftxursd")
data = pr.reader()

data_matrix = [['Games', 'Average', 'Ceiling', 'Floor', 'SD']] + [[i[0], '{0:,.2f}'.format(stat.mean(i[1])), '{0:,d}'.format(max(i[1])), '{0:,d}'.format(min(i[1])), '{0:,.2f}'.format(stat.stdev(i[1]))] for i in data]

table = FigureFactory.create_table(data_matrix, index=True)
url = pty.plot(table, filename='data_table')
