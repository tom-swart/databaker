from setuptools import setup, find_packages

long_desc = """
Transform Excel spreadsheets
"""
# See https://pypi.python.org/pypi?%3Aaction=list_classifiers for classifiers

conf = dict(
    name='databaker',
    version='2.0.0',
    description="DataBaker, part of QuickCode for ONS",
    long_description=long_desc,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    keywords='',
    author='The Sensible Code Company Ltd',
    author_email='feedback@sensiblecode.io',
    url='https://github.com/sensiblecodeio/databaker',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=['docopt', 'xypath @git+https://github.com/tom-swart/xypath.git#egg=xypath', 'xlutils', 'pyhamcrest'],
    tests_require=[],
    entry_points={
        'console_scripts': [
            'databaker_nbconvert = databaker.databaker_nbconvert:main',
            ]
        },
    )

if __name__ == '__main__':
    setup(**conf)
