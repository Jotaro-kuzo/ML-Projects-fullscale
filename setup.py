
from setuptools import setup, find_packages
from typing import List


PROJECT_NAME="Housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Santhosh_2548"
DESCRIPTION = "This is full end to end House price prediction project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."


def get_requirements_list()->List[str]:

    """
    Description: This function is going to return list of requiremnets ,emtioned in requiremnents.txt file

    return This function is going to return a list which contains the list of libraries mentioned in requiremnets file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list



setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description=DESCRIPTION,
packages = find_packages(),
install_requires = get_requirements_list()

)



