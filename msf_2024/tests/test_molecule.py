import msf_2024
import numpy as np
import pytest

@pytest.fixture
def methane_molecule():
    coordinates=np.array([[-1.4000001,0,0],
                            [0,0,1.4],
                            [0,0,0],
                            [0,1.4,0],
                            [0,-1.4,0]])
    return coordinates

# def test_build_bond_list(methane_molecule):
#     coordinates=methane_molecule
#     bonds=msf_2024.build_bond_list(coordinates,1.5,0)
#     assert len(bonds)==4, 'Expected 4 bonds'
#     for bond_length in bonds.values():
#         assert pytest.approx(bond_length) == 1.4, 'Expected a bond length of 1.4'

def test_fail_build_bond_list(methane_molecule):
    coordinates=methane_molecule
    msf_2024.build_bond_list(coordinates=coordinates,max_bond=0)
    with pytest.raises(ValueError):
        msf_2024.build_bond_list(coordinates=coordinates,max_bond=-1)




@pytest.mark.parametrize('max_bond',np.linspace(1,5,4))
@pytest.mark.parametrize('min_bond',np.linspace(0,0.5,4))
def test_build_bond_list(methane_molecule,max_bond,min_bond):
    coordinates=methane_molecule
    bonds=msf_2024.build_bond_list(coordinates,max_bond,min_bond)
    assert len(bonds) in (0,4,9,10), f'Expected 0 or 4 bonds, not {len(bonds)}'
    for bond_length in bonds.values():
        assert pytest.approx(bond_length) in (1.4,1.9798990580330125,2.8), f'Expected a bond length of 1.4, not {bond_length}'
