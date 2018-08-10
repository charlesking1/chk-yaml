#!/usr/bin/python3

import sys, os, types, re
import ruamel.yaml as yaml
# from jinja2 import Environment, FileSystemLoader

if len(sys.argv) <= 1:
    print
    print("Usage: python3 ", sys.argv[0] ," <yaml file>")
    print("where: ")
    print(" <yaml file> = location of the yaml file")
    sys.exit(1)


yamlfile = sys.argv[1]

# define Airwaves dictionary
airwaves = {
	'a': '10.1.1.1', 
	'b': '10.2.2.2', 
	'c': '10.3.3.3' 
}

# Depending on the file extension we load the data file differently..
filename, file_extension = os.path.splitext(yamlfile)

if file_extension == ".json":
    print("Error: Script does not expect .json file")
    sys.exit(1)
elif file_extension == ".yml":
    ## Load YAML data file..
    with open(yamlfile) as stream:
        try:
            dataObj = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

else:
    print("Error: Unrecognised file extension (.yml)")
    sys.exit(1)


# Capture directory for template file..
yamlfile_dir= os.path.dirname(os.path.abspath(yamlfile))

# Test #1 for whitespace in filename
# "\s" matches Unicode whitespace
if re.search(r"\s", yamlfile):
   print ("Error: Filename contains whitespace.")

# Test #2 check issatelite value exists by get(key) which returns value for key in dict
if dataObj.get('issatellite') is not None:
   print("issatelite value = ", dataObj[issatellite])
else:
   print("Error: issatellite value key is MISSING !! Fix YAML file")


# Test #3 check amsserver is IP, not FQDN
#if dataObj.get('awmsserver') is not None:
   

# Test #4 Check p2psubnet against Infoblox matches


# Test
print("got to here")

# dataObj is:  <class 'dict'> 
print("dataObj is: ", type(dataObj), "\n")

print("Airwaves is: ", type(airwaves), "\n")

print(dataObj.items(), "\n")
print(dataObj.keys(), "\n")
print("Values: ", "\n", dataObj.values(), "\n")

print("got to 2nd point")

sys.exit(0)
