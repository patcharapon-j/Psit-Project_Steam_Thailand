#using information from process.py
import process as information
#using module plotly
import plotly.plotly as py
import plotly.graph_objs as go



#add data
txt = "Day"
axis_x = [txt+str(num+1) for num in range(60)] #add axis_x
axis_y = [[information.reader()[num][1][i] for i in range(60)] for num in range(28)]

#stack data
y_stack = [1 for _ in range(28)]
y_stack[0] = axis_y[0]
for i in range(28):
	if i > 0:
		y_stack[i] = [y0+y1 for y0, y1 in zip(axis_y[i], y_stack[i-1])]

#trace data
trace = [None for _ in range(28)]
for num in range(28):
	trace[num] = go.Scatter(
		x = axis_x,
		y = y_stack[num],
		text = axis_y[num],
		hoverinfo = 'name+x', #show information when mouse is over
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