# setup.py is to build our application as a package
from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    
setup(
    
    name='mlproject',
    version='0.0.1',
    author='Nikki',
    author_email='nbeedala@andrew.cmu.edu',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt'),
    
)