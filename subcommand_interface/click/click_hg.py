# vim: fileencoding=utf-8

from __future__ import print_function

import click_hg_add
import click_hg_branch

import click


@click.group()
@click.option('-y', '--noninteractive', is_flag=True, help='do not prompt, automatically pick the first choice for all prompts')
@click.option('-v', '--verbose', is_flag=True, help='enable additional output')
@click.option('--version', is_flag=True, help='output version information and exit')
@click.option('--hidden', is_flag=True, help='consider hidden changesets')
def click_hg(noninteractive, verbose, version,  hidden):
    print('noninteractive {}'.format(noninteractive))
    print('verbose {}'.format(verbose))
    print('version {}'.format(version))
    print('hidden {}'.format(hidden))


click_hg.add_command(click_hg_add.add)
click_hg.add_command(click_hg_branch.branch)

if __name__ == '__main__':
    click_hg()
