from setuptools import setup

import re
import platform
import os
import sys

if 'test' in sys.argv:
    # Setup test unloads modules after the tests have completed. This causes an
    # error in atexit's exit calls because the registered modules no longer
    # exist.  This hack resolves this issue by disabling the register func
    import atexit
    atexit.register = lambda be_gone_nasty_traceback: True


def load_version(filename='yara/version.py'):
    """Parse a __version__ number from a source file"""
    with open(filename) as source:
        text = source.read()
        match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", text)
        if not match:
            msg = "Unable to find version number in {}".format(filename)
            raise RuntimeError(msg)
        version = match.group(1)
        return version

data_files = []
libpath = os.path.join(
    'libs', platform.system().lower(), platform.machine().lower(),
    'libyara.so'
)
if os.path.exists(libpath):
    data_files.append(('lib', [libpath]))

setup(
    name="yara",
    version=load_version(),
    packages=['yara'],
    data_files=data_files,
    zip_safe=False,
    author="Michael Dorman",
    author_email="mjdorma@gmail.com",
    url="http://code.google.com/p/yara-project/",
    description="Compile YARA rules to test against files or strings",
    long_description=open('README.rst').read(),
    license="Apache Software Licence",
    install_requires=[],
    entry_points={
        'console_scripts': [
            'yara-ctypes = yara.cli:entry'
            ]
    },
    platforms=['cygwin', 'win', 'linux'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Security',
        'Topic :: System :: Monitoring'
    ],
    test_suite="tests"
)


