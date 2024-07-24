import msf_2024
import numpy as np
import pytest

def test_build_bond_list():
    coordinates=np.array([[-1.40,0,0],
                         [0,0,1.4],
                         [0,0,0],
                         [0,1.4,0],
                         [0,-1.4,0]])
    bonds=msf_2024.build_bond_list(coordinates,1.5,0)
    assert len(bonds)==4, 'Expected 4 bonds'
    for bond_length in bonds.values():
        assert pytest.approx(bond_length) == 1.4, 'Expected a bond length of 1.4'

def test_fail_build_bond_list():
    coordinates=np.array([[-1.40,0,0],
                        [0,0,1.4],
                        [0,0,0],
                        [0,1.4,0],
                        [0,-1.4,0]])
    
    msf_2024.build_bond_list(coordinates=coordinates,max_bond=0)
    with pytest.raises(ValueError):
        msf_2024.build_bond_list(coordinates=coordinates,max_bond=-1)