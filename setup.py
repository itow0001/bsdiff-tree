'''
Created on Apr 29, 2016

@author: iitow
'''
from setuptools import setup, find_packages
SRCDIR = 'src'
def readme():
    ''' Spits out README.rst for our long_description
    with open('README.rst', 'r') as fobj:
        return fobj.read()
    '''
setup(
    name='bstree',
    version='1.0.1',
    description="diff all files and executables in 2 trees provides a list of files/executables changed. Systems [Freebsd, Linux, OSX]",
    long_description=readme(),
    author='Ian Itow',
    author_email='itow0001@gmail.com',
    url='https://github.com/itow0001/bsdiff-tree',
    license='MIT',
    classifiers=[
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.7',
    ],
    package_dir={'': SRCDIR},
    packages=find_packages(SRCDIR),
    zip_safe=False,
    install_requires=[
    ],
    entry_points={
        'console_scripts': ['bstree = bsdiff_tree.__main__:main']
    },
    include_package_data=True,
)