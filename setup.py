from setuptools import setup, find_packages
import re, ast

# get version from __version__ variable in nilighttheme/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('nilighttheme/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

# Reading requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='nilighttheme',
    version=version,
    description='Light Material Theme for Frappe',
    author='Randy Lowery',
    author_email='lowerymayorga@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements,
)
