from setuptools import setup
from setuptools import find_packages

import mlogger

setup(
    name='mlogger',
    version=mlogger.__version__,

    description='Logging library',
    long_description='Logging library',
    keywords='mlogger',

    author=mlogger.__author__,
    author_email=mlogger.__email__,
    url=mlogger.__url__,

    packages=find_packages(exclude=['docs']),
    classifiers=[
        'Framework :: mlogger',
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=mlogger.__license__,
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "requests < 3",
        "Django == 3.2.0"
        "django - log - request - id"
        ,
    ],
)
