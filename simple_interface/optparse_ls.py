# vim: fileencoding=utf-8

from __future__ import print_function

from optparse import OptionParser
from subprocess import call

def main():
    parser = OptionParser(usage='optparse_ls sample')
    parser.add_option('-a', action='store_true',
                      help='Include directory entries whose names begin with a dot (.).')
    parser.add_option('-l', action='store_true',
                      help='(The lowercase letter ``ell''.)  List in long format.  (See below.) If the output is to a terminal, a total sum for all the file sizes is output on a line before the long listing.')

    parser.add_option('-t', action='store_true',
                      help='Sort by time modified (most recently modified first) before sorting the operands by lexicographical order.')

    (options, args) = parser.parse_args()

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

    print("options : {}".format(options))
    print("args : {}".format(args))
    print("return_code: {}".format(return_code))


if __name__ == '__main__':
    main()
