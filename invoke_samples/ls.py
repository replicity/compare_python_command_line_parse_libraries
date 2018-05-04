from __future__ import print_function

from subprocess import call

from invoke import task

@task(help={
    'all': 'Include directory entries whose names begin with a dot (.).',
    'long': '(The lowercase letter ``ell''.)  List in long format. (See below.)  If the output is to a terminal, a total sum for all the file sizes is output on a line before the long listing.',
    'time': 'Sort by time modified (most recently modified first) before sorting the operands by lexicographical order.'
    })
def ls(c, all=False, long=False, time=False):
    """
    ls
    """

    cmd = 'ls'
    option = ' -'
    if all:
        option += 'a'
    if long:
        option += 'l'
    if time:
        option += 't'

    if option == ' -':
        option = ''

    print()

    return_code = call(cmd + option, shell=True)

    print()

    print('all : {}'.format(all))
    print('long : {}'.format(long))
    print('time : {}'.format(time))
    print("return_code: {}".format(return_code))


