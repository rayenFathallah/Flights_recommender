from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(filepath:str)->List[str]: 
    ''' Return the list of requirements'''
    requirements = list()
    with open(filepath) as file_obj : 
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if not req.startswith('-e')]
    return requirements

setup(
    name='Flights_recommender',
    version='0.0.1',
    author='Oussama',
    author_email='',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)