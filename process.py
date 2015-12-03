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
    return data

def avgerage():
    """return list contain avg of all data"""
    data = reader()
    out = []
    for run in data:
        out.append([run[0], statistics.mean(run[1])])
    return out

def normalizer(day):
	"""return normalized data from 0 to 1 at day 'day'"""
    data = reader()
	total = sum([x[1][day-1] for x in data])
	out = []
	for run in data:
		out.append([run[0], run[1][day-1] / total])
	return out

