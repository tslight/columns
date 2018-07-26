import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="columns",
    version="0.0.2",
    author="Toby Slight",
    author_email="tobyslight@gmail.com",
    description="Print a list in columns.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tslight/columns",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'columns = columns.__main__:main',
        ],
    }
)
