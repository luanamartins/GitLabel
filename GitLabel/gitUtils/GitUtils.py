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
    return subprocess.call(["git", "fetch"])

def gitStatus():
    return subprocess.call(["git", "status"])

def checkoutBranch(branch):
    return subprocess.call(["git", "checkout", branch])

