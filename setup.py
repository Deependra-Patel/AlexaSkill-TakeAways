import os
import shutil
from subprocess import call

BOLD = '\033[1m'

if __name__ == '__main__':
    """
    Running `python setup.py` will generate a takeaways.zip file which can
    be uploaded to the AWS Lambda website and be used as a fully functioning
    lambda function.
    """

    # Place takeaways.py, data and requests into zip_folder
    print("Adding contents to zip folder")
    os.mkdir('zip_folder')
    zip_folder = 'zip_folder/'
    call(['cp', 'get_nearby_takeaways.py', 'lambda_function.py', zip_folder])

    packages_dir = 'venv/lib/python3.6/site-packages/'
    for package in os.listdir(packages_dir):
        if package.endswith('.so') or package.endswith('.py'):
            shutil.copyfile(packages_dir + package, zip_folder + package)
        else:
            shutil.copytree(packages_dir + package, zip_folder + package)

    # Zip contents of zip_folder
    print("Zipping contents")
    shutil.make_archive('takeaways', 'zip', 'zip_folder')

    # Delete the zip folder
    shutil.rmtree(zip_folder)

    print(BOLD + "takeaways.zip is now created - upload this to AWS Lambda"
          + BOLD)
