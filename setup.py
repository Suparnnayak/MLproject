from setuptools import find_packages,setup
from typing import List

A="-e ."

def get_requirements(file_path:str)->List[str]:
    # this function will return list of requirements

    requirements=[]
    with open(file_path) as file_obk:
        requirements=file_obk.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if A in requirements:
            requirements.remove(A)
    return requirements

setup(
    name='Mlproject',
    version='0.0.1',
    author='Krish',
    author_email='suparnnayak56@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)