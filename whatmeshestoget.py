# Did this because I realised some segments where probably not actually neurons / glia / blood vessels.
# (These where the ones that had 4 vertices and didn't seem to make a reasonable shape, given the fact
# that it was at 4nm resolution. Helped me get a reasonable sized mesh).

import cloudvolume as cv
import numpy as np
import trimesh
import matplotlib.pyplot as plt


vol = cv.CloudVolume("precomputed://gs://iarpa_microns/minnie/minnie65/seg", mip=0, parallel=True)


point1_x = 100000
point1_y = 100000
point1_z = 17000

point2_x = 101000
point2_y = 101000
point2_z = 18000

bounding_box = cv.Bbox((point1_x, point1_y, point1_z),(point2_x, point2_y, point2_z))

unique_ids = vol.unique(bounding_box, mip=0)

list_of_segs = list(unique_ids)

list_of_segs.remove(0)

num_segs = len(list_of_segs)

vertex_numbers = []

print("will test " + str(num_segs) + "segments")

i = 0

num_runs = 0

while i <= num_segs:
    mesh_dict = vol.mesh.get(segids=list_of_segs[i], lod=3)
    for mesh in mesh_dict.values():
        vertex_numbers.append(len(mesh.vertices))
    
    print("vertices: " + str(vertex_numbers[i]))
    i+=1
    print(i)

    
print(vertex_numbers)

plt.hist(vertex_numbers, bins=100, edgecolor='k')  # Adjust the number of bins as needed
plt.title('Histogram of number of vertices in meshes that are in this region')
plt.xlabel('Number of vertices')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()