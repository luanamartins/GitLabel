# GitLabel

This project aims to organize branches on git repositories. The core idea is to tag a feature, binding it to a set of branches on diferent projects. Those projects suppose to work together, although they are currently based in different branches.

## Requirements for development
 - Python 3.4
 - Eclipse Mars
 - Unittest

## Process
- Checkout the branch
- Create a tag to a tuple (Project, Branch)
- Whether a checkout fails, undo previous checkouts to older branch

## Installation instructions
 - TO DO

## Configuration instructions
 - TO DO
 
## Commands
- gitlabel checkout “label”
- gitlabel add “label” [(“project 1”, “branch 1”), (“project 2”, “branch 2”)]


## Copyright and licensing information
GNU GENERAL PUBLIC LICENSE (Version 2, June 1991)
Copyright (C) 1989, 1991 Free Software Foundation, Inc., http://fsf.org/ 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.
