# vim: fileencoding=utf-8

from __future__ import print_function

from subprocess import call

import click


@click.command()
@click.option('-a', is_flag=True, help='Include directory entries whose names begin with a dot (.).')
@click.option('-l', is_flag=True, help='(The lowercase letter ``ell''.)  List in long format. \
                                        (See below.) If the output is to a terminal, a total sum \
                                        for all the file sizes is output on a line before the long listing.')
@click.option('-t', is_flag=True, help='Sort by time modified (most recently modified first) \
                                        before sorting the operands by lexicographical order.')
def click_ls(a, l, t):

    cmd = 'ls'

    option = ' -'
    if a:
        option += 'a'
    if l:
        option += 'l'
    if t:
        option += 't'
    if option == ' -':
        option = ''

    print()

    return_code = call(cmd + option, shell=True)

    print()

    print("a : {}, l : {}, t : {}".format(a, l, t))
    print("return_code: {}".format(return_code))


if __name__ == '__main__':
    click_ls()
