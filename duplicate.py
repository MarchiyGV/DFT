pseudopotentials = {'Ni': 'Ni.upf',
                    'Ag': 'Ag.upf'}
from ase.calculators.espresso import Espresso
from ase.constraints import FixAtoms
from ase.io.espresso import read_espresso_out, write_espresso_in
from ase.io import read, write
write('abc.xyz', read('abc.traj'))

file = 'base.out'
structure = read_espresso_out(file)
structure = structure.repeat((2,2,1))
write_espresso_in('repeated.in', structure)
