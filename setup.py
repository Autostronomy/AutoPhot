from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="autophot",
    version="1.0.0",    
    description="Sorry this has moved to: AstroPhot. Please run: pip install astrophot",
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    url="https://github.com/Autostronomy/AutoPhot",
    author="Connor Stone",
    author_email="connorstone628@gmail.com",
    license="GPL-3.0 license",
    packages=find_packages(),
    install_requires=["numpy"],
    entry_points = {
        'console_scripts': [
            'autophot = autophot:run_from_terminal',
        ],
    },
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",  
        "Programming Language :: Python :: 3",
    ],
)
