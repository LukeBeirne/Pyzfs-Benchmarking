import argparse
import os
import subprocess
import libzfs_core as zfs

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

inputfile = args.filename


# File exists error checking
if not os.path.isfile(inputfile):
	print('Invalid file input')
	quit()


# Opening and reading file
f = open(inputfile, "r")




# Defining ZFS classes and functions

class zpool:
	def __init__(self, name, vdev):
		self.name = name
		self.vdev = vdev


def delete_zpool(name):
	destroy = subprocess.call(['sudo', 'zpool', 'destroy', name])
	return destroy



# Creating zpool

name = 'pool1'


try:
	create = subprocess.call(['sudo', 'zpool', 'create', name, os.getcwd()+'/'+inputfile])
	status = subprocess.check_output(['zpool', 'status'])
	print(status)
finally:
	f.close()
	delete_zpool(name)



# attempt to get zpool properties
# with pyzfs functions

try:
	properties = zfs.lzc_get_props(b'name')
	print(properties)
finally:
	f.close()
	delete_zpool(name)

f.close()
destroy = delete_zpool(name)
