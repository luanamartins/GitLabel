from gitUtils.GitUtils import checkoutBranch, changeDirectoryPath, gitFetch

if __name__ == '__main__':

    path = ''
    projects = ['ClientChat', 'ServerChat', 'ConvertingQueries']
#     branches = ['feature-user-interface', 'feature-structure', 'feature-structure']
    branches = ['master', 'master', 'master']
    mapper = map(lambda proj, branch: (proj, branch), projects, branches)
    for (proj, branch) in mapper:
        print(proj)
        changeDirectoryPath(path + proj)
        gitFetch()
        checkoutBranch(branch)
