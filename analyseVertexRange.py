# This was to try and find a mapping between the coordinate systems in the cloud-volume and eventual trimesh
# because I noticed some discrepencies.
import trimesh
import numpy as np

mesh = trimesh.load("neuropil-mesh-without-cropping.obj")

print("Mesh loaded")

vertices = mesh.vertices

print("found vertices")

min_x = np.min(vertices[:, 0])  # Minimum x value
max_x = np.max(vertices[:, 0])  # Maximum x value

print("found x values")

min_y = np.min(vertices[:, 1])  # Minimum y value
max_y = np.max(vertices[:, 1])  # Maximum y value

print("found y values")

min_z = np.min(vertices[:, 2])  # Minimum z value
max_z = np.max(vertices[:, 2])  # Maximum z value

print("found z values")

print("box is:")

print("x: " + str(min_x))
print("y: " + str(min_y))
print("z: " + str(min_z))

print("")
print("to")
print("")

print("x: " + str(max_x))
print("y: " + str(max_y))
print("z: " + str(max_z))