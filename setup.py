import os
import os.path
import sys
import versioneer

# NumPy 1.11.2 contains a bug which prevents submodules from working correctly
# on Python 3.4 unless importlib.machinery has been imported at some time.
try:
    import importlib.machinery
except:
    pass

from setuptools import find_packages

DISTNAME = 'scikit-survival'
DESCRIPTION = 'Survival analysis built on top of scikit-learn'
MAINTAINER = 'Sebastian Pölsterl'
MAINTAINER_EMAIL = 'sebp@k-d-w.org'
URL = 'https://github.com/sebp/scikit-survival'


def configuration(parent_package='', top_path=None):
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    from numpy.distutils.misc_util import Configuration

    config = Configuration(None, parent_package, top_path)

    # Avoid non-useful msg:
    # "Ignoring attempt to set 'name' (from ... "
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)

    config.add_subpackage('sksurv')

    return config


def setup_package():
    metadata = dict(name=DISTNAME,
                    author=MAINTAINER,
                    author_email=MAINTAINER_EMAIL,
                    description=DESCRIPTION,
                    license="GPLv3+",
                    url=URL,
                    version=versioneer.get_version(),
                    cmdclass=versioneer.get_cmdclass(),
                    classifiers=['Development Status :: 4 - Beta',
                                 'Intended Audience :: Science/Research',
                                 'Intended Audience :: Developers',
                                 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                                 'Operating System :: POSIX',
                                 'Operating System :: Unix',
                                 'Programming Language :: C',
                                 'Programming Language :: Python',
                                 'Programming Language :: Python :: 3.4',
                                 'Programming Language :: Python :: 3.5',
                                 'Topic :: Software Development',
                                 'Topic :: Scientific/Engineering',
                    ],
                    packages=find_packages(),
                    install_requires=[
                        'cvxopt',
                        'cvxpy',
                        'numexpr',
                        'numpy',
                        'pandas >=0.18.0, <0.19',
                        'scipy',
                        'scikit-learn >=0.18.0, <0.19'],
                    extras_require={
                        'tests': [
                            'nose',
                            'coverage'],
                        'docs': [
                            'sphinx >= 1.4',
                            'numpydoc']}
    )

    if (len(sys.argv) >= 2
        and ('--help' in sys.argv[1:] or sys.argv[1]
        in ('--help-commands', 'egg_info', '--version', 'clean'))):

        # For these actions, NumPy is not required.
        try:
            from setuptools import setup
        except ImportError:
            from distutils.core import setup

        metadata['version'] = versioneer.get_version()
    else:
        from numpy.distutils.core import setup

        metadata['configuration'] = configuration

    setup(**metadata)


if __name__ == "__main__":
    py_version = sys.version_info[:2]
    if py_version < (3, 4):
        raise RuntimeError('Python 3.4 or later is required')

    setup_package()
