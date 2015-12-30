from os import walk
import os
import subprocess

def changeDirectoryPath(path):
    os.chdir(path)

def gitCurrentBranch():
    return subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])

def listBranches(path):
    os.chdir(path)
    output = subprocess.check_output(["git", "branch", "-r"])
    output = output.decode(encoding='utf_8').split('\n')
    return map(lambda br : br.strip(), output)

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
