import logging


FORMAT = '%(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('datatools')
logger.setLevel(logging.INFO)

