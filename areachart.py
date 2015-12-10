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
trace = [None for _ in range(28)]

for num in range(28):
	trace[num] = go.Scatter(
		x = axis_x,
		y = axis_y[num],
		hoverinfo = 'name+y+x', #show information when mouse is over
		name = information.reader()[num][0],
	    mode ='lines',
	    line = dict(
	        width = 0.5
	    ),
	    fill='tonexty'
	)


data = [trace[num] for num in range(28)]
layout = go.Layout(
	showlegend = True,
	title = 'Steamspy Data',
	xaxis=dict(
		title = 'Days'
	),
	yaxis = dict(
		title = 'Minute'
	)
)

fig = go.Figure(data=data, layout=layout)
plot_url=py.plot(fig, filename='stacked-area-plot')