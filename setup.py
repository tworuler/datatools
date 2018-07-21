from distutils.core import setup

setup(
    name='datatools',
    version=0.1,
    packages=['datatools'],
    entry_points="""
        [console_scripts]
        dt=datatools:cli
    """
)
