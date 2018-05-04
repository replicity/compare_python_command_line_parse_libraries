# vim: fileencoding=utf-8
"""docopt_ls

Usage:
    docopt_ls.py [-ahlt]

Options:
    -a              Include directory entries whose names begin with a dot (.).
    -h              Show help
    -l              (The lowercase letter ``ell''.)  List in long format.
                    (See below.)  If the output is to a terminal, a total sum
                    for all the file sizes is output on a line before the long listing.
    -t              Sort by time modified (most recently modified first)
                    before sorting the operands by lexicographical order.

"""

from __future__ import print_function

from subprocess import call
from docopt import docopt


def main():
    args = docopt(__doc__)
    option_a = args['-a']
    option_l = args['-l']
    option_t = args['-t']

    cmd = 'ls'

    option = ' -'
    if option_a:
        option += 'a'
    if option_l:
        option += 'l'
    if option_t:
        option += 't'
    if option == ' -':
        option = ''

    print()

    return_code = call(cmd + option, shell=True)

    print()

    print("options : {}".format(option))
    print("return_code: {}".format(return_code))


if __name__ == '__main__':
    main()
