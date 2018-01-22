#!/usr/bin/env python3
from setuptools import (
    setup,
    find_packages
)

with open('requirements.txt', 'rb') as req_file:
    REQUIREMENTS = [str(req, encoding='ascii') for req in req_file.readlines()]

print(REQUIREMENTS)

setup(
    name='File Crawler',
    version='0.0.1',
    description='File crawling and indexing utility',
    author='Filip Hornak',
    author_email='None@None',
    url='http://None',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'filecrawl': 'types/*.json'},
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    scripts=['bin/crawler.py'],
    setup_requires=['pytest-runner'],
    test_requires=['pytest', 'pytest-cov', 'pytest-pylint'],
    test_suite='py.test',
    extras_require={
        'test': [
            'pytest',
            'pytest-runner'
        ],
        'docs': [
            'sphinx',
            'sphinxcontrib-napoleon'
        ]
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programing Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Topic :: Desktop Environment :: File Managers'
    ]
)