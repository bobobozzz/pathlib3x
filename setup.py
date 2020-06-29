"""
Setuptools entry point.
see : https://docs.python.org/3.8/distutils/setupscript.html
"""

import codecs
import os
import pathlib
from typing import List

from setuptools import setup                # type: ignore
from setuptools import find_packages


def is_travis_deploy() -> bool:
    if 'travis_deploy' in os.environ:
        if os.environ['travis_deploy'] == 'True':
            return True
    return False


def is_tagged_commit() -> bool:
    if 'TRAVIS_TAG' in os.environ:
        if os.environ['TRAVIS_TAG'] != '':
            return True
    return False


def strip_links_from_required(l_required: List[str]) -> List[str]:
    """
    >>> required = ['lib_regexp @ git+https://github.com/bitranox/lib_regexp.git', 'test']
    >>> assert strip_links_from_required(required) == ['lib_regexp', 'test']

    """
    l_req_stripped = list()                                        # type: List[str]
    for req in l_required:
        req_stripped = req.split('@')[0].strip()
        l_req_stripped.append(req_stripped)
    return l_req_stripped


long_description = 'backport of latest pathlib to python 3.6, 3.7 with a few extensions'   # will be overwritten with long_description if exists !
path_readme = pathlib.Path(__file__).parent / 'README.rst'

if path_readme.exists():
    # noinspection PyBroadException
    try:
        readme_content = codecs.open(str(path_readme), encoding='utf-8').read()
        long_description = readme_content
    except Exception:
        pass


def get_requirements_from_file(requirements_filename: str) -> List[str]:
    """
    >>> assert len(get_requirements_from_file('requirements.txt')) > 0
    """
    l_requirements = list()
    with open(str(pathlib.Path(__file__).parent / requirements_filename), mode='r') as requirements_file:
        for line in requirements_file:
            line_data = get_line_data(line)
            if line_data:
                l_requirements.append(line_data)
    return l_requirements


def get_line_data(line: str) -> str:
    line = line.strip()
    if '#' in line:
        line = line.split('#', 1)[0].strip()
    return line


tests_require = get_requirements_from_file('requirements_test.txt')
install_requires = get_requirements_from_file('requirements.txt')
setup_requires = list(set(tests_require + install_requires))

# for deploy on pypi we must not rely on imports from github
if is_travis_deploy() and is_tagged_commit():
    setup_requires = strip_links_from_required(setup_requires)
    # tests_require = strip_links_from_required(tests_require)
    # install_requires = strip_links_from_required(install_requires)

if __name__ == '__main__':
    setup(name='pathlib3x',
          version='0.1.0',
          url='https://github.com/bitranox/pathlib3x',
          packages=find_packages(),
          package_data={'pathlib3x': []},
          description='backport of latest pathlib to python 3.6, 3.7 with a few extensions',
          long_description=long_description,
          long_description_content_type='text/x-rst',
          author='Robert Nowotny',
          author_email='bitranox@gmail.com',
          classifiers=['Development Status :: 5 - Production/Stable', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Natural Language :: English', 'Operating System :: OS Independent', 'Programming Language :: Python', 'Topic :: Software Development :: Libraries :: Python Modules'],
          entry_points={'console_scripts': ['pathlib3x = pathlib3x.pathlib3x_cli:cli_main']},
          # minimally needs to run tests - no project requirements here
          tests_require=tests_require,
          # specify what a project minimally needs to run correctly
          install_requires=install_requires + ['typing', 'pathlib'],
          # minimally needs to run the setup script, dependencies needs also to put here for "setup.py install test"
          # dependencies must not be put here for pip install
          setup_requires=setup_requires,
          zip_save=False
          )