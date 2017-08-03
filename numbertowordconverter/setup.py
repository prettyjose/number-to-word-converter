#-*-coding:utf8;-*-
#qpy:3
#qpy:console


"""A setuptools based setup module.

See:

https://packaging.python.org/en/latest/distributing.html

https://github.com/pypa/sampleproject

"""


# Always prefer setuptools over distutils

from setuptools import setup
#from setuptools.command.install import install 


# To use a consistent encoding

#from codecs import open

from os import path


here = path.abspath(path.dirname(__file__))

print(path.join(here, 'README.rst'))

long_desc=open(path.join(here, 'README.rst'), encoding='utf-8').read()
print(long_desc)
packages = ['numbertowordconverter','numbertowordconverter.tests']
setup(
    name='numbertowordconverter',
    version='0.0.1',
    description='a simple converter',
    long_description=long_desc,
    author='pjose',
    packages=packages,
    

)