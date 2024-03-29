# from setuptools import setup

# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()

# ## edit below variables as per your requirements -
# REPO_NAME = "Movie_Recommender_System_Using_Machine_Learning"
# AUTHOR_USER_NAME = "ravi0dubey"
# SRC_REPO = "src"
# LIST_OF_REQUIREMENTS = ['streamlit']


# setup(
#     name=SRC_REPO,
#     version="0.0.1",
#     author=AUTHOR_USER_NAME,
#     author_email="ravidatascience4@gmail.com",
#     description="A small package for Movie Recommender System",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
#     packages=[SRC_REPO],
#     license="MIT",
#     python_requires=">=3.7",
#     install_requires=LIST_OF_REQUIREMENTS
# )

from setuptools import find_packages, setup

setup(
    name="catdog",
    version="0.0.1",
    author="Ravi Dubey",
    author_email="Ravi0dubey@gmail.com",
    packages=find_packages(),
    install_requires=[],
)