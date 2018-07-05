import json
import sys

args = sys.argv

jsonFile = open(args[1], 'r')
jsonData = json.load(jsonFile)

print(jsonData)
