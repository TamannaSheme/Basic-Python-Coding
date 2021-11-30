"""Plot sin using np library. Use linspace to generate values."""""

#Exercise-03
import matplotlib.pyplot as pl
import numpy as np

x = np.linspace(-np.pi, np.pi, 556, endpoint=True)
y = np.sin(x)
pl.plot(x,y)
pl.show()

"""Plot cosine function using np library. Use linspace to generate values."""""

#Exercise
import matplotlib.pyplot as pl
import numpy as np

x = np.linspace(-np.pi, np.pi, 556, endpoint=True)
y = np.cos(x)
pl.plot(x,y)
pl.show()

"""Plot tan function using np library. Use linspace to generate values."""""

#Exercise
import matplotlib.pyplot as pl
import numpy as np

x = np.linspace(-np.pi, np.pi, 556, endpoint=True)
y = np.tan(x)
pl.plot(x,y)
pl.show()


"""Plot sin, cosine, and tan function using np library. Use
linspace to generate values."""""
#Exercise
import matplotlib.pyplot as pl
import numpy as np

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

y = np.cos(x)
y1 = np.sin(x)
z1 = np.tan(x)
pl.plot(x,y)
pl.plot(x, y1)
pl.plot(x, z1)

pl.show()
