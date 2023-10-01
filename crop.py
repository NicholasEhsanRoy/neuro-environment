# Was eventually what I used to crop the massive mesh with overflow to just the stuff I needed.

import trimesh
import concurrent.futures
from tqdm import tqdm  # Import tqdm

def process_chunk(chunk, bbox_min, bbox_max):
    vertices_to_keep = []
    for vertex in chunk:
        if bbox_min[0] <= vertex[0] <= bbox_max[0] and \
           bbox_min[1] <= vertex[1] <= bbox_max[1] and \
           bbox_min[2] <= vertex[2] <= bbox_max[2]:
            vertices_to_keep.append(vertex)
    return vertices_to_keep

print("loading mesh")
# Load the mesh
mesh = trimesh.load_mesh('neuropil-mesh-without-cropping.obj')
print("loaded mesh")

# Define bounding box (min and max coordinates for x, y, and z)
bbox_min = [794952, 797920, 676638]  # Minimum vertex values
bbox_max = [811592, 811360, 723039]  # Maximum vertex values

print("defined bbox")

# Split vertices into smaller chunks
num_chunks = 8
chunk_size = len(mesh.vertices) // num_chunks
vertex_chunks = [mesh.vertices[i:i + chunk_size] for i in range(0, len(mesh.vertices), chunk_size)]

print("split vertices into chunks")
vertices_to_keep = []

print("processing vertices in parallel")
# Process vertices in parallel with tqdm
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for chunk in vertex_chunks:
        futures.append(executor.submit(process_chunk, chunk, bbox_min, bbox_max))
    
    # Add tqdm to loop
    for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing Vertices"):
        vertices_to_keep.extend(future.result())

print("updating faces")
# Update faces based on the new vertex indices
new_faces = []
for face in mesh.faces:
    for vertex in mesh.vertices[face]:
        if vertex in vertices_to_keep:
            new_faces.append(face)

print("creating cropped mesh")
# Create a new mesh with cropped vertices and updated faces
cropped_mesh = trimesh.Trimesh(vertices=vertices_to_keep, faces=new_faces)

print("exporting mesh")
# Export the cropped mesh to a file
cropped_mesh.export('neuropil.obj')
