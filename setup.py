from distutils.core import setup

setup(
    name='tube',
    version='1.0',
    author='Adam Gilman',
    author_email='me@adamgilman.com',
    packages=['tube'],
    url='http://pypi.python.org/pypi/tube/',
    license='LICENSE',
    description='Python object wrapper for TfL (Transport for London) TrackerNet information service',
    install_requires=[
        "requests >= 2.5.0",
        "xmltodict >= 0.9.0",
    ],
)