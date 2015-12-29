from gitUtils.GitUtils import checkoutBranch, changeDirectoryPath, gitFetch, gitStatus

def checkoutBranches(path, projects, branches):
    mapper = map(lambda project, branch: (project, branch), projects, branches)
    for (project, branch) in mapper:
        print(project)
        gitStatus()
        changeDirectoryPath(path + project)
        gitFetch()
        checkoutBranch(branch)

if __name__ == '__main__':
    path = ''
    projects = ['ConvertingQueries']
    branches = ['master']
    checkoutBranches(path, projects, branches)