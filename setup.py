from setuptools import setup,find_packages
from setuptools.command.install import install as _install
from codecs import open
from os import path


class Install(_install):
	def run(self):
		_install.do_egg_install(self)

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

# Get requirements.txt for required packages
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as r:
	temp_packages = r.readlines()
	required_packages = []
	for item in temp_packages:
		required_packages.append(item.strip())
	
setup (name='AwsConsoleBackend',
		version='1.0.0',
		description='Aws custom console REST interface',
		long_description=long_description,

		# The project's main homepage.
		url='https://github.com/deepukr85/aws-console-backend',

		# Author details
		author='Deepu K R',
		author_email='deepukr85@gmail.com',

		# calls custom command install class declared above which installs language models
		cmdclass={'install': Install},

		classifiers=[
		# How mature is this project? Common values are
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stable
		'Development Status :: 3 - Alpha',

		# Indicate who your project is intended for
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',

		# Specify the Python versions you support here. In particular, ensure
		# that you indicate whether you support Python 2, Python 3 or both.
		'Programming Language :: Python :: 3.5',
		],

		# What does your project relate to?
		keywords='AWS custom console REST',

		# You can just specify the packages manually here if your project is
		# simple. Or you can use find_packages().
		packages=find_packages(exclude=['contrib', 'docs', 'tests']),
		
		# List run-time dependencies here.  These will be installed by pip when
		# your project is installed. For an analysis of "install_requires" vs pip's
		# requirements files see:
		# https://packaging.python.org/en/latest/requirements.html

		install_requires=required_packages,

		# List additional groups of dependencies here (e.g. development
		# dependencies). You can install these using the following syntax,
		# for example:
		# $ pip install -e .[dev,test]
		extras_require={
			'dev': ['check-manifest'],
			'test': ['coverage'],
		}

		)
