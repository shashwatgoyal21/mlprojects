

from setuptools import find_packages, setup
from typing import List


exclude = "-e ."

def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file1:
        requirements=file1.readlines()
        requirements= [req.replace("\n","") for req in requirements]
            
        if exclude in requirements:
            requirements.remove(exclude)

    return requirements


setup(
    name='ML Project',
    version = '0.0.1',
    author='shashwat',
    author_email='shasha.shardool@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='ML project'
)
