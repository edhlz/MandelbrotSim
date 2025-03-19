import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iteration):
    z = 0 
    for n in range(max_iteration):
        if abs(z) > 2:
            return n
        z = z**2 + c    
    return max_iteration

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iteration):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, width)
    mset = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            mset[i, j] = mandelbrot(c, max_iteration)

    return mset


xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
width, height = 1000, 1000

max_iteration = 100

mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iteration)

plt.imshow(mandelbrot_image, extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.colorbar()
plt.title('Mandelbrot Teste')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.show