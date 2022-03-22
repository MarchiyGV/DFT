from ase.io import read, write
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", required=False, default='out_removed.poscar')
parser.add_argument("-o", "--out-name", dest='out', required=False, default='removed.pwi')
args = parser.parse_args()

file = args.name
out = args.out
structure = read(file)
print(structure)
with open(out, 'w') as f:
    write(f, structure, format='lammps-data')

with open(out, 'r') as f:
    for line in f:
        print(line)
