# vim: fileencoding=utf-8
"""docopt_hg_add

Usage:
    docopt_hg.py add [options] [-I PATTERNS] [-X PATTERNS] [-S] [-n] PATH...

Global Options:
    -y --noninteractive     do not prompt, automatically pick the first choice for all prompts
    -v --verbose            enable additional output
    --version               output version information and exit
    -h --help               display help and exit
       --hidden             consider hidden changesets

Specific docopt_hg.py add actions:
    -I PATTERNS --include=PATTERNS      include names matching the given patterns
    -X PATTERNS --exclude=PATTERNS      exclude names matching the given patterns
    -S --subrepos                       recurse intn subrepositories
    -n --dry-run                        do not perform actions, just print output

"""

from __future__ import print_function

from docopt import docopt


def main():
    args = docopt(__doc__,
                  version='docopt_hg version 0.0.1')
    print(args)


if __name__ == '__main__':
    main()
