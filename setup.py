from setuptools import setup,find_packages
from typing import List
HYPHEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This Function will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
    name="ML_project",
    version=0.1,
    author="Krishna mittal",
    author_email="krishnamittal403@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
    
)
