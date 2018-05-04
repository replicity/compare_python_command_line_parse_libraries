# vim: fileencoding=utf-8

from __future__ import print_function

from argparse import ArgumentParser


def add(args):
    print("run add")
    print(args)


def branch(args):
    print("run branch")
    print(args)


def main():
    parser = ArgumentParser(description='argparse_hg sample')
    parser.add_argument('-y', '--noninteractive', action='store_true', help='do not prompt, automatically pick the first choice for all prompts')
    parser.add_argument('-v', '--verbose', action='store_true', help='enable additional output')
    parser.add_argument('--hidden', action='store_true', help='consider hidden changesets')

    subparsers = parser.add_subparsers()

    parser_add = subparsers.add_parser('add')
    parser_add.add_argument('-I', '--include', nargs=1, help='include nargs matching the given patterns')
    parser_add.add_argument('-X', '--exclude', nargs=1, help='exclude nargs matching the given patterns')
    parser_add.add_argument('-S', '--subrepos', action='store_true', help='recurse into subrepositories')
    parser_add.add_argument('-n', '--dry-run', action='store_true', help='do not perform actions, just print output')
    parser_add.set_defaults(func=add)

    parser_branch = subparsers.add_parser('branch')
    parser_branch.add_argument('-f', '--force', action='store_true', help='set branch name even if it shadows an existing branch')
    parser_branch.add_argument('-C', '--clean', action='store_true', help='reset branch name to parent branch name')
    parser_branch.add_argument('-r', '--rev', nargs=1, help='change branches of the given revs (EXPERIMENTAL)')
    parser_branch.add_argument('NAME', nargs=1, help='branch name')
    parser_branch.set_defaults(func=branch)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
