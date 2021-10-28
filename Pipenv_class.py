'''
Virtual environment -> Environment with proper settings for a project.You can have multiple VE and use a version
of library or even python in each one, following your project needs.

Site to find libraries: www.pypi.org

Useful libraries -> requests, numpy

How to install a Virtual environment in windows:
1. Open CMD
2. Run "pip --version" to check your pip version. It must to be from python 3.7
3. Run " pip install --user pipenv" to install pipenv in the actual user
4. It will show a warning. Copy the directory that is in that.
5. Open "Edit the system environment variables". Click on "Environment variables" than search for "Path" in "User variables for miked"
6. Click in "Edit", than in "new" and paste the directory that is in your transference area. Click in "ok" twice
7. Open a new terminal. Run "pipenv --version". You'll see that the pipenv is intalled.
8. Open visual studio code and the terminal in it.
9. Create a new folder. Each one for a project
10. Enter in the using directory.  
11. Use "pipenv --three". It will create the Virtual Environment
12. It will be create a Pipfile. It will be a file with the project informations.
13. pipenv intall library -> It installs the latest version of a library in the VE
14. It will be created a Pipfile.lock with the library informations
15. pipenv install library==version -> It installs the defined version of a library in the VE
16. If you enter in another project, it will not have the same libraries. So you can install any version you want
'''
