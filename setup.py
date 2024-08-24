from setuptools import setup, find_packages


def get_requirements(file_path:str)-> list[str]:
    ''' this functions will return the list of requirements'''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='chetan chowdhari',
    author_email='chetan@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)