# NOT python 2.7
from honeybee.room import Room
from honeybee_energy.lib.constructionsets import construction_set_by_identifier
from honeybee.typing import clean_and_id_ep_string, clean_ep_string
from honeybee_energy.material.opaque import EnergyMaterial


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

#! Copied from grasshopper POST-testing if it works, AFTER DEBUGGING A COUPLE TIMES!!


def hb_opaque_mat(_name, _thickness, _cond, _density,
                  _spec_heat, _roughness_=None, _therm_absp_=None,
                  _sol_absp_=None, _vis_absp_=None):

    _roughness_ = 'MediumRough' if _roughness_ is None else _roughness_
    _therm_absp_ = 0.9 if _therm_absp_ is None else _therm_absp_
    _sol_absp_ = 0.7 if _sol_absp_ is None else _sol_absp_
    name = clean_and_id_ep_string('OpaqueMaterial') if _name is None else \
        clean_ep_string(_name)

    # create the material
    mat = EnergyMaterial(
        name, _thickness, _cond, _density, _spec_heat, _roughness_,
        _therm_absp_, _sol_absp_, _vis_absp_)
    if _name is not None:
        mat.display_name = _name

    return mat
