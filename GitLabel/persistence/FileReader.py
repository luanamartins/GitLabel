from os import walk

def listFolders(path):
    directories = []
    for (_, dirnames, _) in walk(path):
        directories.extend(dirnames)
        break
    return directories