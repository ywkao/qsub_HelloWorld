#!/usr/bin/env python2
import os
import sys

year = sys.argv[1]
path = os.getcwd()
command = '"cd {0}; ./hello.sh {1} {2}"'
list = "list_samples"

counter = 0
file = open(list, "r")
for x in file:
    counter = counter + 1
    tagName="hello_{}".format(counter)
    print tagName, command.format(path, year, x.rstrip())
    os.system('./submitJOB.py --command={} --name={}'.format(command.format(path, year, x.rstrip()), tagName))
