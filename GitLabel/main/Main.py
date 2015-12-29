from gitUtils.GitUtils import checkoutBranch, changeDirectoryPath, gitFetch, gitStatus
import sys

def checkoutBranches(mapper):
#     mapper = map(lambda project, branch: (project, branch), projects, branches)
    for (project, branch) in mapper:
        print(project)
        gitStatus()
        changeDirectoryPath(project)
        gitFetch()
        checkoutBranch(branch)

def main(args):
    print(args)
    tuples = eval("%s" % args)
    checkoutBranches(tuples)

if __name__ == '__main__':
    main(sys.argv[1])
