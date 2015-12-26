from os import walk

def listGitFolders(path):
    directories = []
    for (_, dirnames, _) in walk(path):
#       files.extend(filenames)
        directories.extend(dirnames)
        break
    return directories

def writeOnFile(filepath, label, listOfFiles):
    extensionFile = ".txt"
    filepathForLabel = filepath + label + extensionFile
    file = open(filepathForLabel, 'w')
    for (projectName, branchFullname) in listOfFiles:
#         print(projectName + ";" + branchFullname)
        file.write(projectName + ";" + branchFullname)
        file.write('\n')
    file.close()
#     print(listOfFiles)


     
