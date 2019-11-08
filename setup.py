# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os


# file read helper
def read_from_file(path):
    if os.path.exists(path):
        with open(path, "rb", "utf-8") as input:
            return input.read()


version = "4.6.0"

setup(
    name='heiko',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description='Heiko is a frontend for MaaS',
    long_description=read_from_file('README.md'),
    long_description_content_type="text/markdown",

    # The project's main homepage.
    url='https://github.com/k4cg/heiko',

    # Author details
    author='K4CG',
    author_email='info@k4cg.org',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'Topic :: Terminals',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='mate matomat beer drinks accounting',
    packages=find_packages(),
    zip_safe=True,

    # dependencies
    install_requires=[
        'certifi>=14.05.14',
        'six>=1.10',
        'python_dateutil>=2.5.3',
        'setuptools>=21.0.0',
        'urllib3>=1.15.1',
        'sty',
        'tabulate',
        'pyyaml',
        'pygame',
        'watson_developer_cloud',
    ],

    # extra_requires
    extras_require={
        'dev': [
            'bumpversion',
            'gitchangelog',
            'twine',
            'setuptools',
        ]
    },

    entry_points={
        'console_scripts': [
            'heiko=heiko:main',
        ],
    },
)
