
import tifffile as tif
import numpy as np

data = np.random.randint(0, 255, (30, 3, 256, 256), 'uint8')
tif.imwrite('demo_uint8.ome.tif', data, photometric='rgb')

data = np.random.randint(0, 65535, (30, 3, 512, 512), 'uint16')
tif.imwrite('demo_uint16.ome.tif', data, photometric='rgb')

