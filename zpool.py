import argparse
import os
import subprocess
import libzfs_core

#
# Setting up libzfs_core import
#
# PYTHONPATH environment variable:
# export PYTHONPATH=zfs/contrib/pyzfs
#
# Python3 should recognize libzfs_core
# as a package to import
#


# Parsing input config file
parser = argparse.ArgumentParser()
parser.add_argument('filename', type = str)

args = parser.parse_args()


