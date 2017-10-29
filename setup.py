
"""This file contains setup information for multiple data-structures."""


from setuptools import setup


setup(
    name='Data-Structures',
    description='Contains setup for Data-Structures modules.',
    author='Kinley Ramson',
    author_email='kinleyramson@gmail.com',
    package_dir={'': 'src'},
    py_modules=[],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov']}
)
