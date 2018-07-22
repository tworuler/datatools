import click
import numpy as np
from PIL import Image
from termcolor import cprint
from datatools import common
from datatools.logger import logger


def print_array(array):
    shape = array.shape
    array = np.reshape(array, -1)
    for v in array:
        print(v)


@click.command(help='Display numpy array content')
@click.argument('file', type=click.File('rb'))
def readnpy(file):
    a = np.load(file)
    print('shape: ', a.shape)
    print('dtype: ', a.dtype)
    print(a)


@click.command(help='Display numpy array attributes')
@click.argument('file', nargs=-1, type=click.Path(exists=True, dir_okay=False))
def readnpys(file):
    print('SHAPE', 'DTYPE')
    for f in file:
        a = np.load(f)
        cprint(f + ':', 'magenta', end='')
        print(a.shape, a.dtype)


@click.command(help='Show image')
@click.argument('file', nargs=-1, type=click.Path(exists=True))
@click.option('--head', '-h', is_flag=True, help='print description')
@click.option('--value', '-v', is_flag=True, help='print array value')
@click.option('--palette', '-p', type=int, help='palette mode')
@click.option('--show', is_flag=True, help='show image')
def readimg(file, head, value, palette, show):
    is_single_file = (len(file) == 1)
    if head:
        print('FORMAT HxW MODE')
    for f in file:
        try:
            image = Image.open(f)
        except OSError:
            logger.error('Invalid image "{}"'.format(f))
            continue
        w, h = image.size
        if head:
            if not is_single_file:
                cprint(f + ':', 'magenta', end='')
            print('{} {}x{} {}'.format(image.format, h, w, image.mode))
        if value:
            array = np.asarray(image)
            print_array(array)
        if palette is not None:
            palette_value = common.PALETTES[palette]
            image.putpalette(palette_value)
        if show:
            image.show()

