import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='test_1',  
     version='0.1',
     scripts=['test_1'] ,
     author="srikant hiremath",
     author_email="srikant.hiremath@discoverdollar.com",
     description="add numbers",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/discoverdollartech/test_1",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
