# vim: fileencoding=utf-8
"""docopt_hg

Usage:
    docopt_hg.py [-y] [-v] [--version] [-h] [--hidden] [--help] <command> [<args>...]

Options:
    -y --noninteractive     do not prompt, automatically pick the first choice for all prompts
    -v --verbose            enable additional output
    --version               output version information and exit
    -h --help               display help and exit
       --hidden             consider hidden changesets

Sub command list
    add          add the specified files on the next commit
    branch       set or show the current branch name
    help         show help for a given topic or a help overview

"""

from __future__ import print_function

from subprocess import call
from docopt import docopt


def main():
    args = docopt(__doc__,
                  version='docopt_hg version 0.0.1',
                  options_first=True)
    argv = [args['<command>']] + args['<args>']

    if args['<command>'] in 'add branch commit ci'.split():
        exit(call(['python', 'docopt_hg_{}.py'.format(args['<command>'])] + argv))
    elif args['<command>'] in ['help', None]:
        exit(call(['python', 'docopt_hg.py', '--help']))
    else:
        exit("%r is not a docopt_hg.py command. See 'hg help -v'." % args['<command>'])


if __name__ == '__main__':
    main()
