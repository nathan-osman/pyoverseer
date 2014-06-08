from distutils.core import setup

from pyoverseer import VERSION

setup(
    name='pyoverseer',
    version='.'.join([str(n) for n in VERSION]),
    description="Server and client for monitoring statistics on services running on servers.",
    author='Nathan Osman',
    author_email='admin@quickmediasolutions.com',
    url='https://github.com/nathan-osman/pyoverseer',
    license='MIT',
    packages=['pyoverseer']
)
