# This turned otu to be a dead-end, but learned what my skills don't yet put me in a position to use.

from intern.remote.cv import CloudVolumeRemote
from intern.resource.cv import CloudVolumeResource
from intern.service.mesh.service import MeshService, VoxelUnits
import numpy as np

remote = CloudVolumeRemote({"protocol" : "gcp", "cloudpath" : "iarpa_microns/minnie/minnie65/seg", "token" : "public"})

resource = CloudVolumeResource("gcp", "iarpa_microns/minnie/minnie65/seg")

bboxx = [60000, 64000]
bboxy = [65000, 69000]
bboxz = [16000, 20000]

relavent_ids = remote.get_ids_in_region(resource=resource, resolution=0, x_range=bboxx, y_range=bboxy, z_range=bboxz)

print(relavent_ids)
