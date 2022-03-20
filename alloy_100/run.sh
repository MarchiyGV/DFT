#!/usr/bin/env bash

module purge
module load intel libraries/mkl intel-mpich/scalapack intel/mpich
sbatch task
tail -f "base.out"
