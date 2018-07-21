#!/usr/bin/env python
# coding: utf-8


import click
from datatools.reader import readnpy
from datatools.reader import readimg


@click.group()
def cli():
    pass


cli.add_command(readnpy)
cli.add_command(readimg)


if __name__ == '__main__':
    cli()

