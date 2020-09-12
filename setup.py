from setuptools import setup, find_packages

__version__ = "1.0.0"

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requirements = ["boto3>=1.14.0", "docopt" >= "0.6.2", "termcolor>=1.1.0"]

setup(
    name="ssmpsm",
    version=__version__,
    author="Craig Hurley",
    author_email="none@example.com",
    description="Get/set AWS SSM parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    keywords="ssm, parameter, aws",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
)
