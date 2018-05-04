# vim: fileencoding=utf-8
"""docopt_hg_branch

Usage:
    docopt_hg.py branch [options] [-f] [-C] [-r VALUE] NAME

Global Options:
    -y --noninteractive     do not prompt, automatically pick the first choice for all prompts
    -v --verbose            enable additional output
    --version               output version information and exit
    -h --help               display help and exit
       --hidden             consider hidden changesets

Specific docopt_hg.py add actions:
    -f --force              set branch name even if it shadows an existing branch
    -C --clean              reset branch name to parent branch name
    -r --rev VALUE          change branches of the given revs (EXPERIMENTAL)

"""

from __future__ import print_function

from docopt import docopt


def main():
    args = docopt(__doc__,
                  version='docopt_hg version 0.0.1')
    print(args)


if __name__ == '__main__':
    main()
