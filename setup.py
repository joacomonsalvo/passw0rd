from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="passw0rd",
    version="0.0.1",
    description="Password Generator",
    url="https://github.com/joacomonsalvo/passw0rd",
    author="Joaco Monsalvo",
    author_email="",
    pymodules=["passw0rd"],
    package_dir={"": "src"},

    install_requires=[
        # "something ~= 0.1",
    ],

    extra_require={
        "dev": [
          "pytest >= 3.7",
        ],
    },

    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['python', 'password', 'generator', 'pwd', 'passw0rd'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
