"""Test input file calculate.FiniteElement."""
import logging
import json
import pytest
from apbs.input_file.calculate.finite_element import FiniteElement


_LOGGER = logging.getLogger(__name__)


GOOD_TEMPLATE = {
    "a priori refinement": None,
    "boundary condition": None,
    "calculate energy": True,
    "calculate forces": True,
    "charge discretization": None,
    "domain length": None,
    "error based refinement": None,
    "error tolerance": 1e-3,
    "equation": None,
    "ions": None,
    "initial mesh resolution": 0.5,
    "initial mesh vertices": 100000,
    "maximum refinement iterations": 10,
    "maximum vertices": 10000000,
    "molecule": "foo",
    "solute dielectric": 12,
    "solvent dielectric": 78.54,
    "solvent radius": 1.4,
    "surface method": None,
    "surface spline window": 0.3,
    "temperature": 298.15,
    "use maps": None,
    "write atom potentials": "atom_potentials.txt",
    "write maps": [
        {"property": "potential", "format": "dx.gz", "path": "pot.dx.gz"}
    ],
}
GOOD_A_PRIORI_REFINEMNT = ["geometric", "uniform"]
GOOD_BOUNDARY_CONDITIONS = [
    "zero",
    "single sphere",
    "multiple sphere",
    "focus foo",
]
GOOD_BEER = ["White Bluffs FID"]
GOOD_CHARGE_DISCRETIZATIONS = ["linear", "cubic", "quintic"]
GOOD_EQUATIONS = [
    "linearized pbe",
    "nonlinear pbe",
    "linearized regularized pbe",
    "nonlinear regularized pbe",
]
GOOD_IONS = [
    {
        "species": [
            {"charge": +2, "radius": 2.0, "concentration": 0.050},
            {"charge": 1, "radius": 1.2, "concentration": 0.100},
            {"charge": -1, "radius": 2.0, "concentration": 0.200},
        ]
    },
    {
        "species": [
            {"charge": 1, "radius": 1.2, "concentration": 0.100},
            {"charge": -1, "radius": 2.0, "concentration": 0.100},
        ]
    },
]
GOOD_SURFACE_METHODS = [
    "molecular surface",
    "smoothed molecular surface",
    "cubic spline",
    "septic spline",
]
GOOD_USEMAP_INPUTS = [
    [{"property": prop, "alias": "foo"}]
    for prop in [
        "dielectric",
        "ion accessibility",
        "charge density",
        "potential",
    ]
]


@pytest.mark.parametrize("test_variable", GOOD_BOUNDARY_CONDITIONS)
def test_boundary_conditions(test_variable):
    """Test Focus calculation type."""
    input_dict = GOOD_TEMPLATE
    input_dict["boundary condition"] = test_variable
    input_dict["charge discretization"] = GOOD_CHARGE_DISCRETIZATIONS[0]
    input_dict["equation"] = GOOD_EQUATIONS[0]
    input_dict["ions"] = GOOD_IONS[0]
    input_dict["surface method"] = GOOD_SURFACE_METHODS[0]
    input_dict["use maps"] = GOOD_USEMAP_INPUTS[0]
    _LOGGER.debug(json.dumps(input_dict, indent=2))
    obj = FiniteElement(dict_=input_dict)
    dict_ = obj.to_dict()
    obj = FiniteElement(dict_=dict_)
    obj.validate()

    with pytest.raises(ValueError):
        input_dict["boundary condition"] = "foo"
        obj = FiniteElement(dict_=input_dict)
        obj.validate()
