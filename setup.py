import setuptools

with open("README.md","r",encoding = 'utf-8') as f:
    long_description = f.read()



__version__ = '0.0.0'

REPO_NAME = 'kidney-Disease-Classification-Deep-Learning-Project'
AUTHOR_USER_NAME = 'Farukuddin'
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "farukuddin.md12@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description="A pyhton pacakge for CNN app",
    Long_description = long_description,
    Long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls  = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir = {"": "src"},
    packages= setuptools.find_packages(where = "src")
)
