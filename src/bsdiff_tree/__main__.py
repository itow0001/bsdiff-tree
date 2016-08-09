'''
    Main entry for bstree
'''
from __future__ import absolute_import
import argparse
import os
from bsdiff_tree.modules.manager import Manager


def menu():
    '''
    The Menu is here
    '''
    parser = argparse.ArgumentParser(
        description='diff all files and executables in 2 trees provide a list of files changed')
    parser.add_argument('-o',
                        action="store",
                        dest="origin",
                        help='Origin tree, base path')
    parser.add_argument('-n',
                        action="store",
                        dest="new",
                        help='New tree, base path')
    parser.add_argument('-p',
                        action="store",
                        dest="path",
                        help='absolute path to place output')
    parser.add_argument('-e',
                        action='append',
                        dest="excludes",
                        default=[],
                        help='exclude files or directories')
    parser.add_argument('-E',
                        action='store',
                        dest="excludes_file",
                        default=[],
                        help='All excludes from a file')
    parser.add_argument('-d',
                        action="store_true",
                        dest="debug",
                        default=False,
                        help='enable debug messages')
    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s 1.0')
    return parser.parse_args()

def main():
    '''
    This is used in the cli and from a couple places
    '''
    options = menu()
    if not options.origin or not options.new or not options.path:
        print "[Error] need -o, -n, -f"
        os.sys.exit(1)
    m = Manager(options)
if __name__ == '__main__':
    main()