from setuptools import setup, find_packages

setup(
    name='pygo',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    setup_requires=[
        "cffi>=1.13.2"
    ],
    install_requires=[
        "cffi>=1.13.2"
    ],
    cffi_modules=[
        "pygo_build:ffibuilder"
    ],  # "filename:global"
)