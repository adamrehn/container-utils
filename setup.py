from os.path import abspath, dirname, join
from setuptools import setup

# Read the README markdown data from README.md
with open(abspath(join(dirname(__file__), 'README.md')), 'rb') as readmeFile:
	__readme__ = readmeFile.read().decode('utf-8')

setup(
	name='container-utils',
	version='0.0.1',
	description='Utility functionality for working with Docker containers',
	long_description=__readme__,
	long_description_content_type='text/markdown',
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Topic :: Software Development :: Build Tools',
		'Environment :: Console'
	],
	keywords='docker container utilities',
	url='http://github.com/adamrehn/container-utils',
	author='Adam Rehn',
	author_email='adam@adamrehn.com',
	license='MIT',
	packages=['container_utils'],
	zip_safe=True,
	python_requires = '>=3.5',
	install_requires = [
		'docker>=3.7.0',
		'setuptools>=38.6.0',
		'twine>=1.11.0',
		'wheel>=0.31.0'
	]
)
