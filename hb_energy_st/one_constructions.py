# NOT python 2.7
from honeybee.room import Room
from honeybee_energy.lib.constructionsets import construction_set_by_identifier


def hb_apply_construction_set(_rooms, _constr_set):
    """_summary_

    Args:
        _rooms (_type_): _description_
        _constr_set (_type_): _description_

    Returns:
        list: _description_
    """
    new_rooms = []
    for rm in _rooms:
        new_room = rm.duplicate()
        new_room.properties.energy.construction_set = _constr_set
        new_rooms.append(new_room)
    return new_rooms
