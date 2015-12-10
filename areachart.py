#using information from process.py
import process as information
#using module plotly
import plotly.plotly as py
import plotly.graph_objs as go



#add data
txt = "Day"
axis_x = [txt+str(num+1) for num in range(60)] #add axis_x
axis_y = [[information.reader()[num][1][i] for i in range(60)] for num in range(28)]
### axis_y = []
### for num in range(28):
### 	axis_y.append([information.reader()[num][1][i] for i in range(60)])

#trace data
trace0 = go.Scatter(
	x = axis_x,
	y = axis_y[0],
	text=str(axis_y[0]),
    hoverinfo='x+text',
    mode='lines',
    line=dict(
        width=0.5
    ),
    fill='tonexty'
)

data = [trace0]

fig = go.Figure(data=data)
plot_url=py.plot(fig)