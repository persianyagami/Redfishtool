#!/usr/bin/python
# Copyright Notice:
# Copyright 2016 DMTF. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfishtool/blob/master/LICENSE.md

# redfishtool:  redfishtool.py
#
# contents:
#  -CLI wrapper:  calls main() routine in ./redfishtool  package
#
#  Note: structure supports a future lib interface to the routines
#        where the libWrapper is the interface
#
from redfishtool import main
import sys

if __name__ == "__main__":
    main(sys.argv)



