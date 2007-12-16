#!/usr/bin/env python

from distutils.core import setup
import glob


setup(name='Statlib',
      version='1.0',
      description='A collection of statistical modules.',
      author='Raymond Hettinger, Gary Strangman',
      author_email='python@rcn.com, strang@nmr.mgh.harvard.edu',
      url='http://www.nmr.mgh.harvard.edu/Neural_Systems_Group/gary/python.html, http://users.rcn.com/python/download/python.htm',
      packages = ["statlib"],
      data_files = [("Lib/test", glob.glob("test/*.TXT"))]
      
      
     )