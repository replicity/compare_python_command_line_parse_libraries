# vim: fileencoding=utf-8

from __future__ import print_function

import click


@click.command()
@click.option('-y', '--noninteractive', is_flag=True, help='do not prompt, automatically pick the first choice for all prompts')
@click.option('-v', '--verbose', is_flag=True, help='enable additional output')
@click.option('--version', is_flag=True, help='output version information and exit')
@click.option('--hidden', is_flag=True, help='consider hidden changesets')
@click.option('-l', '--include', nargs=1, help='include names matching the given patterns')
@click.option('-x', '--exclude', nargs=1, help='exclude names matching the given patterns')
@click.option('-S', '--subrepos', is_flag=True, help='recurse into subrepositories')
@click.option('-n', '--dry-run', is_flag=True, help='do not perform actions, just print output')
@click.argument('FILE', nargs=-1)
def add(noninteractive, version, verbose, hidden, include, exclude, subrepos, dry_run, file):
    print('noninteractive {}'.format(noninteractive))
    print('verbose {}'.format(verbose))
    print('version {}'.format(version))
    print('hidden {}'.format(hidden))
    print('include {}'.format(include))
    print('exclude {}'.format(exclude))
    print('subrepos {}'.format(subrepos))
    print('dry-run {}'.format(dry_run))
    print('FILE {}'.format(file))
