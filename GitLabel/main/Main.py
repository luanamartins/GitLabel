from persistence.FileWriter import listGitFolders
import os
import subprocess

if __name__ == '__main__':
    path = ''
    gitProjectName = 'ClientChat'
    directories = listGitFolders(path)
#     print(directories)
    
    label = "Test projetos"
    os.chdir(path + gitProjectName)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    branchesFilepath = BASE_DIR + '/files/branchesFilepath.txt'
    branchesFile = open(branchesFilepath, 'w+')
    subprocess.call(["git", "branch", "-r"], stdout=branchesFile)
    b = open(branchesFilepath, 'r')
    for branchFullname in b:
        #print(branchFullname)
        lines = branchFullname.split("/")
        #print(lines)
        print(lines[len(lines) - 1])
        
    
        
        
