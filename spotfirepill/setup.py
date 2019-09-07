import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spotfirepill",
    version="0.14",
    author="Vengat",
    author_email="tagnev.vengat@gmail.com",
    description="This will use spotfire REST API end points to login & execute the jobs",
    long_description="""Using Spotfire class. Create the object to instantiate the spotfire class.
        And then login using "Client Id" & "Client Secret" to execute the jobs & check the status.



        Example
        -------

        pip install spotfirepill

        import spotfirepill as spt
        spot_fire_instance = spt.SpotFire(base_url,client_id,client_secret)
        spot_fire_instance.login()


        # Execute the Job
        spot_fire_instance.start_library('{job_id}')
        it returns job execution id

        #Get the Status

        spot_fire_instance.get_status('{job execution id}')""",
    long_description_content_type="text/markdown",
    url="https://github.com/tagnev/spotfirepill",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    spotfire_requires='>=7.14',
)
