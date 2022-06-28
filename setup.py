from setuptools import setup
from typing import List

 

def get_requirements_list()->List[str]:
    """
    This function is going to return list of requiremnet
    mentioned in requiremnents.txt file

    return a list which contain name of libraries mentioned in requiremnets.txt file
    """

    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

#Declaring variables form setup functions
PROJECT_NAME = "HOUSING-PREDICTION"
VERSION = "0.0.1"
AUTHOR = "SHREYA"
DESCRIPTON = "This is my first ML project"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"

setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTON,
packages = PACKAGES,
install_requires = get_requirements_list()
)


if __name__ == "__main__":
    print(get_requirements_list())
