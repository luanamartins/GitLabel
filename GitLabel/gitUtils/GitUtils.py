from os import walk
import os
import subprocess

def listBranches(path):
    os.chdir(path)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    branchesFilepath = BASE_DIR + '/files/branchesFilepath.txt'
    branchesFile = open(branchesFilepath, 'w+')
    subprocess.call(["git", "branch", "-r"], stdout=branchesFile)
    b = open(branchesFilepath, 'r')
    branches = []
    for branchFullname in b:
        lines = branchFullname.split("/")
        print(lines[len(lines) - 1])
        branches.append(lines[len(lines) - 1])
        
def checkoutBranch(path, branch):
    subprocess.call(["git", "checkout", branch])
    
def listFolders(path):
    directories = []
    for (_, dirnames, _) in walk(path):
#       files.extend(filenames)
        directories.extend(dirnames)
        break
    return directories