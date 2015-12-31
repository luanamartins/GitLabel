from os import chdir
import subprocess

def changeDirectoryPath(path):
    chdir(path)

def gitCurrentBranch():
    return subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])

def listBranches(path):
    changeDirectoryPath(path)
    output = gitBranch()
    output = output.decode(encoding='utf_8').split('\n')
    return map(lambda branch : branch.strip(), output)

def gitBranch():
    return subprocess.check_output(["git", "branch", "-r"])

def gitFetch():
    res = subprocess.call(["git", "fetch"])
    print(res)

def gitStatus():
    res = subprocess.call(["git", "status"])
    print(res)

def checkoutBranch(branch):
    res = subprocess.call(["git", "checkout", branch])
    print('Checkout = ' + str(res))

