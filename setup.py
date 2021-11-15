from setuptools import setup, find_packages
import glob
import os
import pkg_resources
# Note: the _program variable is set in __init__.py.
# it determines the name of the package/final command line tool.
from pangolin_assignment import __version__, _program

setup(name='pangolin_assignment',
      version=__version__,
      packages=find_packages(),
      scripts=[],
      package_data={'pangolin_assignment':['pango_assignment.cache.csv.gz']},
      description='cached pangolin assignments',
      url='https://github.com/cov-lineages/pangolin-assignment',
      author='cov-lineages group',
      entry_points="""
      [console_scripts]
      {program} = pangolin_assignment.command:main
      """.format(program = _program),
      include_package_data=True,
      keywords=[],
      zip_safe=False)
