# this turned out to be the approach I used.
import pyvista as pv

print("reading in neuropil mesh")
mesh = pv.read("neuropil-mesh-without-cropping.obj", file_format="obj", progress_bar=True)

print("making a bbox")
# Define bounding box (min and max coordinates for x, y, and z)
bbox_min = [794952, 797920, 676638]  # Minimum vertex values
bbox_max = [811592, 811360, 723039]  # Maximum vertex values

box = pv.Box(bounds=[bbox_min[0], bbox_max[0], bbox_min[1], bbox_max[1], bbox_min[2], bbox_max[2]])

clipped_mesh = mesh.clip_box(box, invert=False, progress_bar=True)

print("bbox made, now plotting the box, where my region should be")
plotter = pv.Plotter()

plotter.add_mesh(clipped_mesh, color='blue', opacity = 1, show_edges=True)

plotter.add_mesh(box, color='red', opacity=0.1)

plotter.show()






