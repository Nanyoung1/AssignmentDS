import numpy as np
x = np.arange(62500)
x = x.reshape(25, 25, 100)
x_mean = x.mean(axis=2)
np.savetxt("test.csv", x_mean, delimiter=",")
