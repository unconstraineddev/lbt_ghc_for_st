# No Shame Random Drawer.py
from honeybee.boundarycondition import Outdoors
from honeybee.facetype import Wall
from honeybee.room import Room
from honeybee.face import Face
from honeybee.aperture import Aperture
from honeybee.door import Door
from honeybee.orientation import angles_from_num_orient, face_orient_index


def is_exterior_wall(face):
    """Check whether a given Face is an exterior Wall."""
    return isinstance(face.boundary_condition, Outdoors) and \
        isinstance(face.type, Wall)
