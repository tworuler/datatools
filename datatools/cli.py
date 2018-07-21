#!/usr/bin/env python
# coding: utf-8


import click
from datatools.reader import readnpy


@click.group()
def cli():
    pass


cli.add_command(readnpy)


if __name__ == '__main__':
    cli()

