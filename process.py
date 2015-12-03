"""Process Rawdata and compute statistics values"""
import statistics
def reader():
	"""read data from txt file"""
	f = open("Raw Data.txt", "r")
	print(f.read())

reader()
