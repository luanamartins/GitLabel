from os import walk
import os
import subprocess

def changeDirectoryPath(path):
    os.chdir(path)

def gitCurrentBranch():
    return subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])

def listBranches(path):
    os.chdir(path)
    currentWorkingPath = os.path.dirname(os.path.dirname(__file__))
    branchesFilepath = currentWorkingPath + '/files/branchesFilepath.txt'
    branchesFile = open(branchesFilepath, 'w+')
    subprocess.call(["git", "branch", "-r"], stdout = branchesFile)
    b = open(branchesFilepath, 'r')
    branches = []
    for branchFullname in b:
        lines = branchFullname.split("/")
        print(lines[len(lines) - 1])
        branches.append(lines[len(lines) - 1])
    return branches

def gitFetch():
    res = subprocess.call(["git", "fetch"])
    print(res)

def gitStatus():
    res = subprocess.call(["git", "status"])
    print(res)

def checkoutBranch(branch):
    res = subprocess.call(["git", "checkout", branch])
    print('Checkout = ' + str(res))

def listFolders(path):
    directories = []
    for (_, dirnames, _) in walk(path):
#       files.extend(filenames)
        directories.extend(dirnames)
        break
    return directories
