import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spotfirepill",
    version="0.10",
    author="Vengat",
    author_email="tagnev.vengat@gmail.com",
    description="This will use spotfire REST API end points to login & execute the jobs",
    long_description="using this package, we can execute the existing the  Spofire Automation jobs and check the status",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    spotfire_requires='>=7.14',
)
