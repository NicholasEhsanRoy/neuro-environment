# Turned out to be a failed attempt at cropping, but learned alot.

import trimesh
import numpy as np

# Load the .obj file
mesh = trimesh.load("neuropil-mesh-without-cropping.obj")

print("loaded the mesh")

# Define the bounding box (min and max vertices)
bbox_min = [794952, 797920, 676638]  # Minimum vertex values
bbox_max = [811592, 811360, 723039]  # Maximum vertex values

print("defined a bbox")

# Find the indices of vertices inside the bounding box
inside_bbox = np.all((mesh.vertices >= bbox_min) & (mesh.vertices <= bbox_max), axis=1)
print("found list of indices as boolean array")

# Create a mask to filter the faces
face_mask = np.all(inside_bbox[mesh.faces], axis=1)

# Extract the vertices and faces within the bounding box
cropped_vertices = mesh.vertices[inside_bbox]
cropped_faces = mesh.faces[face_mask]
print("filtered vertices and faces")

# Create a new trimesh object from the cropped vertices and faces
cropped_mesh = trimesh.Trimesh(vertices=cropped_vertices, faces=cropped_faces)

print("cropped mesh")

# The cropped_mesh contains the cropped mesh based on the bounding box

cropped_mesh.export(file_obj="cropped_neuropil_mesh.obj", file_type="obj")

print("exported cropped mesh")
