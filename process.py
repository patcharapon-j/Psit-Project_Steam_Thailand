"""Process Rawdata and compute statistics values"""
import statistics
def reader():
	"""read data from txt file"""
	data = []
	f = open("Raw Data.txt", "r")
	head = None
	temp = []
	for run in f.read().split("\n"):
		if "###" in run:
			data.append([head, temp])
			temp = []
			head = run[4:-4]
		else:
			temp.append(int(run.split()[3]))
	data.append([head, temp])
	data = data[1:]

reader()
