## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

#fetch value from package.xml
setup_args = generate_distutils_setup(
        packages=['iwtros_goal'],
        package_dir={'': 'script'})

setup(**setup_args)