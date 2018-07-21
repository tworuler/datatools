from distutils.core import setup

setup(
    name='datatools',
    version=1.0,
    packages=['datatools'],
    entry_points="""
        [console_scripts]
        dt=datatools:cli
    """
)
