import matplotlib.pyplot as plt
from sys import argv

data = sp.genfromtxt("data/argv[0].tsv", delimiter="\t")

def plot(data):
	plt.scatter(x,y)
	plt.title("Web traffic over the last month")
	plt.xlabel("Time")
	plt.ylabel("Hits/hour")
	plt.xticks([w*7*24 for w in range(10)],
	 ['week %i'%w for w in range(10)])
	plt.autoscale(tight=True)
	plt.grid()
	plt.show()


if __name__ == '__main__':
	main()

	