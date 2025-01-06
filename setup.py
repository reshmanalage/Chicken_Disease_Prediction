import setuptools

# Read the contents of your README file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

_version = "0.0.0"
REPO_NAME = "Chicken_Disease_Prediction"
AUTHOR_USER_NAME = "reshmanalage"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "reshmanalage2706@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=_version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
