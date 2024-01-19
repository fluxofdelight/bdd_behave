from setuptools import setup, find_packages


setup(
    name='BDD',
    version='1.0',
    description='',
    author='fluxofdelight',
    author_email='',
    url='https://github.com/fluxofdelight/bdd',
    packages=find_packages(),
    python_requires='>=3.11, <4',
    install_requires=[
        "behave==1.2.6",
        "selenium==4.15.2"
    ]
)
