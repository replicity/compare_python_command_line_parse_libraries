# vim: fileencoding=utf-8

from __future__ import print_function

import click


@click.command()
@click.option('-f', '--force', is_flag=True, help='set branch name even if it shadows an existing branch')
@click.option('-C', '--clean', is_flag=True, help='reset branch name to parent branch name')
@click.option('-r', '--rev', nargs=1, help='change branches of the given revs (EXPERIMENTAL)')
@click.argument('NAME', nargs=1)
def branch(force, clean, rev, name):
    print('force {}'.format(force))
    print('clean {}'.format(clean))
    print('rev {}'.format(rev))
    print('name {}'.format(name))
