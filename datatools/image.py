import os
import sys
import click
import numpy as np
from PIL import Image

from datatools.logger import logger
from datatools.common import PALETTES


IMAGE_FORMATS = ['jpg', 'jpeg', 'png']


def imgcvt_single(src, dst, format, mode, suffix, overwrite):
    if dst is None:
        root, ext = os.path.splitext(src)
        if not ext or ext[1:] not in IMAGE_FORMATS:
            root = src
        if suffix is not None:
            root += suffix
        if format is not None:
            ext = '.' + format
        dst = root + ext
    logger.info('Converting {} => {}'.format(src, dst))
    if not overwrite and os.path.exists(dst):
        logger.warning('DST file "{}" exists '.format(dst))
        return
    image = Image.open(src)
    if mode is not None and image.mode != mode:
        image_data = np.asarray(image)
        image = Image.fromarray(image_data)
        image = image.convert(mode)
    image.save(dst)


@click.command(help='Convert image')
@click.argument('src', required=False,
                type=click.Path(exists=True, dir_okay=False))
@click.argument('dst', required=False)
@click.option('--format', required=False, type=click.Choice(IMAGE_FORMATS),
              help='destination image format')
@click.option('--mode', required=False, type=click.Choice(Image.MODES),
              help='destination image mode')
@click.option('--suffix', required=False,
                help='add suffix to destination image name')
@click.option('--overwrite', is_flag=True,
                help='overwrite the destination image file')
def imgcvt(src, dst, format, mode, suffix, overwrite):
    if src is None:
        for line in sys.stdin:
            paths = line.strip().split()
            if len(paths) == 1:
                src_path = paths[0]
                dst_path = None
            elif len(paths) == 2:
                src_path = paths[0]
                dst_path = paths[1]
            else:
                logger.error('Invalid arguments: ' + line)
                continue
            imgcvt_single(src_path, dst_path, format, mode, suffix, overwrite)
    else:
        imgcvt_single(src, dst, format, mode, suffix, overwrite)

