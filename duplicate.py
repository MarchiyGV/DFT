pseudopotentials = {'Ni': 'Ni.upf',
                    'Ag': 'Ag.upf'}
from ase.calculators.espresso import Espresso
from ase.constraints import FixAtoms
from ase.io.espresso import read_espresso_out, write_espresso_in
from ase.io import read, write

file = 'base.out'
out = 'repeated.txt'
N_lay = 5
#structure = read_espresso_out(file)
structure = read(file)
print(structure)
structure = structure.repeat((2,2,1))
mask = [print(atom.tag) for atom in structure]
structure.set_constraint(FixAtoms(mask=mask))
with open(out, 'w') as f:
    write_espresso_in(f, structure)

with open(out, 'r') as f:
    for line in f:
        print(line)
