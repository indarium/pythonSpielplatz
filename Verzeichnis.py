import os, sys
path = "c:/Test"

def search(path):
    fileslist = []
    if os.path.isdir(path):
        elements = os.listdir( path )
        for element in elements:
            currentElement = os.path.join(path, element)
            if os.path.isdir(currentElement)==False:
                fileslist.append(currentElement)
            else:
                fileslist = fileslist + search(currentElement)
    return fileslist

fl = []
fl = search(path)
for file in fl:
  print file
