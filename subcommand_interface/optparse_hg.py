# vim: fileencoding=utf-8
"""optparser subcommand sample"""


from __future__ import print_function

from optparse import OptionParser
import sys


def add(options, args):
    print("run add")
    print("options : {}".format(options))
    print("args : {}".format(args))


def branch(options, args):
    print("run branch")
    print("options : {}".format(options))
    print("args : {}".format(args))


def main():
    version = 1.0

    commands = {}
    commands['help'] = """optparse_subcommand.py subcommand [options] \nCommands:
        add          add the specified files on the next commit
        branch       set or show the current branch name
        help         show help for a given topic or a help overview
    """
    commands['add'] = 'docopt_hg.py add [options] [-I PATTERNS] [-X PATTERNS] [-S] [-n] PATH...'
    commands['branch'] = 'docopt_hg.py branch [options] [-f] [-C] [-r VALUE] NAME'

    if len(sys.argv) < 2:
        run_command = 'help'
    else:
        run_command = sys.argv[1]
        if run_command not in commands:
            # 想定外のコマンド
            run_command = 'help'

    parser = OptionParser(description=__doc__, version='%prog version ' + str(version))

    # set help message
    parser.set_usage(commands[run_command])

    # set global optin
    parser.add_option('-y', '--noninteractive', action='store_true', help='do not prompt, automatically pick the first choice for all prompts')
    parser.add_option('-v', '--verbose', action='store_true', help='enable additional output')
    parser.add_option('--hidden', action='store_true', help='consider hidden changesets')

    # set individual command option
    if run_command == 'add':
        parser.add_option('-I', '--include', type='string', nargs=1, help='include nargs matching the given patterns')
        parser.add_option('-X', '--exclude', type='string', nargs=1, help='exclude nargs matching the given patterns')
        parser.add_option('-S', '--subrepos', action='store_true', help='recurse into subrepositories')
        parser.add_option('-n', '--dry-run', action='store_true', help='do not perform actions, just print output')
    if run_command == 'branch':
        parser.add_option('-f', '--force', action='store_true', help='set branch name even if it shadows an existing branch')
        parser.add_option('-C', '--clean', action='store_true', help='reset branch name to parent branch name')
        parser.add_option('-r', '--rev', type='string', nargs=1, help='change branches of the given revs (EXPERIMENTAL)')

    (options, args) = parser.parse_args()

    if run_command == 'help':
        parser.print_help()
    else:
        exec("%s(options, args)" % (run_command))


if __name__ == '__main__':
    main()
