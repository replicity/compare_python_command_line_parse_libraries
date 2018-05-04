# vim: fileencoding=utf-8

from __future__ import print_function

from argparse import ArgumentParser
from subprocess import call


def main():
    parser = ArgumentParser(description='argparse_ls sample')
    parser.add_argument('-a', action='store_true',
                      help='Include directory entries whose names begin with a dot (.).')
    parser.add_argument('-l', action='store_true',
                      help='(The lowercase letter ``ell''.)  List in long format.  (See below.) If the output is to a terminal, a total sum for all the file sizes is output on a line before the long listing.')
    parser.add_argument('-t', action='store_true',
                      help='Sort by time modified (most recently modified first) before sorting the operands by lexicographical order.')

    options = parser.parse_args()

    cmd = 'ls'

    option = ' -'
    if options.a:
        option += 'a'
    if options.l:
        option += 'l'
    if options.t:
        option += 't'
    if option == ' -':
        option = ''

    print()

    return_code = call(cmd + option, shell=True)

    print()
    # write ls processing code here

    print("options : {}".format(options))
    print("return_code: {}".format(return_code))


if __name__ == '__main__':
    main()
