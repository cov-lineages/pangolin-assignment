from setuptools import setup, find_packages
import glob
import os
import pkg_resources
import git
from setuptools.command.install import install as _install

# Note: the _program variable is set in __init__.py.
# it determines the name of the package/final command line tool.
from pangolin_assignment import __version__, _program

class install(_install):
    def pull_first(self):
        """This script is in a git directory that can be pulled."""
        cwd = os.getcwd()
        gitdir = os.path.dirname(os.path.realpath(__file__))
        os.chdir(gitdir)
        g = git.cmd.Git(gitdir)
        try:
            g.execute(['git', 'lfs', 'pull'])
        except git.exc.GitCommandError:
            raise RuntimeError("Make sure git-lfs is installed!")
        os.chdir(cwd)
    
    def run(self):
        self.pull_first()
        super().run()

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
      install_requires=["git-lfs"],
      include_package_data=True,
      keywords=[],
      cmdclass={'install': install},
      zip_safe=False)
