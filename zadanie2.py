import numpy as np
import matplotlib.pyplot as plt
try:	
	data=np.loadtxt ("newton.txt")
	plt.plot(data[:,0], data[:,1], marker='.')
	plt.minorticks_on()
	plt.grid(which="major", linewidth=1)
	plt.grid(which="minor", linestyle=":", linewidth=0.5)
	plt.show()
except BaseException:
	print("faila nety")
