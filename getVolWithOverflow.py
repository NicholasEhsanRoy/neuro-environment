# Turned out to be what really allowed for progress, finally got a volume where everything was there, 


import cloudvolume as cv
import numpy as np
import trimesh


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

print("will make a mesh of " + str(len(list_of_segs)) + " segments")

list_of_segs.remove(0)

mesh_dict = vol.mesh.get(segids=list_of_segs, lod=3)

trimesh_list = []

print("creating trimeshes")

mesh_count = 0

for mesh in mesh_dict.values():
    if len(mesh.vertices) > 10:
        continue
    trimesh_list.append(trimesh.Trimesh(vertices=mesh.vertices, faces=mesh.faces))
    mesh_count += 1

print("created list of " + str(mesh_count) + " trimesh meshes")

volume_mesh = trimesh.util.concatenate(trimesh_list)

print("created a merged mesh")

volume_mesh.export(file_obj="mesh-of-unincluded-segments.obj", file_type="obj")

print("exported the mesh as an obj file")
#trimesh.Trimesh(vertices = mesh.vertices, faces=mesh.faces).export(file_obj="test_np_mesh.obj", file_type="obj")

#print("mesh saved, go view it now and hope it worked")
